#!/usr/bin/env python3
"""Generate lecture slide and vibe-coding HTML pages."""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = ROOT / "lectures" / "slides"
VIBE_DIR = ROOT / "lectures" / "vibe"

NAV = """  <nav class="site-nav">
    <ul class="navbar">
      <li><a href="../../index.html">Home</a></li>
      <li><a href="../../instructions.html">Instructions</a></li>
      <li><a href="../../lectures.html">Lectures</a></li>
      <li><a href="../../homeworks.html">Homeworks</a></li>
      <li><a href="../../project_requirements.html">Final Project</a></li>
    </ul>
    <button type="button" class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode"></button>
  </nav>"""


def esc(s):
    return html.escape(s, quote=False)


def slide_html(n, title, slides):
    parts = []
    for i, sl in enumerate(slides, 1):
        cls = sl.get("class", "")
        active = " active" if i == 1 else ""
        inner = sl["html"]
        parts.append(f'      <section class="slide{active}{(" " + cls) if cls else ""}" data-slide="{i}">\n{inner}\n      </section>')
    body = "\n".join(parts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lecture {n} Slides — {esc(title)}</title>
  <link rel="stylesheet" href="../../css/style.css">
  <link rel="stylesheet" href="../../css/slides.css">
  <script>!(function(){{if(localStorage.getItem("theme")==="dark")document.documentElement.setAttribute("data-theme","dark");}})();</script>
</head>
<body class="slide-deck-body">
{NAV}
  <header class="slide-deck-header">
    <a href="../../lectures.html">← Lectures</a>
    <span>Lecture {n}: {esc(title)}</span>
    <span class="slide-counter">1 / {len(slides)}</span>
  </header>
  <div class="slide-viewport">
{body}
  </div>
  <p class="slide-hint">Arrow keys, Space, or buttons to advance</p>
  <footer class="slide-deck-footer">
    <button type="button" id="prev" aria-label="Previous slide">← Previous</button>
    <button type="button" id="next" aria-label="Next slide">Next →</button>
  </footer>
  <script src="../../js/slides.js"></script>
  <script src="../../js/theme.js"></script>
</body>
</html>
"""


def vibe_html(n, title, goal, zip_name, steps):
    step_blocks = []
    for i, st in enumerate(steps, 1):
        extend = f'\n      <p class="vibe-extend"><strong>Stretch:</strong> {esc(st["extend"])}</p>' if st.get("extend") else ""
        step_blocks.append(f"""    <div class="vibe-step">
      <h2><span class="step-num">Step {i}</span> {esc(st["title"])}</h2>
      <p>{esc(st["desc"])}</p>
      <pre class="prompt">{esc(st["prompt"])}</pre>
      <div class="vibe-check"><strong>Check:</strong> {esc(st["check"])}</div>{extend}
    </div>""")
    steps_html = "\n".join(step_blocks)
    zip_link = f'../../data/lec{ n:02d}/{zip_name}' if zip_name else "#"
    zip_line = f'<p class="vibe-download"><strong>Starter code:</strong> <a href="{zip_link}">{esc(zip_name or "coming soon")}</a></p>' if zip_name else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lecture {n} Vibe Coding — {esc(title)}</title>
  <link rel="stylesheet" href="../../css/style.css">
  <link rel="stylesheet" href="../../css/vibe-session.css">
  <script>!(function(){{if(localStorage.getItem("theme")==="dark")document.documentElement.setAttribute("data-theme","dark");}})();</script>
</head>
<body>
{NAV}
  <main class="vibe-main">
    <div class="vibe-header">
      <h1>Lecture {n}: {esc(title)}</h1>
      <p class="meta">
        <a href="../slides/lec{n:02d}-slides.html">← Slides</a>
        <a href="../../lectures.html">All lectures</a>
        · ~20 minutes in class
      </p>
    </div>
    <div class="vibe-goal"><strong>In-class goal:</strong> {esc(goal)}</div>
    {zip_line}
{steps_html}
  </main>
  <script src="../../js/theme.js"></script>
  <footer class="site-footer"><p>© 2026 Tauhid Zaman</p></footer>
</body>
</html>
"""


# --- LECTURE CONTENT ---
LECTURES = {}

LECTURES[1] = {
    "title": "AI and Vibe Coding",
    "slides": [
        {"class": " title-slide", "html": """        <h1>AI and Vibe Coding</h1>
        <p class="subtitle">MGT 409 · AI Foundations for Managers</p>"""},
        {"html": """        <h1>What is an LLM?</h1>
        <ul>
          <li>A <strong>Large Language Model</strong> predicts the next token (word piece) given everything before it.</li>
          <li>It is trained on huge text corpora—not a database of facts you query.</li>
          <li>At runtime you send a <strong>prompt</strong>; the model returns more tokens.</li>
        </ul>
        <p class="takeaway">Think: very advanced autocomplete with reasoning patterns—not guaranteed truth.</p>"""},
        {"html": """        <h1>One token at a time (inference)</h1>
        <ul>
          <li>Generation is <strong>autoregressive</strong>: each new word depends on all prior words.</li>
          <li>Every new token requires a full forward pass through the model (many layers).</li>
          <li>Longer prompts + longer answers = more compute and cost.</li>
        </ul>
        <p class="takeaway">Managers care: latency and token bills scale with length.</p>"""},
        {"html": """        <h1>Transformers (high level)</h1>
        <p>Modern LLMs are built from <strong>transformer</strong> blocks. Each token gets three internal vectors:</p>
        <table>
          <tr><th>Vector</th><th>Intuition</th></tr>
          <tr><td><strong>Query (Q)</strong></td><td>“What am I looking for from other words?”</td></tr>
          <tr><td><strong>Key (K)</strong></td><td>“What do I advertise as a match?”</td></tr>
          <tr><td><strong>Value (V)</strong></td><td>“What information do I carry?”</td></tr>
        </table>"""},
        {"html": """        <h1>Attention mechanism</h1>
        <ol>
          <li>Compare this token’s <strong>Query</strong> to every token’s <strong>Key</strong> → similarity scores.</li>
          <li>Turn scores into <strong>weights</strong> (positive, sum to 1).</li>
          <li>Build a new representation = weighted sum of all <strong>Values</strong>.</li>
        </ol>
        <p>Words don’t stay isolated—the model <strong>blends context</strong> into each token.</p>"""},
        {"html": """        <h1>Example: “bank” disambiguation</h1>
        <p><em>“We walked along the river bank at sunset.”</em></p>
        <div class="bar-row"><span>river</span><div class="bar" style="width:70%"></div><span>high</span></div>
        <div class="bar-row"><span>sunset</span><div class="bar" style="width:35%"></div></div>
        <div class="bar-row"><span>walked</span><div class="bar" style="width:30%"></div></div>
        <p style="margin-top:1rem"><em>“The bank approved our loan.”</em> → “bank” attends to <strong>loan</strong>, <strong>approved</strong>.</p>
        <p class="takeaway">Same spelling, different meaning—resolved by attention to neighbors.</p>"""},
        {"html": """        <h1>Tiny numeric toy</h1>
        <p>Token <strong>report</strong> asks who to listen to:</p>
        <ul>
          <li>Q(report)·K(Annual) → score 2.0</li>
          <li>Q(report)·K(due) → score 1.0</li>
          <li>Softmax → weights ≈ <strong>73%</strong> Annual, <strong>27%</strong> due</li>
        </ul>
        <p>New value ≈ 0.73×V(Annual) + 0.27×V(due) (+ other tokens).</p>
        <p class="takeaway">Layers stack this operation—syntax early, meaning deeper.</p>"""},
        {"html": """        <h1>What is vibe coding?</h1>
        <ul>
          <li>Describe what you want in natural language to an AI coding assistant (Cursor, etc.).</li>
          <li>You review, run, and fix—<strong>you</strong> stay in charge.</li>
          <li>Document prompts in <code>AI_prompts.md</code> (your words, per task).</li>
        </ul>"""},
        {"html": """        <h1>Course toolchain</h1>
        <ul>
          <li>VS Code / Cursor, Python 3.11+, OpenAI API key in <code>.env</code></li>
          <li>One script = one focused LLM call (Homework 1)</li>
          <li>Agents (loops + tools) start Lecture 4</li>
        </ul>
        <p>See <strong>Instructions</strong> on the course site for setup.</p>"""},
        {"html": """        <h1>Prompt anatomy</h1>
        <ul>
          <li><strong>Role</strong> — who the model is</li>
          <li><strong>Task</strong> — one clear job</li>
          <li><strong>Output format</strong> — JSON schema, bullets, etc.</li>
          <li><strong>Constraints</strong> — don’t invent; cite sources; refuse if unsure</li>
        </ul>"""},
        {"html": """        <h1>Course arc (5 modules)</h1>
        <ol>
          <li>Vibe coding &amp; structured text</li>
          <li>Tools &amp; agents &amp; agentic search</li>
          <li>Multimodal knowledge</li>
          <li>Apps &amp; deployment</li>
          <li>Security, economics &amp; future</li>
        </ol>
        <p>Final project: integrate everything into one <strong>Business AI Co-Pilot</strong>.</p>"""},
        {"class": " section-slide", "html": """        <h1>→ Vibe coding (in class)</h1>
        <p>First API call + project folder setup</p>
        <p><a href="../vibe/lec01-vibe.html">Open vibe coding prompts →</a></p>"""},
        {"html": """        <h1>Homework 1 preview</h1>
        <p>Spoke &amp; Wrench bicycle shop: extract messy PDFs → January income statement.</p>
        <p>Single-step LLM scripts only—<strong>not</strong> agents yet.</p>
        <p><a href="../../hw1/p1.html">Homework 1 details →</a></p>"""},
    ],
    "vibe": {
        "goal": "Set up your project folder and make your first OpenAI API call from Python.",
        "zip": "lec01_starter.zip",
        "steps": [
            {"title": "Create project skeleton", "desc": "Ask your vibe coder to scaffold a minimal Python project.", "prompt": "Create a folder lec01/ with hello_llm.py, requirements.txt (openai, python-dotenv), .env.example (OPENAI_API_KEY=), and README.md with setup steps. Do not add API keys.", "check": "You have lec01/ with the four files; .env is gitignored."},
            {"title": "Load API key safely", "desc": "Wire dotenv and a test call.", "prompt": "In hello_llm.py, load OPENAI_API_KEY from .env using python-dotenv. Add a function ask_llm(prompt) that calls gpt-4o-mini and returns the text. Add if __name__ == main guard that prints ask_llm('Say hello in one sentence.').", "check": "Running python hello_llm.py prints one sentence without errors."},
            {"title": "Start AI_prompts.md", "desc": "Log what you asked the vibe coder.", "prompt": "Create AI_prompts.md with a heading for Lecture 1 and paste summaries of the two prompts you used above in your own words.", "check": "AI_prompts.md exists with Lecture 1 section."},
        ],
    },
}

LECTURES[2] = {
    "title": "Structured Data from Free Text",
    "slides": [
        {"class": " title-slide", "html": """        <h1>Structured Data from Free Text</h1>
        <p class="subtitle">Lecture 2</p>"""},
        {"html": """        <h1>Why structure matters</h1>
        <ul>
          <li>Business runs on spreadsheets, ERPs, and APIs—all need <strong>fields</strong>.</li>
          <li>PDFs, emails, and scans are <strong>unstructured</strong>.</li>
          <li>LLMs excel at mapping messy text → JSON if you specify the schema.</li>
        </ul>"""},
        {"html": """        <h1>JSON as a contract</h1>
        <ul>
          <li>Define field names, types, and required vs optional.</li>
          <li>Validate output (jsonschema or manual checks).</li>
          <li>Missing data → <code>null</code> or <code>fields_not_found</code>—never invent.</li>
        </ul>"""},
        {"html": """        <h1>PDF and text challenges</h1>
        <ul>
          <li>Layout noise: tables split across lines, headers/footers.</li>
          <li>Multi-document reconciliation (bank vs receipt vs card).</li>
          <li>Judgment calls need a human-auditable log.</li>
        </ul>"""},
        {"html": """        <h1>Pipeline pattern</h1>
        <div class="diagram">read PDF → extract (LLM) → validate JSON → reconcile → report
        </div>
        <p>Homework 1 implements this for a real small business.</p>"""},
        {"html": """        <h1>Prompt tips for extraction</h1>
        <ul>
          <li>Paste or attach document text; name the source file in output.</li>
          <li>List every field with an example.</li>
          <li>Repeat: “If not present, use null—do not guess.”</li>
        </ul>"""},
        {"class": " section-slide", "html": """        <h1>→ Vibe coding</h1>
        <p>Extract vendor, date, amount from one receipt PDF</p>
        <p><a href="../vibe/lec02-vibe.html">Open prompts →</a></p>"""},
        {"html": """        <h1>Summary</h1>
        <ul>
          <li>Structure = trust + automation.</li>
          <li>One script, one extraction task (HW1 pattern).</li>
          <li>Next: give the LLM <strong>tools</strong> (Lecture 3).</li>
        </ul>"""},
    ],
    "vibe": {
        "goal": "Extract structured JSON from one receipt PDF using a prompt file.",
        "zip": "lec02_starter.zip",
        "steps": [
            {"title": "Prompt file", "desc": "Create an extraction prompt template.", "prompt": "Create prompts/receipt_extract.md that instructs the model to extract vendor, date, description, amount_usd, category from receipt text and return JSON. Include: do not invent missing fields.", "check": "prompts/receipt_extract.md exists with field list."},
            {"title": "Extraction script", "desc": "Single-purpose script.", "prompt": "Create extract_receipt.py that reads receipt text from a file path argument, loads prompts/receipt_extract.md, calls OpenAI, parses JSON, writes output/receipt.json. Use python-dotenv for API key.", "check": "python extract_receipt.py sample_receipt.txt creates valid JSON."},
            {"title": "Log prompts", "desc": "Add to AI_prompts.md under Lecture 2.", "prompt": "Append Lecture 2 section to AI_prompts.md with summaries of prompts used.", "check": "AI_prompts.md updated."},
        ],
    },
}

# Continue with lectures 3-13 - I'll add compact but complete content

def add_remaining():
    LECTURES[3] = {
        "title": "Tool Use",
        "slides": [
            {"class": " title-slide", "html": "<h1>Tool Use</h1><p class=\"subtitle\">Integrating tools with AI</p>"},
            {"html": "<h1>LLM + tools</h1><ul><li>Models alone cannot browse the web or run your code unless you wire it.</li><li><strong>Tool use</strong> = model chooses to call a function you define.</li><li>Results return to the model for the next step.</li></ul>"},
            {"html": "<h1>Web search tool</h1><ul><li>Fetch fresh facts with URLs for citations.</li><li>Always require source links in output JSON.</li><li>Verify claims—hallucinations still happen.</li></ul>"},
            {"html": "<h1>Function calling</h1><ul><li>Declare tools with name, description, parameters (JSON schema).</li><li>Model returns tool call → your code runs it → feed result back.</li></ul>"},
            {"html": "<h1>MCP (Model Context Protocol)</h1><ul><li>A standard way to expose tools to agents (like USB for capabilities).</li><li>We introduce it here; agents use it in Lecture 4.</li><li>You may use MCP or plain Python functions in homework.</li></ul>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>Competitor web search → JSON table</p><p><a href=\"../vibe/lec03-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Tools turn chat into action. Next lecture: put tools inside a <strong>loop</strong> (agents).</p>"},
        ],
        "vibe": {"goal": "Build a web-search script that returns a competitor table with URLs.", "zip": "lec03_starter.zip", "steps": [
            {"title": "Search function", "desc": "Wrap search API or tool.", "prompt": "Create search_web.py with search_web(query) that returns top 5 results as list of {title, url, snippet}. Use OpenAI responses with web search tool or a search API stub documented in README.", "check": "search_web('office furniture retailers') returns JSON with urls."},
            {"title": "Structured output", "desc": "LLM formats results.", "prompt": "Create research_competitors.py that searches for '3 competitors in [niche]', asks LLM to output JSON table with name, url, one_line_summary. Save output/competitors.json.", "check": "competitors.json has ≥3 rows with urls."},
            {"title": "AI_prompts.md", "desc": "Log Lecture 3 prompts.", "prompt": "Add Lecture 3 section to AI_prompts.md.", "check": "File updated."},
        ]},
    }
    LECTURES[4] = {
        "title": "Agents",
        "slides": [
            {"class": " title-slide", "html": "<h1>Agents</h1><p class=\"subtitle\">Chat + tools in a loop</p>"},
            {"html": "<h1>Script vs agent</h1><ul><li><strong>Script:</strong> one prompt, one answer (HW1).</li><li><strong>Agent:</strong> loop until goal met—observe, decide, act.</li></ul>"},
            {"html": "<h1>The agent loop</h1><div class=\"diagram\">while not done:\n  model decides next action (tool or final answer)\n  run tool if needed\n  append result to conversation\n</div>"},
            {"html": "<h1>When to stop</h1><ul><li>Max steps guardrail.</li><li>Valid JSON schema achieved.</li><li>Model emits FINISH or stop token.</li></ul>"},
            {"html": "<h1>Logging</h1><p>Save traces (tool calls, outputs) for debugging and grading.</p>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>3-step research agent</p><p><a href=\"../vibe/lec04-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Agents chain tools. Homework 2 combines tool use + agent loop.</p>"},
        ],
        "vibe": {"goal": "Build a simple agent that searches, summarizes, and outputs JSON.", "zip": "lec04_starter.zip", "steps": [
            {"title": "Agent skeleton", "desc": "Loop with max 5 steps.", "prompt": "Create agent.py with run_agent(goal) that loops: call OpenAI with tools [search_web, finish]. Parse tool calls, execute, append messages. Stop when finish called or 5 steps.", "check": "Agent completes a simple goal in logs."},
            {"title": "Structured finish", "desc": "Force JSON output.", "prompt": "Add tool finish(summary_json) that validates JSON schema {competitors: [...], executive_summary: string} before stopping.", "check": "Output validates against schema."},
            {"title": "AI_prompts.md", "desc": "Log prompts.", "prompt": "Add Lecture 4 to AI_prompts.md.", "check": "Updated."},
        ]},
    }
    LECTURES[5] = {
        "title": "Agentic Search",
        "slides": [
            {"class": " title-slide", "html": "<h1>Agentic Search</h1><p class=\"subtitle\">Search documents using an agent</p>"},
            {"html": "<h1>Not one-shot RAG</h1><ul><li>Old pattern: embed once, retrieve once, answer.</li><li><strong>Agentic search:</strong> agent may query, read, refine, cite, or refuse.</li></ul>"},
            {"html": "<h1>Cite and refuse</h1><ul><li>Answers must name the source document.</li><li>Trap questions: refuse or escalate—never fabricate policy.</li></ul>"},
            {"html": "<h1>Knowledge base setup</h1><ul><li>Chunk FAQs, policies, product docs.</li><li>Agent chooses search tool over chunks or files.</li></ul>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>FAQ agent with cite + refuse</p><p><a href=\"../vibe/lec05-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Homework 3 Part 1: agentic search on Meridian FAQ docs.</p>"},
        ],
        "vibe": {"goal": "Answer FAQ questions with citations; refuse unknown policies.", "zip": "lec05_starter.zip", "steps": [
            {"title": "KB loader", "desc": "Load markdown/PDF chunks.", "prompt": "Create kb_search.py with search_kb(query) returning top 3 chunks with source filename.", "check": "Returns chunks from sample FAQ folder."},
            {"title": "QA agent", "desc": "Cite sources in answer.", "prompt": "Create faq_agent.py: search_kb → LLM answer with JSON {answer, sources[], refused: bool}. If no relevant chunk, set refused true.", "check": "Trap question returns refused: true."},
            {"title": "AI_prompts.md", "desc": "Log prompts.", "prompt": "Add Lecture 5 section.", "check": "Updated."},
        ]},
    }
    LECTURES[6] = {
        "title": "Image Analysis",
        "slides": [
            {"class": " title-slide", "html": "<h1>Image Analysis</h1><p class=\"subtitle\">Vision models</p>"},
            {"html": "<h1>Vision models</h1><ul><li>Same API pattern: image + prompt → structured JSON.</li><li>Use for receipts, ads, product photos, shelf images.</li></ul>"},
            {"html": "<h1>Embeddings preview</h1><p>Images can also become vectors for search (Lecture 7).</p>"},
            {"html": "<h1>Quality checks</h1><ul><li>Validate required fields.</li><li>Flag low-confidence extractions for human review.</li></ul>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>Extract product fields from a photo</p><p><a href=\"../vibe/lec06-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Homework 3 Part 2: catalog image extraction.</p>"},
        ],
        "vibe": {"goal": "Extract name, price, category from a product image.", "zip": "lec06_starter.zip", "steps": [
            {"title": "Vision prompt", "desc": "Create image extract prompt.", "prompt": "Create prompts/product_image.md for extracting name, price_usd, category, description from product photo. Return JSON only.", "check": "Prompt file ready."},
            {"title": "extract_image.py", "desc": "Call vision API.", "prompt": "Create extract_image.py --image path that base64-encodes image, calls gpt-4o vision, writes output/product.json.", "check": "JSON has required fields for sample chair.jpg."},
            {"title": "AI_prompts.md", "desc": "Log.", "prompt": "Add Lecture 6.", "check": "Updated."},
        ]},
    }
    LECTURES[7] = {
        "title": "Multimodal Search",
        "slides": [
            {"class": " title-slide", "html": "<h1>Multimodal Search</h1><p class=\"subtitle\">Text + image catalog search</p>"},
            {"html": "<h1>Two search modes</h1><ul><li><strong>Text query</strong> over metadata and descriptions.</li><li><strong>Image query</strong> find similar products.</li></ul>"},
            {"html": "<h1>Describe vs embed</h1><ul><li>Describe: vision model captions image then text search (slower).</li><li>Embed: vector similarity (faster at scale).</li></ul>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>Find similar catalog item from image</p><p><a href=\"../vibe/lec07-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Homework 4: multimodal catalog search for Meridian.</p>"},
        ],
        "vibe": {"goal": "Search catalog by text or image query.", "zip": "lec07_starter.zip", "steps": [
            {"title": "Catalog index", "desc": "Load products with embeddings.", "prompt": "Create catalog_index.py that loads products.json, embeds description+metadata with OpenAI embeddings, saves index/catalog_embeddings.json.", "check": "Index file created for ≥5 products."},
            {"title": "Search API", "desc": "Text and image query.", "prompt": "Create catalog_search.py --query text OR --image path returning top 3 products with scores.", "check": "Both modes return ranked results."},
            {"title": "AI_prompts.md", "desc": "Log.", "prompt": "Add Lecture 7.", "check": "Updated."},
        ]},
    }
    LECTURES[8] = {
        "title": "Customer-Facing Agents",
        "slides": [
            {"class": " title-slide", "html": "<h1>Customer-Facing Agents</h1><p class=\"subtitle\">Channels and tone</p>"},
            {"html": "<h1>Same backend, many channels</h1><ul><li>Telegram, Slack, web chat widget.</li><li>Reuse FAQ + catalog modules from prior lectures.</li></ul>"},
            {"html": "<h1>UX for customers</h1><ul><li>Clear tone, escalation to human, refuse gracefully.</li><li>Log conversations for review.</li></ul>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>Wire Telegram or Slack bot stub</p><p><a href=\"../vibe/lec08-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Homework 4: customer bot for Meridian.</p>"},
        ],
        "vibe": {"goal": "Connect faq_agent to a messaging webhook stub.", "zip": "lec08_starter.zip", "steps": [
            {"title": "Bot entrypoint", "desc": "Echo server with agent hook.", "prompt": "Create bot_server.py Flask app POST /message {text} → calls faq_agent → returns JSON response. Include README for ngrok testing.", "check": "curl POST returns agent answer."},
            {"title": "Telegram or Slack", "desc": "Optional webhook adapter.", "prompt": "Add telegram_bot.py OR slack_bot.py that forwards messages to bot_server logic.", "check": "One message round-trip works.", "extend": "Deploy with public URL in HW4."},
            {"title": "AI_prompts.md", "desc": "Log.", "prompt": "Add Lecture 8.", "check": "Updated."},
        ]},
    }
    LECTURES[9] = {
        "title": "Web and Mobile Applications",
        "slides": [
            {"class": " title-slide", "html": "<h1>Web and Mobile Applications</h1><p class=\"subtitle\">UI over your agents</p>"},
            {"html": "<h1>UI as a shell</h1><ul><li>Tabs map to agent modules (extract, search, research).</li><li>Vite + vanilla JS or React—vibe code the layout.</li></ul>"},
            {"html": "<h1>Mobile</h1><p>Responsive web or React Native shell calling same API backend.</p>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>Two-tab Vite app</p><p><a href=\"../vibe/lec09-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Homework 5: Meridian web app with live deploy.</p>"},
        ],
        "vibe": {"goal": "Scaffold a Vite app with two tabs calling your Python APIs.", "zip": "lec09_starter.zip", "steps": [
            {"title": "Vite scaffold", "desc": "Create frontend.", "prompt": "Create app/ with Vite vanilla TS, two tabs FAQ and Catalog. Each tab has input + results div. README with npm run dev.", "check": "npm run dev shows two tabs."},
            {"title": "Wire backend", "desc": "Fetch from Flask/FastAPI.", "prompt": "Add api_server.py routes /faq and /search. Connect frontend fetch calls. Enable CORS.", "check": "Clicking search shows JSON results in UI."},
            {"title": "AI_prompts.md", "desc": "Log.", "prompt": "Add Lecture 9.", "check": "Updated."},
        ]},
    }
    LECTURES[10] = {
        "title": "Application Deployment",
        "slides": [
            {"class": " title-slide", "html": "<h1>Application Deployment</h1><p class=\"subtitle\">Go live safely</p>"},
            {"html": "<h1>Secrets</h1><ul><li>API keys in host env vars—never in git.</li><li>.env locally; dashboard vars in production.</li></ul>"},
            {"html": "<h1>Hosting</h1><ul><li>Static frontend: Vercel, Netlify.</li><li>Python API: Render, Railway, or serverless functions.</li></ul>"},
            {"html": "<h1>Smoke test checklist</h1><ul><li>Homepage loads, one FAQ query, one search, logs clean.</li></ul>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>Deploy and document URL</p><p><a href=\"../vibe/lec10-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Homework 5 requires a public URL.</p>"},
        ],
        "vibe": {"goal": "Deploy frontend and document production URL in README.", "zip": "lec10_starter.zip", "steps": [
            {"title": "Deploy frontend", "desc": "Vercel or similar.", "prompt": "Add vercel.json or deployment section to README with steps to deploy app/ to Vercel. Document required env vars.", "check": "Live HTTPS URL opens app."},
            {"title": "Deploy API", "desc": "Host Python backend.", "prompt": "Add render.yaml or Railway instructions for api_server.py. Set OPENAI_API_KEY in dashboard.", "check": "Production FAQ endpoint responds."},
            {"title": "AI_prompts.md", "desc": "Log.", "prompt": "Add Lecture 10.", "check": "Updated."},
        ]},
    }
    LECTURES[11] = {
        "title": "Security and Guardrails",
        "slides": [
            {"class": " title-slide", "html": "<h1>Security and Guardrails</h1><p class=\"subtitle\">Safe agents</p>"},
            {"html": "<h1>Threat model</h1><ul><li>Prompt injection via user or web content.</li><li>Data leakage (PII in logs or outputs).</li><li>Autonomous actions without approval.</li></ul>"},
            {"html": "<h1>Guardrails</h1><ul><li>Refuse off-topic or harmful requests.</li><li>Redact PII before logging.</li><li>Human approval for high-stakes actions.</li></ul>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>Add refusal + PII redaction</p><p><a href=\"../vibe/lec11-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Homework 6 + final project require demonstrated guardrails.</p>"},
        ],
        "vibe": {"goal": "Add input filter and PII redaction to your agent pipeline.", "zip": "lec11_starter.zip", "steps": [
            {"title": "Injection filter", "desc": "Block obvious jailbreak patterns.", "prompt": "Create guardrails.py with check_input(text) returning {allowed, reason}. Block 'ignore previous instructions' patterns. Integrate before agent calls.", "check": "Malicious test string is blocked."},
            {"title": "PII redaction", "desc": "Redact emails/phones in logs.", "prompt": "Add redact_pii(text) and apply to all log writes.", "check": "Log file shows [EMAIL] not real addresses."},
            {"title": "AI_prompts.md", "desc": "Log.", "prompt": "Add Lecture 11.", "check": "Updated."},
        ]},
    }
    LECTURES[12] = {
        "title": "Tokenomics",
        "slides": [
            {"class": " title-slide", "html": "<h1>Tokenomics</h1><p class=\"subtitle\">Cost and scale</p>"},
            {"html": "<h1>Tokens</h1><ul><li>Input + output tokens billed per call.</li><li>Bigger models cost more; longer context costs more.</li></ul>"},
            {"html": "<h1>Model choice</h1><ul><li>mini/nano for extraction; flagship for hard reasoning.</li><li>Measure before optimizing.</li></ul>"},
            {"html": "<h1>Scale scenarios</h1><p>Cost per 100 runs × daily volume = operating budget.</p>"},
            {"class": " section-slide", "html": "<h1>→ Vibe coding</h1><p>Log tokens and cost per request</p><p><a href=\"../vibe/lec12-vibe.html\">Open prompts →</a></p>"},
            {"html": "<h1>Summary</h1><p>Homework 6: economics report. Final project memo includes cost per 100 runs.</p>"},
        ],
        "vibe": {"goal": "Add token and USD cost logging to each agent call.", "zip": "lec12_starter.zip", "steps": [
            {"title": "Usage logger", "desc": "Capture usage from API response.", "prompt": "Create cost_log.py with log_usage(model, input_tokens, output_tokens) appending to output/usage.csv with estimated USD using published rates.", "check": "CSV grows after each call."},
            {"title": "Integrate", "desc": "Wrap ask_llm / agent calls.", "prompt": "Modify agent and LLM wrappers to call log_usage after every API response.", "check": "One end-to-end flow produces usage row."},
            {"title": "AI_prompts.md", "desc": "Log.", "prompt": "Add Lecture 12.", "check": "Updated."},
        ]},
    }
    LECTURES[13] = {
        "title": "Future Directions",
        "slides": [
            {"class": " title-slide", "html": "<h1>Future Directions</h1><p class=\"subtitle\">What's next</p>"},
            {"html": "<h1>Evals and benchmarks</h1><ul><li>Your final project is graded with automated tests + hidden suite.</li><li>Public practice suite released before submit.</li></ul>"},
            {"html": "<h1>Build vs buy</h1><ul><li>When to use Copilot, vendor SaaS, or custom agents.</li></ul>"},
            {"html": "<h1>Horizon</h1><ul><li>Multimodal agents, longer context, on-device models, regulation.</li></ul>"},
            {"html": "<h1>Final project kickoff</h1><p><strong>Business AI Co-Pilot</strong> — pick your business, pass capability benchmarks, deploy, memo on cost and security.</p><p><a href=\"../../project_requirements.html\">Final project requirements →</a></p>"},
            {"html": "<h1>Thank you</h1><p>Questions? Continue integrating your co-pilot for finals week.</p>"},
        ],
        "vibe": {"goal": "Plan your final project modules and run the public benchmark checklist.", "zip": None, "steps": [
            {"title": "Choose business", "desc": "Pick domain for co-pilot.", "prompt": "Write final_project/README.md section Business: 1 paragraph on who uses your co-pilot and what decisions it supports.", "check": "README has Business section."},
            {"title": "Module map", "desc": "List required capabilities.", "prompt": "Add Module map table: PDF extract, image extract, agentic search, web research, decision agent, router, guardrails.", "check": "All buckets listed with file names."},
            {"title": "Benchmark dry run", "desc": "Self-test against public suite when available.", "prompt": "Document in README how you will run python run_benchmarks.py --suite public (stub OK until instructor publishes).", "check": "README has Testing section."},
        ]},
    }

add_remaining()


def main():
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)
    VIBE_DIR.mkdir(parents=True, exist_ok=True)
    for n, data in sorted(LECTURES.items()):
        if n == 1:
            print("Skip lec01 (hand-maintained deep deck)")
            continue
        path = SLIDES_DIR / f"lec{n:02d}-slides.html"
        path.write_text(slide_html(n, data["title"], data["slides"]), encoding="utf-8")
        v = data["vibe"]
        vpath = VIBE_DIR / f"lec{n:02d}-vibe.html"
        vpath.write_text(vibe_html(n, data["title"], v["goal"], v.get("zip"), v["steps"]), encoding="utf-8")
        print("Wrote", path.name, vpath.name)


if __name__ == "__main__":
    main()
