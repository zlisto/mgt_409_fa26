"""Minimal Dash chat shell for a screen-aware PydanticAI agent.

Run:  python app.py
Open: immersive window via desktop.py (browser left, this chat on the right)

Build agent.py and prompts/prompt.md in class. Style this UI yourself.
"""

from __future__ import annotations

import threading
import traceback
import uuid

from dash import Dash, Input, Output, State, clientside_callback, dcc, html, no_update

from agent import run_agent

app = Dash(__name__)

# Dash Interval can fire twice for one send; claim each pending id once.
_TURN_LOCK = threading.Lock()
_CLAIMED_TURNS: set[str] = set()

app.layout = html.Div(
    [
        html.H2("Screen helper"),
        html.P(id="screen-status", children="No screenshot yet."),
        dcc.Store(
            id="chat-history",
            data=[{"role": "assistant", "content": "Hi — ask me about what you're looking at."}],
        ),
        dcc.Store(id="last-shot", data=None),
        dcc.Store(id="pending-request", data=None),
        dcc.Store(id="scroll-sink", data=None),
        dcc.Interval(id="agent-poll", interval=250, n_intervals=0, max_intervals=0, disabled=True),
        html.Div(
            id="chat-window",
            style={
                "height": "420px",
                "overflowY": "auto",
                "border": "1px solid #ccc",
                "padding": "12px",
                "marginBottom": "12px",
            },
        ),
        dcc.Textarea(
            id="composer",
            style={"width": "80%", "height": "70px"},
            placeholder="Type a message…",
        ),
        html.Button("Send", id="send-button", n_clicks=0),
        html.P("Enter to send · Shift+Enter for a new line"),
    ],
    style={"maxWidth": "720px", "margin": "24px auto", "fontFamily": "sans-serif"},
)


def render_messages(history, pending):
    blocks = []
    for msg in history or []:
        who = "Assistant" if msg["role"] == "assistant" else "You"
        blocks.append(
            html.Div(
                [html.Strong(f"{who}: "), dcc.Markdown(msg["content"], link_target="_blank")],
                style={"marginBottom": "10px"},
            )
        )
        tools = msg.get("tool_events") or []
        if tools:
            blocks.append(
                html.Ul(
                    [html.Li(f"Used: {t.get('name', '?')}") for t in tools],
                    style={"color": "#666", "fontSize": "0.85rem", "marginTop": "-4px"},
                )
            )
    if pending:
        blocks.append(
            html.Div(
                [html.Strong("Assistant: "), html.Span("…")],
                style={"color": "#888"},
                role="status",
                **{"aria-live": "polite"},
            )
        )
    return blocks


@app.callback(
    Output("chat-window", "children"),
    Input("chat-history", "data"),
    Input("pending-request", "data"),
)
def update_chat(history, pending):
    return render_messages(history, pending)


@app.callback(Output("screen-status", "children"), Input("last-shot", "data"))
def update_screen_status(last_shot):
    if not last_shot:
        return "No screenshot yet."
    when = last_shot.get("captured_at", "?")
    region = last_shot.get("region", "window")
    return f"Last look: {when} · {region}"


@app.callback(
    Output("chat-history", "data", allow_duplicate=True),
    Output("pending-request", "data"),
    Output("composer", "value"),
    Output("agent-poll", "disabled"),
    Output("agent-poll", "n_intervals"),
    Output("agent-poll", "max_intervals"),
    Input("send-button", "n_clicks"),
    State("composer", "value"),
    State("chat-history", "data"),
    State("pending-request", "data"),
    prevent_initial_call=True,
)
def submit_message(_send, text, history, pending):
    if pending or not text or not text.strip():
        return no_update, no_update, no_update, no_update, no_update, no_update
    message = text.strip()
    updated = [*(history or []), {"role": "user", "content": message}]
    return updated, {"text": message, "id": str(uuid.uuid4())}, "", False, 0, 1


@app.callback(
    Output("chat-history", "data", allow_duplicate=True),
    Output("pending-request", "data", allow_duplicate=True),
    Output("last-shot", "data"),
    Output("agent-poll", "disabled", allow_duplicate=True),
    Input("agent-poll", "n_intervals"),
    State("pending-request", "data"),
    State("chat-history", "data"),
    State("last-shot", "data"),
    prevent_initial_call=True,
)
def complete_agent_turn(n_intervals, pending, history, last_shot):
    if not pending or not n_intervals:
        return no_update, no_update, no_update, True if not pending else no_update

    turn_id = pending.get("id") or str(uuid.uuid4())
    with _TURN_LOCK:
        if turn_id in _CLAIMED_TURNS:
            return no_update, no_update, no_update, True
        _CLAIMED_TURNS.add(turn_id)

    try:
        print(f"\nagent turn: {pending['text']!r}", flush=True)
        result = run_agent(pending["text"])
        tools = result.get("tool_events", [])
        if tools:
            print("tools this turn: " + ", ".join(t.get("name", "?") for t in tools), flush=True)
        reply = {"role": "assistant", "content": result["text"], "tool_events": tools}
        new_shot = result.get("last_shot") or last_shot
    except Exception:
        traceback.print_exc()
        reply = {
            "role": "assistant",
            "content": "Something went wrong. Check PORTKEY_API_KEY in your .env and try again.",
        }
        new_shot = last_shot
    finally:
        with _TURN_LOCK:
            _CLAIMED_TURNS.discard(turn_id)

    return [*(history or []), reply], None, new_shot, True


clientside_callback(
    """
    function(n) {
        const el = document.getElementById('composer');
        if (!el || el.dataset.bound) return window.dash_clientside.no_update;
        el.dataset.bound = '1';
        el.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                document.getElementById('send-button').click();
            }
        });
        return window.dash_clientside.no_update;
    }
    """,
    Output("send-button", "n_clicks"),
    Input("send-button", "n_clicks"),
)

clientside_callback(
    """
    function(children, pending) {
        const el = document.getElementById('chat-window');
        if (!el) return window.dash_clientside.no_update;
        const pin = () => { el.scrollTop = el.scrollHeight; };
        pin();
        requestAnimationFrame(pin);
        setTimeout(pin, 50);
        return window.dash_clientside.no_update;
    }
    """,
    Output("scroll-sink", "data"),
    Input("chat-window", "children"),
    Input("pending-request", "data"),
)


if __name__ == "__main__":
    from desktop import run_desktop

    run_desktop()
