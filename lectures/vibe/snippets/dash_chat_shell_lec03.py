"""Minimal Dash chat shell for a Lecture 3 chatbot (tools + LLM).

Run:  python app.py
Open: http://127.0.0.1:8050

Wire your model + tools inside get_reply() (same file or import from chatbot.py).
Return {"text": "..."} and optionally "tool_events".
"""

from __future__ import annotations

import traceback
from typing import Any

from dash import Dash, Input, Output, State, dcc, html, no_update, clientside_callback


def get_reply(user_text: str, conversation_history: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Replace this with your OpenAI / Portkey call + tools.

    Must return at least {"text": "..."}.
    Optional: "tool_events": [{"name": "Yahoo price", "status": "completed"}, ...]
    so the UI can list what ran under the reply.
    """
    _ = conversation_history
    return {
        "text": (
            f"You said: {user_text}\n\n"
            "Replace get_reply() with your real chatbot (model + tools)."
        ),
        "tool_events": [],
    }


app = Dash(__name__)

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            @keyframes chat-pulse {
                0%, 100% { opacity: 0.25; }
                50% { opacity: 1; }
            }
            .chat-thinking::after {
                content: "...";
                letter-spacing: 0.05em;
                animation: chat-pulse 1s ease-in-out infinite;
            }
            .chat-tool-steps {
                color: #666;
                font-size: 0.85rem;
                margin: -4px 0 12px 0;
                padding-left: 0.25rem;
            }
            .chat-tool-steps li { margin: 2px 0; }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""

app.layout = html.Div(
    [
        html.H2("Stock research chat"),
        dcc.Store(
            id="chat-history",
            data=[{"role": "assistant", "content": "Hi — ask me about a stock."}],
        ),
        dcc.Store(id="pending-request", data=None),
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
        dcc.Textarea(id="composer", style={"width": "80%", "height": "70px"}, placeholder="Type a message…"),
        html.Button("Send", id="send-button", n_clicks=0),
        html.P("Enter to send · Shift+Enter for a new line"),
    ],
    style={"maxWidth": "720px", "margin": "24px auto", "fontFamily": "sans-serif"},
)


def render_messages(history, pending):
    blocks = []
    for msg in history or []:
        who = "Bot" if msg["role"] == "assistant" else "You"
        blocks.append(
            html.Div(
                [html.Strong(f"{who}: "), dcc.Markdown(msg["content"])],
                style={"marginBottom": "10px"},
            )
        )
        tools = msg.get("tool_events") or []
        if tools:
            blocks.append(
                html.Ul(
                    [html.Li(f"Used: {t.get('name', '?')}") for t in tools],
                    className="chat-tool-steps",
                )
            )
    if pending:
        blocks.append(
            html.Div(
                [html.Strong("Bot "), html.Span(className="chat-thinking")],
                style={"color": "#888"},
                role="status",
                **{"aria-live": "polite"},
            )
        )
    return blocks


@app.callback(Output("chat-window", "children"), Input("chat-history", "data"), Input("pending-request", "data"))
def update_chat(history, pending):
    return render_messages(history, pending)


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
def submit_message(_, text, history, pending):
    if pending or not text or not text.strip():
        return no_update, no_update, no_update, no_update, no_update, no_update
    updated = [*(history or []), {"role": "user", "content": text.strip()}]
    return updated, {"text": text.strip()}, "", False, 0, 1


@app.callback(
    Output("chat-history", "data", allow_duplicate=True),
    Output("pending-request", "data", allow_duplicate=True),
    Output("agent-poll", "disabled", allow_duplicate=True),
    Input("agent-poll", "n_intervals"),
    State("pending-request", "data"),
    State("chat-history", "data"),
    prevent_initial_call=True,
)
def complete_chat_turn(_, pending, history):
    if not pending:
        return no_update, no_update, True
    try:
        print(f"\nchat turn: {pending['text']!r}", flush=True)
        result = get_reply(pending["text"], (history or [])[:-1])
        tools = result.get("tool_events", []) if isinstance(result, dict) else []
        text = result["text"] if isinstance(result, dict) else str(result)
        if tools:
            print("tools this turn: " + ", ".join(t.get("name", "?") for t in tools), flush=True)
        else:
            print("tools this turn: (none)", flush=True)
        reply = {"role": "assistant", "content": text, "tool_events": tools}
    except Exception:
        traceback.print_exc()
        reply = {"role": "assistant", "content": "Something went wrong. Check .env / Portkey and try again."}
    return [*(history or []), reply], None, True


# Enter sends; Shift+Enter keeps a newline
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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=False, use_reloader=False)
