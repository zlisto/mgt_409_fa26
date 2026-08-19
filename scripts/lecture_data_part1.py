"""MBA-depth slide and vibe content for Lectures 2–7."""

DECK = {}

# Canonical student HTML: lectures/slides/lec02-slides.html + vibe/lec02-vibe.html
# (40 min lecture + 40 min vibe, Aug 2026). Do not rebuild over those files.
DECK[2] = {
    "title": "Structured Data from Free Text",
    "slides": [
        {"class": "title-slide", "html": """        <h1>Structured Data from Free Text</h1>
        <p class="subtitle">MGT 409 · Lecture 2 · Tauhid Zaman</p>
        <p class="subtitle">PDFs do not close the books. JSON might.</p>"""},
        {"html": """        <p class="instructor-banner">Instructor outline — remove before class.</p>
        <h1>40 minutes, then vibe</h1>
        <table class="pace-table">
          <tr><th>Clock</th><th>Beat</th></tr>
          <tr><td>0–4</td><td>Cold open: last week an API call; this week fields a spreadsheet can eat</td></tr>
          <tr><td>4–10</td><td>Fluency is not a receipt. ERP / audit / P&amp;L want fields. Gartner pile + IDP TAM</td></tr>
          <tr><td>10–16</td><td>Homework 1 is a pipeline, not a chatbot — walk the diagram</td></tr>
          <tr><td>16–22</td><td>JSON is the contract. Two files named “prompts.” Do not mix them</td></tr>
          <tr><td>22–32</td><td>Spine: LLM extract → LLM recon → Python P&amp;L. One purchase, three docs</td></tr>
          <tr><td>32–37</td><td>Schema ≠ truth. Validator. Prompt anatomy for the lab</td></tr>
          <tr><td>37–40</td><td>Handoff: 40-min vibe (P2 miniature) + HW1 map. Do not solve the zip</td></tr>
        </table>
        <p class="takeaway">Then 40 minutes of vibe. If you are still on news at minute 18, skip to the pipeline.</p>"""},
        {"html": """        <h1>Last week you called an API. This week it has a job.</h1>
        <ul>
          <li>Lecture 1: one prompt, one reply, tokens cost money.</li>
          <li>Lecture 2: force the reply into <strong>fields a spreadsheet can eat</strong>.</li>
          <li>Homework 1: Spoke &amp; Wrench’s January shoebox → an income statement.</li>
        </ul>
        <div class="pill-row">
          <span class="pill pill-hot">receipts</span>
          <span class="pill pill-teal">bank PDF</span>
          <span class="pill pill-gold">credit card</span>
          <span class="pill pill-grape">emails / notes</span>
        </div>
        <p class="takeaway">Unstructured in. Typed rows out.</p>"""},
        {"html": """        <h1>The intern who never says “I don’t know”</h1>
        <div class="stat-grid">
          <div class="stat-box">
            <div class="num">ERP</div>
            <div class="label">Wants vendor, date, amount, account — not a paragraph</div>
          </div>
          <div class="stat-box">
            <div class="num">Audit</div>
            <div class="label">Wants <code>source_file</code> and a number a human can re-check</div>
          </div>
          <div class="stat-box">
            <div class="num">P&amp;L</div>
            <div class="label">Wants one booked amount after conflicts are resolved</div>
          </div>
        </div>
        <ul>
          <li>Frontier models are <strong>fluent</strong>. Fluency is not a receipt.</li>
          <li>Homework 1: missing fields go in <code>fields_not_found</code>. <strong>Do not invent values.</strong></li>
        </ul>
        <p class="takeaway">Fast intern, not a creative bookkeeper. If it is not on the page, it is <code>null</code>.</p>"""},
        {"html": """        <h1>The pile is still 70–90% unstructured</h1>
        <img class="news-card" src="../images/lec02/news-gartner-unstructured.svg" alt="News card: Gartner 2026, 70 to 90 percent of enterprise data is unstructured">
        <p class="source-note">Gartner MQ for Document Management 2026: 70–90% of enterprise data is unstructured. Fortune Business Insights: IDP $10.57B (2025) → <strong>$14.16B (2026)</strong>, $91B by 2034 — order of magnitude, not a precise TAM. <a href="https://www.gartner.com/reviews/market/document-management">Gartner</a> · <a href="https://www.fortunebusinessinsights.com/intelligent-document-processing-market-108590">Fortune Business Insights</a></p>
        <p class="joke">Homework 1 is a $14 billion industry wearing a bicycle-shop costume.</p>"""},
        {"html": """        <h1>Homework 1 is a pipeline, not a chatbot</h1>
        <svg class="flow-svg" viewBox="0 0 860 210" aria-label="Homework 1 document pipeline">
          <defs>
            <marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path class="arrow" d="M0,0 L6,3 L0,6 Z"/></marker>
          </defs>
          <rect class="box-light" x="8" y="70" width="118" height="70" rx="8"/>
          <text x="67" y="100" text-anchor="middle" font-size="13" font-weight="700">PDF pack</text>
          <text x="67" y="118" text-anchor="middle" font-size="11">receipts / bank / card</text>
          <line x1="126" y1="105" x2="150" y2="105" stroke="#286dc0" stroke-width="3" marker-end="url(#a2)"/>
          <rect class="box-dark" x="150" y="18" width="150" height="54" rx="8"/>
          <text class="on-dark" x="225" y="40" text-anchor="middle" font-size="13">read_receipts</text>
          <text class="on-dark" x="225" y="58" text-anchor="middle" font-size="11">LLM · P2</text>
          <rect class="box-dark" x="150" y="80" width="150" height="54" rx="8"/>
          <text class="on-dark" x="225" y="102" text-anchor="middle" font-size="13">read_bank</text>
          <text class="on-dark" x="225" y="120" text-anchor="middle" font-size="11">LLM · P3</text>
          <rect class="box-dark" x="150" y="142" width="150" height="54" rx="8"/>
          <text class="on-dark" x="225" y="164" text-anchor="middle" font-size="13">read_card</text>
          <text class="on-dark" x="225" y="182" text-anchor="middle" font-size="11">LLM · P4</text>
          <line x1="300" y1="105" x2="330" y2="105" stroke="#286dc0" stroke-width="3" marker-end="url(#a2)"/>
          <rect class="box-dark" x="330" y="70" width="150" height="70" rx="8"/>
          <text class="on-dark" x="405" y="100" text-anchor="middle" font-size="13">reconcile.py</text>
          <text class="on-dark" x="405" y="118" text-anchor="middle" font-size="11">LLM · P5</text>
          <line x1="480" y1="105" x2="508" y2="105" stroke="#286dc0" stroke-width="3" marker-end="url(#a2)"/>
          <rect class="box-light" x="508" y="70" width="150" height="70" rx="8"/>
          <text x="583" y="96" text-anchor="middle" font-size="13" font-weight="700">income_statement</text>
          <text x="583" y="116" text-anchor="middle" font-size="11">Python math · P7</text>
          <line x1="658" y1="105" x2="686" y2="105" stroke="#286dc0" stroke-width="3" marker-end="url(#a2)"/>
          <rect class="box-light" x="686" y="70" width="160" height="70" rx="8"/>
          <text x="766" y="96" text-anchor="middle" font-size="13" font-weight="700">HTML report</text>
          <text x="766" y="116" text-anchor="middle" font-size="11">P8 + pipeline P9</text>
        </svg>
        <p>Dark boxes call the LLM. Light boxes are your code. One script per problem — testable and gradable.</p>"""},
        {"html": """        <h1>JSON is the contract</h1>
        <ul>
          <li>Name every field. Type every field. Enums beat vibes: <code>business</code> | <code>personal</code>.</li>
          <li>Missing → <code>null</code> + <code>fields_not_found</code>. Never a creative <code>$0.00</code>.</li>
          <li>If two PDFs disagree, a recon-log row — not a silent average.</li>
        </ul>
        <div class="diagram">{
  "vendor": "Park Tool",
  "date": "2026-01-12",
  "amount_usd": 88.70,
  "category": "tools_equipment",
  "source_file": "receipt_park_tool.pdf",
  "fields_not_found": []
}</div>
        <p class="takeaway">A schema that asks for unobservable fields is a hallucination machine.</p>"""},
        {"html": """        <h1>Two files both named “prompts.” Do not mix them.</h1>
        <div class="two-col">
          <div class="compare-box">
            <h3><code>prompts/*.md</code></h3>
            <p>Runtime contracts your <strong>scripts</strong> load. HW1 wants <code>receipts_extract.md</code>, <code>bank_extract.md</code>, <code>card_extract.md</code>, <code>reconcile.md</code>.</p>
          </div>
          <div class="compare-box">
            <h3><code>AI_prompts.md</code></h3>
            <p>The log of what <strong>you typed to Codex/Cursor</strong>, in your own words, problem by problem. Graders read this. Do not paste the assignment URL.</p>
          </div>
        </div>
        <p class="takeaway">One file the script reads. One file the grader reads. Both required.</p>"""},
        {"html": """        <h1>Who does which job?</h1>
        <div class="split-llm">
          <div class="box-extract">
            <h3>LLM · extract</h3>
            <p>Messy PDF text → typed rows. Layout, vendor names, “is this a debit?” Language understanding. P2–P4.</p>
          </div>
          <div class="box-judge">
            <h3>LLM · reconcile</h3>
            <p>Same purchase on a receipt <em>and</em> a card. Mixed deposits. Emails that explain a mismatch. Written <code>resolution</code>. P5.</p>
          </div>
          <div class="box-math">
            <h3>Python · roll up</h3>
            <p>Income statement math from the recon log. No LLM. If you hardcode totals, you failed the assignment. P7.</p>
          </div>
        </div>
        <p class="takeaway">Extract with the LLM. Reconcile with the LLM. Add with Python.</p>"""},
        {"html": """        <h1>One purchase, three documents</h1>
        <svg class="flow-svg" viewBox="0 0 860 150" aria-label="Same purchase appearing in three sources">
          <rect class="box-light" x="20" y="40" width="180" height="70" rx="8"/>
          <text x="110" y="70" text-anchor="middle" font-size="14" font-weight="700">Receipt PDF</text>
          <text x="110" y="92" text-anchor="middle" font-size="13">Park Tool  $88.70</text>
          <rect class="box-light" x="250" y="40" width="180" height="70" rx="8"/>
          <text x="340" y="70" text-anchor="middle" font-size="14" font-weight="700">Card statement</text>
          <text x="340" y="92" text-anchor="middle" font-size="13">PARKTOOL  $88.70</text>
          <rect class="box-light" x="480" y="40" width="180" height="70" rx="8"/>
          <text x="570" y="70" text-anchor="middle" font-size="14" font-weight="700">Bank line</text>
          <text x="570" y="92" text-anchor="middle" font-size="13">card payment?</text>
          <rect class="box-dark" x="700" y="40" width="140" height="70" rx="8"/>
          <text class="on-dark" x="770" y="70" text-anchor="middle" font-size="14">Book once</text>
          <text class="on-dark" x="770" y="92" text-anchor="middle" font-size="12">or exclude</text>
        </svg>
        <ul>
          <li>Sum all three and you triple-count. P5 log row = <strong>one reconciled amount</strong>.</li>
          <li>Owner’s card + shop checking: <code>business</code> vs <code>personal</code> is not a vibe. Show what you excluded.</li>
          <li>P6: three calls you were least sure about. At least one <code>confidence: low</code>.</li>
        </ul>"""},
        {"html": """        <h1>Schema ≠ truth. Your Python is the adult.</h1>
        <img class="news-card" src="../images/lec02/news-structured-outputs.svg" alt="News card: Analytics Insight 17 Aug 2026 on OpenAI Structured Outputs">
        <div class="two-col">
          <div class="compare-box">
            <h3>Model</h3>
            <p>Reads messy layout. Invents enums. Swaps 8 and 3. Writes a novel inside a JSON string.</p>
          </div>
          <div class="compare-box">
            <h3>Your Python</h3>
            <p>Required keys exist. <code>amount_usd</code> is a number ≥ 0. Date looks like ISO. Category is in the allow-list.</p>
          </div>
        </div>
        <p class="source-note">Analytics Insight, 17 Aug 2026: “Reliable structure does not mean correct facts.” <a href="https://www.analyticsinsight.net/amp/story/openai/openai-structured-outputs-how-to-generate-reliable-json-responses">Analytics Insight</a> · <a href="https://developers.openai.com/api/docs/guides/structured-outputs">OpenAI Structured Outputs</a></p>
        <p class="takeaway">Constrained decoding will not save you from a hallucinated amount. Fail → retry or park it. Never silently “fix” dollars.</p>"""},
        {"html": """        <h1>Extraction prompt anatomy</h1>
        <ol>
          <li><strong>Role:</strong> AP clerk for a New Haven bike shop — not “helpful assistant.”</li>
          <li><strong>Input:</strong> document text + <code>source_file</code> name.</li>
          <li><strong>Schema:</strong> every field, type, example, enum.</li>
          <li><strong>Null policy:</strong> if it is not on the page, <code>null</code> + list the field.</li>
          <li><strong>Output:</strong> JSON only. No markdown fences. No “sure, here you go.”</li>
        </ol>
        <p class="takeaway">That file lives in <code>prompts/</code>. The chat you used to write the script lives in <code>AI_prompts.md</code>.</p>"""},
        {"class": "section-slide", "html": """        <h1>→ Vibe coding (~40 min)</h1>
        <p>One fake receipt → JSON. Prompt file. Validator. Then a miniature recon + Python total.</p>
        <p>This is a <strong>miniature of HW1 Problems 2 / 5 / 7</strong> — not the Spoke &amp; Wrench zip.</p>
        <p><a href="../vibe/lec02-vibe.html">Open the in-class prompts →</a></p>"""},
        {"html": """        <h1>Homework 1 map (do not solve it from this slide)</h1>
        <ul>
          <li><strong>P1</strong> log · <strong>P2–P4</strong> extract receipts / bank / card · <strong>P5</strong> LLM recon log</li>
          <li><strong>P6</strong> three judgment calls (one must be low confidence) · <strong>P7</strong> Python P&amp;L</li>
          <li><strong>P8</strong> HTML for humans · <strong>P9</strong> pipeline diagram · <strong>P10</strong> <code>hw1.zip</code></li>
        </ul>
        <p>Work <strong>one problem at a time</strong>. Screenshot the card. Do not paste the assignment URL and ask for the complete zip.</p>
        <p><a href="../../hw1/p1.html">Homework 1, Problem 1 →</a> · data: <a href="../../data/hw1/hw1_spoke_and_wrench.zip">hw1_spoke_and_wrench.zip</a></p>"""},
        {"html": """        <h1>What to remember</h1>
        <ul>
          <li>Business runs on fields. LLMs map messy text → JSON <em>if</em> the contract is strict.</li>
          <li>Schema guarantees shape. Code guarantees the number is sane. You guarantee the policy.</li>
          <li>Extract with the LLM. Reconcile conflicts with the LLM. Add with Python.</li>
        </ul>
        <p class="takeaway">Next lecture: give the model <strong>tools</strong> — search, APIs — so it can leave the PDF.</p>"""},
    ],
    "vibe": {
        "goal": "Leave with a one-receipt extractor (prompt file + JSON + validator), a one-row recon decision, and a Python total. This is a miniature of Homework 1 Problems 2 / 5 / 7 — not the Spoke & Wrench pack.",
        "zip": None,
        "steps": [
            {
                "title": "Scaffold (0–5 min)",
                "desc": "Same hygiene as Lecture 1. The homework zip layout comes later; today is one folder.",
                "prompt": "Create a folder lec02/ with:\n- extract_receipt.py (empty for now)\n- prompts/receipt_extract.md (placeholder)\n- prompts/reconcile.md (placeholder)\n- sample_data/receipt_class.txt\n- output/\n- requirements.txt (openai, python-dotenv)\n- .env.example with OPENAI_API_KEY=\n- .gitignore ignoring .env, __pycache__, and output/*.json\n- README with venv + pip + copy .env.example\nDo not put a real API key in any file.",
                "check": "Folder exists; .gitignore lists .env; no key in git-tracked files.",
            },
            {
                "title": "Write a messy receipt (5–10 min)",
                "desc": "Do not copy Homework 1 PDFs. Invent a classroom receipt so the schema is the point.",
                "prompt": "In sample_data/receipt_class.txt write a short fake bike-shop receipt as plain text. Include: store name, a date in January 2026, two line items, a total in dollars, and a note that tax is not shown as its own line. Leave the payment method blank so one field is actually missing.",
                "check": "File is text, not a PDF. You can see a total and at least one missing fact.",
            },
            {
                "title": "The prompt is the contract (10–16 min)",
                "desc": "This file is what extract_receipt.py will load — the homework’s prompts/*.md pattern. It is not AI_prompts.md.",
                "prompt": "Replace prompts/receipt_extract.md with instructions for an accounts-payable clerk.\n\nExtract JSON with keys:\nsource_file (string), vendor (string), date (YYYY-MM-DD), description (string), amount_usd (number), category (one of parts, labor, tools, other), payment_method (string or null), fields_not_found (array of strings).\n\nRules:\n- Return JSON only. No markdown fences.\n- If a field is not in the text, use null and add the key name to fields_not_found.\n- Never invent amounts or vendors.\n- If category is unclear, use other and list category in fields_not_found.",
                "check": "Prompt names every field, states types, and has “do not invent” language.",
            },
            {
                "title": "One script, one LLM call, one JSON file (16–25 min)",
                "desc": "Homework 1 will loop over many PDFs. Today: one text file. Stay on the course model (often a mini-class via Portkey).",
                "prompt": "Write extract_receipt.py that:\n1. Takes --text-file and --out (default output/receipt.json)\n2. Loads prompts/receipt_extract.md as the system prompt\n3. Sends the file contents plus the filename as the user message\n4. Calls the OpenAI API with response_format json_object (model: same mini-class as Lecture 1 unless the course instructions say otherwise)\n5. Parses JSON\n6. Writes the object to --out\n7. Prints token usage\nUse python-dotenv for OPENAI_API_KEY. Clear error if the key is missing.",
                "check": "python extract_receipt.py --text-file sample_data/receipt_class.txt writes valid JSON with the keys from Step 3.",
            },
            {
                "title": "Validator before you trust it (25–32 min)",
                "desc": "Structured output can still be a fluent lie. Catch it in code.",
                "prompt": "Add validate_receipt(data) and call it before writing the file.\n\nChecks:\n- required keys present\n- amount_usd is a number >= 0, or null\n- if amount_usd is null, fields_not_found includes \"amount_usd\"\n- date matches YYYY-MM-DD when not null\n- category is in {parts, labor, tools, other}\nOn failure raise ValueError with a readable message. Do not silently coerce bad amounts.",
                "check": "Temporarily break a field in a test dict; the script refuses to write.",
            },
            {
                "title": "Mini recon + Python total (32–37 min)",
                "desc": "Homework 1: LLM books once (P5), Python adds (P7). Do not sum the receipt and the card. Invent a second source — do not use the HW1 zip.",
                "prompt": "1. Write sample_data/card_line.json by hand: same amount_usd as your receipt, vendor mangled (e.g. PARKTOOL), source_file \"card_jan.txt\", category other.\n2. Replace prompts/reconcile.md: given two JSON objects, decide if they are the same purchase. Return JSON only: booked_amount_usd (number), same_purchase (boolean), resolution (one sentence), fields_not_found (array). Do not average. If same, book once.\n3. Write reconcile_class.py: load output/receipt.json and sample_data/card_line.json, call the LLM with reconcile.md, write output/recon.json, print the JSON.\n4. Write pnl_class.py: load output/recon.json and print booked_amount_usd. No LLM. Do not add receipt amount + card amount.",
                "check": "recon.json has one booked amount. pnl_class.py prints that number, not a double count.",
            },
            {
                "title": "Log the vibe-coder chat (37–40 min)",
                "desc": "Homework 1 Problem 1 wants this habit from day one. Your words, not a paste of this page.",
                "prompt": "Create or append AI_prompts.md with a Lecture 2 section. In your own words, bullet the prompts you actually typed for scaffold, receipt text, extraction contract, script, validator, and (if you got there) recon + Python total. One sentence on what the first attempt got wrong if you had to retry.",
                "check": "File exists; bullets are paraphrases, not a copy-paste of this vibe page.",
                "extend": "Add --input-dir to extract every .txt in a folder. Homework 1 will need PDFs (pdfplumber / PyPDF2) and three different schemas — save that fight for the assignment, one problem at a time.",
            },
        ],
    },
}

# Lecture 3 student HTML is hand-authored (40 min lecture + 40 min vibe). Do not rebuild over lec03-slides.html / lec03-vibe.html.
DECK[3] = {
    "title": "Tool Use",
    "slides": [
        {"class": " title-slide", "html": """        <h1>Tool Use</h1>
        <p class="subtitle">MGT 409 · Lecture 3 · Tauhid Zaman</p>
        <p class="subtitle">The model can <em>request</em> a function. Your code decides whether it runs.</p>"""},
        {"html": """        <p class="instructor-banner">Instructor outline — remove before class.</p>
        <h1>40-minute lecture flow</h1>
        <table class="outline-table">
          <tr><th>Clock</th><th>Beat</th><th>Say this</th></tr>
          <tr><td>0:00–3:00</td><td>Fluent ≠ live</td><td>Chat has a cutoff. No CRM, no this-morning web unless you expose a function.</td></tr>
          <tr><td>3:00–10:00</td><td>Handshake</td><td>Function calling: the model writes JSON. Your Python executes, logs, and caps.</td></tr>
          <tr><td>10:00–18:00</td><td>HW2 wrench</td><td>HW2 P3 is live search. ICP → queries → hits with real URLs. Today = search only.</td></tr>
          <tr><td>18:00–26:00</td><td>Contract + schema</td><td>Name, description, parameters, truncated returns. Evidence in, JSON out.</td></tr>
          <tr><td>26:00–33:00</td><td>Cost + permissions</td><td>Snippets are a second invoice. Read-only search. AISI: models misuse tools that can act.</td></tr>
          <tr><td>33:00–38:00</td><td>Grade a tool</td><td>Click the URL. Trace the query to the ICP. Empty hits → empty list.</td></tr>
          <tr><td>38:00–40:00</td><td>Handoff</td><td>Petal Depot vibe (40 min). Skip MCP and agent loops.</td></tr>
        </table>"""},
        {"html": """        <h1>A chat-only model has no live access</h1>
        <ul>
          <li>Fluent, not on this morning’s web. Knowledge ends at a training cutoff.</li>
          <li>Cannot query a CRM or open FiftyFlowers.com unless <strong>you</strong> expose a function.</li>
        </ul>
        <p class="takeaway">Tools turn language into actions you can log, cap, and audit.</p>"""},
        {"html": """        <h1>What “tool use” actually is</h1>
        <p><strong>Function calling:</strong> you declare functions. The model returns JSON that says “please run this.” <em>Your code</em> runs it.</p>
        <p class="takeaway">The model never uses the internet. It writes a request. You are the execution layer.</p>"""},
        {"html": """        <h1>The handshake (you own the middle)</h1>
        <p>User ask → LLM + tool definitions → tool-call JSON → your Python (auth, logs, caps) → result back to the LLM.</p>"""},
        {"html": """        <h1>Web search is the Homework 2 tool</h1>
        <p><a href="https://developers.openai.com/api/docs/guides/tools-web-search" target="_blank" rel="noopener">Responses API <code>web_search</code></a>. HW2 Problem 3: ICP → ≥5 queries → real search API → <code>title</code>, <code>url</code>, <code>snippet</code>. Do not invent URLs.</p>
        <p class="takeaway">If the tool did not return an HTTPS link, it is not a lead. Graders click links.</p>"""},
        {"html": """        <h1>FiftyFlowers: one pipeline, many tools</h1>
        <p>HW2 is an outreach system. Today we only build the search step. Volume buyers, not one-off retail. Do <strong>not</strong> send emails.</p>
        <p>ICP from their site → search_web → investigate (cite pages) → score ICP → draft emails → HTML report.</p>"""},
        {"html": """        <h1>Design the tool like a contract</h1>
        <table>
          <tr><th>Field</th><th>Do this</th><th>If you don’t</th></tr>
          <tr><td><code>name</code></td><td><code>search_web</code></td><td>The model invents a name you never implemented</td></tr>
          <tr><td><code>description</code></td><td>When to use vs other tools</td><td>It searches when it should read JSON</td></tr>
          <tr><td><code>parameters</code></td><td>JSON Schema, required fields</td><td>Garbage args, surprise spend</td></tr>
          <tr><td>return value</td><td>Hits + URLs, truncated</td><td>Raw HTML dumped into tokens</td></tr>
        </table>"""},
        {"html": """        <h1>After the tool: still a schema</h1>
        <div class="diagram">{
  "queries": ["austin wedding planners wholesale flowers", "..."],
  "results": [
    {"query": "...", "title": "...", "url": "https://...", "snippet": "..."}
  ]
}</div>
        <p class="takeaway">Separate gathering (tools) from judging (later scripts).</p>"""},
        {"html": """        <h1>Tools add a second invoice</h1>
        <ul>
          <li>McKinsey: 88% of orgs use AI; ≤10% scale an agent in any one function.</li>
          <li>Round-trips stuff snippets into the prompt — truncate in code.</li>
          <li>Five queries is homework. Five hundred unsupervised queries is a budget problem.</li>
        </ul>"""},
        {"html": """        <h1>Tools that can act need a sandbox</h1>
        <p><a href="https://www.csoonline.com/article/4205612/openai-anthropic-ai-agents-resorted-to-deception-in-new-cybersecurity-incidents.html" target="_blank" rel="noopener">CSO / AISI, week of 5 Aug 2026</a>: GPT-5.6 Sol and Mythos 5 took unauthorized actions in cyber tests.</p>
        <p class="takeaway">HW2 gets read-only search. No send_email. Humans hit send.</p>"""},
        {"html": """        <h1>When not to add a tool — then how to grade one</h1>
        <ul>
          <li>Skip: static extraction, data already in SQL, &lt;2s SLA, legal no-web.</li>
          <li>Grade: working URL on every fact; queries that match the ICP; abstain on empty hits.</li>
        </ul>"""},
        {"class": " section-slide", "html": """        <h1>→ Vibe coding (40 min)</h1>
        <p>Build <code>search_web</code>. Make the model propose queries. Save real URLs. Then let the model request the tool.</p>
        <p><a href="../vibe/lec03-vibe.html">Open vibe coding prompts →</a></p>"""},
        {"html": """        <h1>Take it home</h1>
        <ul>
          <li>Tools = bounded functions the model may <strong>request</strong>. You execute, log, and cap.</li>
          <li>HW2 lives or dies on <strong>sourced web evidence</strong>.</li>
        </ul>
        <p class="takeaway">Next: put today’s tool inside a <strong>loop</strong>. Still no send-email button.</p>"""},
    ],
    "vibe": {
        "goal": "40 min: ship search_web, invent queries from a tiny ICP, save search_results.json, then a function-calling variant. Homework 2 search wrench — not FiftyFlowers answers, not email, not the agent loop.",
        "zip": None,
        "steps": [
            {
                "title": "Scaffold lec03 (0:00–6:00)",
                "desc": "Separate the search function from the invent-queries script. Secrets stay in .env.",
                "prompt": "Create a folder lec03/ with: search_web.py, run_search.py, prompts/search_queries.md, fixtures/icp.json (tiny fake ICP for Petal Depot, a bulk flower wholesaler targeting wedding planners and floral studios; disqualify one-off retail brides), fixtures/search_results.stub.json (5 fake but well-formed hits with https URLs), output/, requirements.txt (openai, python-dotenv), .env.example with OPENAI_API_KEY=, .gitignore ignoring .env and output/*, README explaining live OpenAI Responses web_search vs stub if --offline. No real API keys.",
                "check": "Folder exists; README explains live search vs stub; no secrets in tracked files.",
            },
            {
                "title": "Implement search_web(query) (6:00–14:00)",
                "desc": "The tool returns evidence, not a vibe paragraph. Every hit needs a URL.",
                "prompt": "In search_web.py define search_web(query: str, max_results: int = 5) -> list[dict] with keys title, url, snippet. Prefer OpenAI Responses API tools=[{type: web_search}] when OPENAI_API_KEY is set. If --offline or no key, filter fixtures/search_results.stub.json by query substring. Drop hits missing https URLs. Truncate snippets to 280 chars in Python. CLI: python search_web.py \"austin wedding planner\".",
                "check": "CLI prints <=5 objects; first object has https url. Offline mode still returns stub URLs.",
            },
            {
                "title": "Prompt: invent search queries from an ICP (14:00–20:00)",
                "desc": "Homework 2 will have the model propose >=5 queries from icp.json. Practice that contract now.",
                "prompt": "In prompts/search_queries.md: input ICP JSON; output JSON only {queries: [string,...]} with at least 5 distinct web search strings. Queries should find BUSINESS customers (planners, studios, venues), not buy-roses-cheap. Include city in some queries. Do not name invented companies. No personal social-media hunting language.",
                "check": "Prompt file states JSON shape, >=5 rule, and business customers not retail shoppers.",
            },
            {
                "title": "run_search.py — queries then tool (20:00–30:00)",
                "desc": "Still a script, not an agent loop. LLM queries, then your code searches each one. HW2 P3 shape.",
                "prompt": "Create run_search.py that loads fixtures/icp.json, calls gpt-4o-mini with prompts/search_queries.md + ICP (json_object), requires len(queries)>=5, calls search_web for each, writes output/search_results.json as {queries, results:[{query,title,url,snippet}]}. Print token usage. CLI: python run_search.py --icp fixtures/icp.json --out-dir output. Refuse results that lack urls. Empty query -> continue.",
                "check": "File exists; >=5 queries; every result row has query + url.",
            },
            {
                "title": "Function-calling variant (30:00–37:00)",
                "desc": "Same destination, tool-native path: the model requests search_web. Max turns are a cap, not an agent loop.",
                "prompt": "Add research_with_tools.py that registers search_web as an OpenAI function tool, lets the model call it up to 3 times from the Petal Depot ICP, max 4 model turns, writes output/tool_trace.json and output/search_results.json. Warn if it tries any other tool name.",
                "check": "Logs show at least one search_web tool call; final JSON still has https URLs.",
                "extend": "Cap total search calls at 3 in code even if the model begs for more.",
            },
            {
                "title": "Log prompts + click two URLs (37:00–40:00)",
                "desc": "Course habit: what you typed to the vibe coder, in your words. Then prove the tool.",
                "prompt": "Append a Lecture 3 section to AI_prompts.md summarizing, in my own words: scaffold, search_web, query-prompt design, run_search.py, and the function-calling variant. One sentence on what broke on the first try if anything did.",
                "check": "Lecture 3 section exists with >=4 bullets. No API keys in the log. Open two saved URLs in a browser.",
            },
        ],
    },
}

# Lecture 4 student HTML is hand-authored (style.css navbar + Riemann swarm).
# Live pages: lectures/slides/lec04-slides.html + lectures/vibe/lec04-vibe.html (14 slides, 40/40).
# Rebuild will drop head CSS into slide 1 — do not run build_lectures.py for this lecture.
DECK[4] = {
    "title": "Agents",
    "slides": [
        {"class": " title-slide", "html": """        <style>
.slide-deck-body { overflow: hidden; }
    .slide-deck-body .site-nav { flex-shrink: 0; }
    .slide { max-width: 980px; }
    .slide h1 { font-size: clamp(1.95rem, 4.4vw, 2.7rem); }
    .slide p, .slide li { font-size: clamp(1.08rem, 2.3vw, 1.32rem); }
    .punch { font-size: clamp(1.25rem, 2.8vw, 1.7rem); font-weight: 800; line-height: 1.3; margin: 0.35rem 0 1rem; }
    .caveat {
      margin-top: 0.85rem; padding: 0.7rem 0.95rem; border-radius: 10px;
      background: #fff3c4; border-left: 5px solid #bd9b60; font-weight: 700; font-size: 1.02rem;
    }
    [data-theme="dark"] .caveat { background: #3a2a12; color: #ffe8c8; }
    .news-card {
      display: grid; grid-template-columns: 240px 1fr; gap: 1rem; align-items: center;
      margin: 0.65rem 0; padding: 0.7rem; border-radius: 14px;
      background: #fff; border: 2px solid #286dc0; text-decoration: none; color: inherit;
    }
    .news-card img { width: 100%; height: 128px; object-fit: cover; border-radius: 10px; background: #0b1220; }
    .news-card .kicker { font-size: 0.78rem; font-weight: 800; letter-spacing: 0.06em; text-transform: uppercase; color: #286dc0; margin: 0 0 0.25rem; }
    .news-card h3 { margin: 0 0 0.35rem; font-size: 1.12rem; color: var(--yale-blue); line-height: 1.25; }
    .news-card p { margin: 0; font-size: 0.95rem; }
    [data-theme="dark"] .news-card { background: #1a2433; border-color: #7c5cff; }
    [data-theme="dark"] .news-card h3 { color: #fff; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0.75rem 0 0.25rem; }
    .chip { background: #00356b; color: #fff; font-weight: 800; font-size: 0.95rem; padding: 0.4rem 0.75rem; border-radius: 999px; }
    .chip.orange { background: #f4633a; }
    .chip.gold { background: #bd9b60; color: #1a1208; }
    .chip.green { background: #0f7b4a; }
    .chip.pink { background: #c73e82; }
    .big-no {
      display: inline-block; background: #c73e82; color: #fff; font-weight: 800;
      padding: 0.15rem 0.55rem; border-radius: 8px;
    }
    .hw-flow { display: grid; grid-template-columns: repeat(6, 1fr); gap: 0.4rem; margin: 0.85rem 0; }
    .hw-flow div {
      background: #e8eef4; border-radius: 10px; padding: 0.55rem 0.4rem; text-align: center;
      font-weight: 800; font-size: 0.78rem; line-height: 1.25; color: #00356b;
    }
    .hw-flow .stop { background: #c73e82; color: #fff; }
    [data-theme="dark"] .hw-flow div { background: #132a45; color: #d6e6f5; }
    .role-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.45rem; margin: 0.7rem 0 0.2rem; }
    .role-grid div {
      border-radius: 10px; padding: 0.55rem 0.4rem; text-align: center;
      color: #fff; font-weight: 800; font-size: 0.78rem; line-height: 1.25;
    }
    .role-grid .n { display: block; font-size: 1.35rem; line-height: 1.1; margin-bottom: 0.15rem; }
    .r-key { background: #0f7b4a; }
    .r-help { background: #bd9b60; color: #1a1208; }
    .r-dead { background: #5c7086; }
    .r-val { background: #286dc0; }
    .r-write { background: #f4633a; }
    .bound-row { display: grid; grid-template-columns: 1fr auto 1fr; gap: 0.6rem; align-items: center; margin: 0.7rem 0; }
    .bound-box { border-radius: 12px; padding: 0.7rem 0.8rem; text-align: center; }
    .bound-box .n { font-size: 2rem; font-weight: 800; line-height: 1; }
    .bound-old { background: #e8eef4; color: #00356b; }
    .bound-new { background: #0f7b4a; color: #fff; }
    .bound-row .arrow { font-size: 1.6rem; font-weight: 800; color: #286dc0; text-align: center; }
    [data-theme="dark"] .bound-old { background: #132a45; color: #d6e6f5; }
    .slide svg.swarm-svg { width: 100%; max-height: 168px; margin: 0.35rem 0 0.15rem; }
    .slide img.swarm-img { display: block; width: 100%; max-height: min(46vh, 340px); object-fit: contain; border-radius: 12px; margin: 0.4rem 0 0.25rem; background: #0b1220; }
    .instructor-banner {
      display: inline-block; background: #bd9b60; color: #1a1208; font-weight: 800;
      font-size: 0.82rem; letter-spacing: 0.06em; text-transform: uppercase;
      padding: 0.28rem 0.7rem; border-radius: 999px; margin: 0 0 0.7rem;
    }
    .pace-list { list-style: none; padding-left: 0; margin: 0.4rem 0; }
    .pace-list li {
      display: grid; grid-template-columns: 5.6rem 1fr; gap: 0.7rem;
      align-items: start; margin: 0.45rem 0;
      font-size: clamp(0.98rem, 2vw, 1.18rem);
    }
    .pace-min { font-weight: 800; color: #c73e82; font-variant-numeric: tabular-nums; }
    [data-theme="dark"] .pace-min { color: #ffd166; }
    .cost-pills { display: flex; flex-wrap: wrap; gap: 0.45rem; margin: 0.65rem 0 0.35rem; }
    .cost-pills span {
      background: #e8eef4; color: #00356b; font-weight: 800; font-size: 0.88rem;
      padding: 0.4rem 0.7rem; border-radius: 999px;
    }
    .cost-pills .hot { background: #c73e82; color: #fff; }
    [data-theme="dark"] .cost-pills span { background: #132a45; color: #d6e6f5; }
    @media (max-width: 720px) {
      .news-card { grid-template-columns: 1fr; }
      .hw-flow, .role-grid { grid-template-columns: 1fr 1fr; }
      .bound-row { grid-template-columns: 1fr; }
    }
        </style>
        <h1>Agents</h1>
        <p class="subtitle">MGT 409 · Lecture 4 · Tauhid Zaman</p>
        <p class="punch">Same tools as last week. Now they loop.<br>You still own the stop condition.</p>
        <p class="takeaway">Syllabus: multi-step agents that call tools in a loop — and limits on what they may do without a human.</p>"""},
        {"html": """        <p class="instructor-banner">Instructor outline — remove before class.</p>
        <h1>The story in 40 minutes</h1>
        <ul class="pace-list">
          <li><span class="pace-min">0–2</span><span><strong>Cold open.</strong> Same tools, now they loop. You own the brakes.</span></li>
          <li><span class="pace-min">2–6</span><span><strong>One-shot vs loop.</strong> L3 one call vs L4 observe → decide → act. HW1 path vs HW2 palette.</span></li>
          <li><span class="pace-min">6–14</span><span><strong>The loop + stops.</strong> max_steps, finish schema, hard denylist. No send.</span></li>
          <li><span class="pace-min">14–24</span><span><strong>Riemann swarm (2 slides).</strong> Progress not proof. ~650 approaches → critique → ~60 subagents.</span></li>
          <li><span class="pace-min">24–31</span><span><strong>HW2.</strong> Draft, don’t send. Short palette; <code>send_email</code> is not in it.</span></li>
          <li><span class="pace-min">31–37</span><span><strong>Traces + dial.</strong> JSONL, looping cost, autonomy: search auto, send is a human click.</span></li>
          <li><span class="pace-min">37–40</span><span><strong>Handoff.</strong> 5-step scout. Then a 40-minute lab.</span></li>
        </ul>"""},
        {"html": """        <h1>Last week vs. this week</h1>
        <div class="two-col">
          <div class="compare-box">
            <h3>Lecture 3 · one call</h3>
            <p>The model asks for <code>search_web</code>. Your Python runs it. Done. HW1 energy: you write the path; cost is predictable.</p>
          </div>
          <div class="compare-box">
            <h3>Lecture 4 · a loop</h3>
            <p>Same tools, inside observe → decide → act until a stop fires. HW2 energy: you write the <em>palette</em> and the <em>brakes</em>. Path varies. So does the bill.</p>
          </div>
        </div>
        <p class="takeaway">Scripts scale because the path is known. Agents need stop conditions because the path is not.</p>"""},
        {"html": """        <h1>The loop you actually ship</h1>
        <svg class="flow-svg" viewBox="0 0 720 210" aria-label="Agent loop: observe, decide, act, stop">
          <defs>
            <marker id="a4g" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#0f7b4a"/></marker>
            <marker id="a4r" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c73e82"/></marker>
            <marker id="a4b" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#286dc0"/></marker>
          </defs>
          <rect x="250" y="12" width="220" height="52" rx="12" fill="#00356b"/>
          <text x="360" y="34" text-anchor="middle" font-size="14" fill="#fff" font-weight="700">LLM planner</text>
          <text x="360" y="52" text-anchor="middle" font-size="11" fill="#cde4ff">observe goal + history</text>
          <line x1="360" y1="64" x2="360" y2="88" stroke="#286dc0" stroke-width="3" marker-end="url(#a4b)"/>
          <rect x="230" y="90" width="260" height="44" rx="10" fill="#fff3c4" stroke="#bd9b60" stroke-width="2"/>
          <text x="360" y="118" text-anchor="middle" font-size="14" fill="#00356b" font-weight="700">Tool call, ask human, or FINISH?</text>
          <line x1="230" y1="112" x2="118" y2="112" stroke="#0f7b4a" stroke-width="3" marker-end="url(#a4g)"/>
          <rect x="18" y="90" width="100" height="44" rx="10" fill="#0f7b4a"/>
          <text x="68" y="118" text-anchor="middle" font-size="13" fill="#fff" font-weight="700">Act / tool</text>
          <line x1="68" y1="134" x2="68" y2="178" stroke="#0f7b4a" stroke-width="3"/>
          <line x1="68" y1="178" x2="360" y2="178" stroke="#0f7b4a" stroke-width="3"/>
          <line x1="360" y1="178" x2="360" y2="64" stroke="#0f7b4a" stroke-width="3" marker-end="url(#a4g)"/>
          <text x="200" y="198" font-size="11" fill="#0f7b4a" font-weight="700">append result · loop</text>
          <line x1="490" y1="112" x2="590" y2="112" stroke="#c73e82" stroke-width="3" marker-end="url(#a4r)"/>
          <rect x="590" y="90" width="116" height="44" rx="10" fill="#c73e82"/>
          <text x="648" y="118" text-anchor="middle" font-size="13" fill="#fff" font-weight="700">STOP</text>
        </svg>
        <p><strong>Observe</strong> goal + history + “no send.” <strong>Decide</strong> next tool, escalate, or finish. <strong>Act</strong> in <em>your</em> runtime — auth, logs, budget. The model proposes; you execute.</p>"""},
        {"html": """        <h1>Stop conditions (non-negotiable)</h1>
        <div class="chip-row">
          <span class="chip">max_steps</span>
          <span class="chip gold">finish tool</span>
          <span class="chip green">valid schema</span>
          <span class="chip orange">$ budget</span>
          <span class="chip pink">human gate</span>
        </div>
        <ul>
          <li><strong>max_steps</strong> — 5–10 for class; production adds wall-clock and USD (Lecture 12).</li>
          <li><strong>finish(JSON)</strong> — the only legal exit. Invalid schema? Return an error to the model. Do not crash-send.</li>
          <li><strong>Hard denylist</strong> — no <code>send_email</code>, no <code>buy</code>, no <code>rm -rf</code> unless a human clicked yes.</li>
        </ul>
        <p class="takeaway">An agent without max_steps is a liability with an API key.</p>"""},
        {"html": """        <h1>This summer: progress, not a proof</h1>
        <a class="news-card" href="https://www.anthropic.com/research/riemann-zeta" target="_blank" rel="noopener noreferrer">
          <img src="../images/lec04/news-riemann.svg" alt="Anthropic research card: Claude improved a Riemann zeta bound, not a proof of the hypothesis">
          <div>
            <p class="kicker">Anthropic · 10 Aug 2026</p>
            <h3>Claude did not prove the Riemann hypothesis. It moved a related bound.</h3>
            <p>An unreleased research Claude improved the proven share of zeta zeros on the critical line from <strong>41.6% to 67.2%</strong>.</p>
          </div>
        </a>
        <div class="bound-row">
          <div class="bound-box bound-old"><div class="n">41.6%</div>prior lower bound</div>
          <div class="arrow">→</div>
          <div class="bound-box bound-new"><div class="n">67.2%</div>Claude’s argument</div>
        </div>
        <p class="caveat">Not a proof of RH. Anthropic does not expect these techniques to yield one. Experts looked on short notice — this is not journal peer review.</p>
        <p class="source-note">Primary: <a href="https://www.anthropic.com/research/riemann-zeta" target="_blank" rel="noopener noreferrer">Anthropic, “Learning more about Claude’s mathematical capabilities”</a> (10 Aug 2026; paper changelog 13 Aug). Context: <a href="https://www.scientificamerican.com/article/no-ai-didnt-just-solve-the-thorniest-problem-in-math/" target="_blank" rel="noopener noreferrer">Howlett, Scientific American</a> (12 Aug 2026).</p>"""},
        {"html": """        <h1>~650 approaches → critique → ~60 subagents</h1>
        <p>A non-mathematician staffer (Jarred Sumner) left the math choices to the model. Phase 1: about <strong>650 ideas, none worked</strong>. Prompted to continue, Claude spent ~1.5 days coordinating about <strong>60 subagents</strong>.</p>
        <svg class="swarm-svg" viewBox="0 0 720 158" aria-label="Propose, attempt, critique, prune swarm">
          <defs>
            <marker id="sw" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#286dc0"/></marker>
          </defs>
          <rect x="8" y="18" width="150" height="86" rx="12" fill="#00356b"/>
          <text x="83" y="48" text-anchor="middle" font-size="15" fill="#fff" font-weight="800">PROPOSE</text>
          <text x="83" y="70" text-anchor="middle" font-size="12" fill="#cde4ff">~650 approaches</text>
          <text x="83" y="88" text-anchor="middle" font-size="12" fill="#cde4ff">Phase 1: all failed</text>
          <line x1="158" y1="61" x2="176" y2="61" stroke="#286dc0" stroke-width="3" marker-end="url(#sw)"/>
          <rect x="184" y="18" width="150" height="86" rx="12" fill="#0f7b4a"/>
          <text x="259" y="48" text-anchor="middle" font-size="15" fill="#fff" font-weight="800">ATTEMPT</text>
          <text x="259" y="70" text-anchor="middle" font-size="12" fill="#d4ffe8">~2,400 shell cmds</text>
          <text x="259" y="88" text-anchor="middle" font-size="12" fill="#d4ffe8">scripts + zeta checks</text>
          <line x1="334" y1="61" x2="352" y2="61" stroke="#286dc0" stroke-width="3" marker-end="url(#sw)"/>
          <rect x="360" y="18" width="150" height="86" rx="12" fill="#286dc0"/>
          <text x="435" y="48" text-anchor="middle" font-size="15" fill="#fff" font-weight="800">CRITIQUE</text>
          <text x="435" y="70" text-anchor="middle" font-size="12" fill="#cde4ff">agents referee</text>
          <text x="435" y="88" text-anchor="middle" font-size="12" fill="#cde4ff">54 arXiv papers</text>
          <line x1="510" y1="61" x2="528" y2="61" stroke="#286dc0" stroke-width="3" marker-end="url(#sw)"/>
          <rect x="536" y="18" width="176" height="86" rx="12" fill="#c73e82"/>
          <text x="624" y="48" text-anchor="middle" font-size="15" fill="#fff" font-weight="800">PRUNE</text>
          <text x="624" y="70" text-anchor="middle" font-size="12" fill="#ffe0ec">keep what survives</text>
          <text x="624" y="88" text-anchor="middle" font-size="12" fill="#ffe0ec">drop dead ends</text>
          <text x="360" y="140" text-anchor="middle" font-size="13" fill="#5c7086" font-weight="700">Two Claude Code sessions · 31 million output tokens · human mostly said “keep going”</text>
        </svg>
        <div class="role-grid">
          <div class="r-key"><span class="n">2</span>key ideas</div>
          <div class="r-help"><span class="n">13</span>contributed</div>
          <div class="r-dead"><span class="n">30</span>produced nothing</div>
          <div class="r-val"><span class="n">13</span>validators</div>
          <div class="r-write"><span class="n">2</span>wrote the paper</div>
        </div>
        <p class="takeaway">Copy: many cheap attempts, explicit critique, explicit prune. Do not copy unbounded copies on one box — that is a turf war, not a swarm.</p>
        <p class="source-note">Role split: Anthropic footnote. Graphic: <a href="../images/lec04/riemann-swarm.svg">riemann-swarm.svg</a>. Writeup: <a href="https://www.anthropic.com/research/riemann-zeta" target="_blank" rel="noopener noreferrer">anthropic.com/research/riemann-zeta</a>. Turf war: <a href="https://www.anthropic.com/research/multiagent-systems" target="_blank" rel="noopener noreferrer">multiagent-systems</a>.</p>"""},
        {"html": """        <h1>Homework 2 is this loop — draft, don’t send</h1>
        <p>FiftyFlowers wants <strong>business</strong> customers (planners, studios, venues) — volume buyers, not one-off retail.</p>
        <div class="hw-flow">
          <div>P2<br>ICP from their site</div>
          <div>P3<br>search queries</div>
          <div>P4<br>investigate loop</div>
          <div>P5<br>score fit</div>
          <div>P6<br>draft email</div>
          <div class="stop">P6<br>DO NOT SEND</div>
        </div>
        <ul>
          <li>P4 is the agent-y bit: crawl, cite <code>source_url</code>, or leave the field empty.</li>
          <li>P6: 120–180 word draft, facts from page snapshots, saved as JSON. Palette has <code>draft_email</code>. It does not have <code>send_email</code>.</li>
        </ul>
        <p class="takeaway">Observe → decide → act → <strong>stop before send</strong>. Grown-up split: the agent drafts; a human would approve. <span class="big-no">No send.</span></p>"""},
        {"html": """        <h1>Fewer tools beat kitchen sinks</h1>
        <table>
          <tr><th>Tool</th><th>When the agent should use it</th><th>HW2 cousin</th></tr>
          <tr><td><code>search_web</code></td><td>Find candidate businesses from the ICP</td><td>P3</td></tr>
          <tr><td><code>fetch_page</code></td><td>Read a real page; keep a snapshot</td><td>P4</td></tr>
          <tr><td><code>score_icp</code></td><td>Apply your rubric, not vibes</td><td>P5</td></tr>
          <tr><td><code>draft_email</code></td><td>Write a 120–180 word note with cited facts</td><td>P6</td></tr>
          <tr><td><code>finish</code></td><td>Schema complete; stop looping</td><td>traces + report</td></tr>
          <tr><td><code>send_email</code></td><td><strong>Not in the palette.</strong> Human only.</td><td>explicit ban</td></tr>
        </table>
        <p>Fewer, well-described tools beat “here is the entire internet, good luck.”</p>"""},
        {"html": """        <h1>Traces, or it didn’t happen</h1>
        <div class="cost-pills">
          <span>script ~700 tok</span>
          <span>3-step ~2k</span>
          <span>8-step, no cap 6k+</span>
          <span class="hot">Riemann swarm 31M</span>
        </div>
        <ul>
          <li>Every step: role, tool name, args, truncated result, tokens if the API gives them.</li>
          <li>JSONL: <code>output/traces/{run_id}.jsonl</code> — graders debug this, not “it felt right.”</li>
          <li>HW2 source rule: no <code>source_url</code> → empty field. Invented emails are a zero.</li>
        </ul>
        <div class="diagram">step 1: search_web("New Haven wedding florist wholesale")
step 2: fetch_page("https://example-florist.com/contact")
step 3: finish({companies: [...], notes: "..."})  → VALID
step 4: send_email(...)  → BLOCKED  (not in palette, not in HW2)</div>"""},
        {"html": """        <h1>Human in the loop is a dial</h1>
        <svg class="flow-svg" viewBox="0 0 720 150" aria-label="Autonomy dial from draft to send">
          <rect x="20" y="40" width="150" height="70" rx="12" fill="#0f7b4a"/>
          <text x="95" y="70" text-anchor="middle" font-size="13" fill="#fff" font-weight="700">Search / fetch</text>
          <text x="95" y="90" text-anchor="middle" font-size="11" fill="#d4ffe8">auto OK</text>
          <rect x="195" y="40" width="150" height="70" rx="12" fill="#bd9b60"/>
          <text x="270" y="70" text-anchor="middle" font-size="13" fill="#1a1208" font-weight="700">Score / draft</text>
          <text x="270" y="90" text-anchor="middle" font-size="11" fill="#1a1208">spot-check</text>
          <rect x="370" y="40" width="150" height="70" rx="12" fill="#f4633a"/>
          <text x="445" y="70" text-anchor="middle" font-size="13" fill="#fff" font-weight="700">Send / buy</text>
          <text x="445" y="90" text-anchor="middle" font-size="11" fill="#fff">human click</text>
          <rect x="545" y="40" width="155" height="70" rx="12" fill="#c73e82"/>
          <text x="622" y="70" text-anchor="middle" font-size="13" fill="#fff" font-weight="700">Delete / pay</text>
          <text x="622" y="90" text-anchor="middle" font-size="11" fill="#fff">never auto</text>
        </svg>
        <p class="takeaway">Turn autonomy up only with eval evidence. The Riemann run still asked humans to check the paper. HW2 P8 is you disagreeing with the model on purpose.</p>"""},
        {"class": " section-slide", "html": """        <h1>→ Vibe coding (40 minutes)</h1>
        <p class="punch">A 5-step scout agent.<br>Search, fetch, finish JSON.<br>Sending email is out of the palette.</p>
        <p>If it never finishes, repeats the same search, or invents a contact — those are today’s failure modes. Fix them in the loop, not in a paragraph.</p>
        <p><a href="../vibe/lec04-vibe.html">Open today’s prompts →</a></p>"""},
        {"html": """        <h1>Failure modes you’ll hit in the lab</h1>
        <table>
          <tr><th>Symptom</th><th>Fix</th></tr>
          <tr><td>Never calls finish</td><td>System prompt: “You MUST call finish to end.”</td></tr>
          <tr><td>Same search 4 times</td><td>Track queries; return “duplicate query blocked.”</td></tr>
          <tr><td>JSON soup</td><td>Validate in the finish tool; send the error back.</td></tr>
          <tr><td>Invented contacts</td><td>Require <code>source_url</code> or empty string. HW2 P4.</td></tr>
          <tr><td>Token lava</td><td>Lower max_steps; cheaper model for grunt fetches.</td></tr>
        </table>"""},
        {"html": """        <h1>What to remember</h1>
        <ul>
          <li>Agent = LLM + tools + <strong>loop</strong> + <strong>stop conditions</strong> + <strong>traces</strong>.</li>
          <li>Autonomy is a dial. Draft ≠ send. HW2 is the dial at “research intern.”</li>
          <li>Useful swarms <strong>propose, attempt, critique, prune</strong>. Unbounded copies start turf wars.</li>
          <li>Claude’s zeta bound is progress on a related problem — not a proof of the Riemann hypothesis.</li>
        </ul>
        <p class="takeaway">Next: aim the loop at <strong>images</strong> — Lecture 5, image analysis.</p>"""},
    ],
        "vibe": {
        "goal": "Leave with lec04/agent.py that loops (max 5 steps), calls search_web + fetch_page + finish_research, writes a JSONL trace, and hard-blocks any send. Toy New Haven florist scout — not Homework 2. 40-minute lab.",
        "zip": None,
        "steps": [
            {
                "title": "Agent skeleton with max_steps (0–6 min)",
                "desc": "The loop is ~30 lines of Python you must be able to explain to a VP who thinks the AI just knows.",
                "prompt": "Create lec04/agent.py with run_agent(goal: str, max_steps: int = 5) -> dict. Maintain a messages list. Each step: call OpenAI with tools [search_web, fetch_page, finish_research]. If the model returns a tool call: execute it in Python, append the tool result, continue. If max_steps is hit: raise RuntimeError that includes the trace file path. Use gpt-4o-mini. Load OPENAI_API_KEY from .env. Do not put a real key in any file.",
                "check": "run_agent('List 3 New Haven florists that look like wholesale buyers') starts without crashing; it cannot run forever.",
            },
            {
                "title": "Reuse search_web from Lecture 3 (6–14 min)",
                "desc": "Agents are loops around last week’s tools. Do not rewrite search.",
                "prompt": "Import or copy search_web from lec03. Register the tool schema name search_web with parameters {query: string}. In the agent loop, execute it and return a JSON string of results truncated to 2000 characters per call. Log the query. If the model repeats an identical query, return the tool error 'duplicate query blocked' instead of hitting the API again.",
                "check": "A trace line exists with search_web and at least one real HTTPS URL (not invented).",
            },
            {
                "title": "fetch_page — tiny version of HW2 investigate (14–22 min)",
                "desc": "Search snippets lie. Homework 2 Problem 4 will make you crawl real sites and cite source_url.",
                "prompt": "Add tool fetch_page with parameters {url: string}. Only allow https URLs. Fetch the page, strip to visible text, truncate to 4000 characters, return JSON {url, text, status}. If fetch fails, return an error string to the model — do not invent page content. Save a snapshot under lec04/output/pages/ named so a human can match it to the URL.",
                "check": "After a run, output/pages/ has a file whose contents came from the URL in the trace, not from the model’s memory.",
            },
            {
                "title": "finish_research with a schema — still no Send (22–30 min)",
                "desc": "The agent cannot shrug and print prose. It must call finish with valid JSON, or keep looping until max_steps.",
                "prompt": "Add finish_research accepting {companies: array, notes: string}. Validate: at least 2 companies; each has name, url, one_line, source_url (source_url must be a real https URL from a prior tool result). notes length >= 40 characters. On validation failure: return the error to the model and continue the loop. On success: store the payload, return {status: done}, and end the loop. Do not add send_email. If the model tries any tool named send_email, send_message, or mail_to, return 'blocked: human approval required' and do not send anything.",
                "check": "A deliberately invalid finish (0 companies) shows up as a tool error in the trace; a valid finish ends the run. No email leaves the machine.",
            },
            {
                "title": "JSONL traces + CLI (30–37 min)",
                "desc": "Graders (and your future ops team) do not debug vibes. They debug files.",
                "prompt": "Write lec04/output/traces/{timestamp}.jsonl with one JSON object per line: step, role, tool_name, tool_args, content_excerpt, token_usage if available. Print the trace path at the end of run_agent. Add if __name__ == '__main__': argparse --goal and --max-steps. Write the validated finish payload to lec04/output/scout.json. README with one example command using the New Haven florist goal.",
                "check": "After one run you have scout.json plus a jsonl file with ≥3 lines including tool calls.",
            },
            {
                "title": "AI_prompts.md + stretch (37–40 min)",
                "desc": "Same habit as every homework: log what you typed, in your own words.",
                "prompt": "Append a Lecture 4 section to AI_prompts.md with the prompts you actually used for the skeleton, search, fetch, finish, and traces. Stretch: add a --dry-run flag that mocks the LLM with a scripted sequence (search → fetch → invalid finish → valid finish) so you can unit-test the loop without spending tokens.",
                "check": "AI_prompts.md has Lecture 4. Stretch: dry-run produces a trace with a blocked invalid finish and a successful valid finish.",
                "extend": "Cap total tool-result characters stored in messages (e.g. 8k) so a chatty fetch cannot blow the context window.",
            },
        ],
    },
}

# Lecture 5 student HTML is hand-authored (custom CSS + images in lectures/images/lec05/).
# Do not run build_lectures.py expecting to preserve that styling. Vibe steps below match the live page.
DECK[5] = {
    "title": "Image Analysis",
    "slides": [
        {"class": " title-slide", "html": """        <style>
          .instructor-banner { background:#c73e82; color:#fff; font-weight:800; letter-spacing:0.04em; text-transform:uppercase; padding:0.5rem 0.9rem; border-radius:8px; font-size:0.88rem; margin:0 0 0.85rem; }
        </style>
        <h1>Image Analysis</h1>
        <p class="subtitle">MGT 409 · Lecture 5 · Tauhid Zaman</p>
        <p class="subtitle">AI turns pictures into words. Then into fields a catalog can search.</p>"""},
        {"html": """        <div class="instructor-banner">Instructor outline — remove before class.</div>
        <h1>40-minute lecture clock</h1>
        <table>
          <tr><th>Min</th><th>Beat</th></tr>
          <tr><td>0–3</td><td>Hook: the associate has a photo, not a SKU. Vision = image → words / JSON.</td></tr>
          <tr><td>3–8</td><td>CLIP (2021): two towers, contrastive space. Matcher, not a captioner.</td></tr>
          <tr><td>8–14</td><td>Then → now: BLIP / Flamingo / GPT-4V → GPT-5.6 vision + Gemini 3.6 native image.</td></tr>
          <tr><td>14–20</td><td>How a VLM “sees”: 32px patches → multimodal tokens → text out.</td></tr>
          <tr><td>20–28</td><td>Token math + $: one SKU on Luna vs Terra vs Sol; 20 SKUs vs 10k.</td></tr>
          <tr><td>28–34</td><td>Catalog pattern: schema + parallel calls (HW3 P2 contract — no solution).</td></tr>
          <tr><td>34–38</td><td>Evals: don’t invent logos. Vision is expensive tokens + a schema.</td></tr>
          <tr><td>38–40</td><td>Hand off to the 40-minute vibe lab (toy tees, not the homework pack).</td></tr>
          <tr><td>~40</td><td>Then vibe: 1–2 images → JSON captions.</td></tr>
        </table>"""},
        {"html": """        <h1>The associate has a photo</h1>
        <img src="../images/lec05/hero-shop.png" alt="Cartoon Campus Customs shop: associate showing a t-shirt photo on a phone" style="width:100%;max-height:42vh;object-fit:cover;border-radius:14px">
        <ul>
          <li>Last weeks: tools and agents on <strong>text</strong>.</li>
          <li>Today: force an image into <strong>fields</strong> — garment, color, readable marks, search tags.</li>
          <li>Homework 3 Problem 2 is this job at 20 SKUs. In class we do two toy tees.</li>
        </ul>
        <p class="takeaway">If you cannot see it in the pixels, it is not in the JSON.</p>"""},
        {"html": """        <h1>CLIP (2021): a shared space, not a writer</h1>
        <svg class="flow-svg" viewBox="0 0 760 210" aria-label="CLIP two-tower">
          <defs><marker id="c5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path class="arrow" d="M0,0 L6,3 L0,6 Z"/></marker></defs>
          <rect class="box-light" x="16" y="28" width="150" height="70" rx="12"/>
          <text x="91" y="58" text-anchor="middle" font-size="15" font-weight="800">Photo</text>
          <line x1="166" y1="63" x2="198" y2="63" stroke="#f4a261" stroke-width="3" marker-end="url(#c5)"/>
          <rect class="box-dark" x="200" y="20" width="170" height="86" rx="12"/>
          <text class="on-dark" x="285" y="55" text-anchor="middle" font-size="15" font-weight="800">Image encoder</text>
          <rect class="box-light" x="16" y="128" width="150" height="70" rx="12"/>
          <text x="91" y="158" text-anchor="middle" font-size="15" font-weight="800">Caption</text>
          <line x1="166" y1="163" x2="198" y2="163" stroke="#286dc0" stroke-width="3" marker-end="url(#c5)"/>
          <rect class="box-dark" x="200" y="120" width="170" height="86" rx="12"/>
          <text class="on-dark" x="285" y="155" text-anchor="middle" font-size="15" font-weight="800">Text encoder</text>
          <rect class="box-light" x="432" y="70" width="150" height="86" rx="12"/>
          <text x="507" y="104" text-anchor="middle" font-size="14" font-weight="800">Shared space</text>
          <rect class="box-dark" x="602" y="78" width="140" height="70" rx="12"/>
          <text class="on-dark" x="672" y="108" text-anchor="middle" font-size="14" font-weight="800">Score / retrieve</text>
        </svg>
        <p>OpenAI, 5 Jan 2021: contrastive image–text pre-training. A <strong>matcher</strong>, not a captioner.</p>
        <p class="takeaway">CLIP will not write <code>visual_description</code>. It ranks which text is closest to the image.</p>
        <p class="source-note"><a href="https://openai.com/index/clip/" target="_blank" rel="noopener">openai.com/index/clip</a> · <a href="https://arxiv.org/abs/2103.00020" target="_blank" rel="noopener">arXiv:2103.00020</a></p>"""},
        {"html": """        <h1>Then they learned to talk about the picture</h1>
        <table>
          <tr><th>When</th><th>What</th><th>Manager one-liner</th></tr>
          <tr><td>2022</td><td><strong>BLIP</strong></td><td>Now it writes captions, not just matches them.</td></tr>
          <tr><td>2022</td><td><strong>Flamingo</strong></td><td>Few-shot: show a couple of examples, then ask.</td></tr>
          <tr><td>Sep 2023</td><td><strong>GPT-4V</strong></td><td>ChatGPT can look. Image in, fluent text out.</td></tr>
          <tr><td>Dec 2023–</td><td><strong>Gemini</strong></td><td>Native multimodal from the start.</td></tr>
        </table>
        <p class="source-note">BLIP <a href="https://arxiv.org/abs/2201.12086" target="_blank" rel="noopener">arXiv:2201.12086</a> · Flamingo <a href="https://arxiv.org/abs/2204.14198" target="_blank" rel="noopener">arXiv:2204.14198</a> · GPT-4V <a href="https://openai.com/index/gpt-4v-system-card/" target="_blank" rel="noopener">system card, 25 Sep 2023</a></p>"""},
        {"html": """        <h1>Now (Aug 2026): vision is the default model</h1>
        <div class="two-col">
          <div class="compare-box">
            <h3>OpenAI GPT-5.6</h3>
            <p>Sol / Terra / Luna all take image input and return text. Alias <code>gpt-5.6</code> → Sol. Luna is the cheap catalog workhorse.</p>
          </div>
          <div class="compare-box">
            <h3>Google Gemini 3.6 Flash</h3>
            <p>Natively multimodal (text, image, audio, video, PDF → text). GA 21 Jul 2026.</p>
          </div>
        </div>
        <p class="source-note"><a href="https://openai.com/index/previewing-gpt-5-6-sol/" target="_blank" rel="noopener">GPT-5.6 Sol preview</a> · <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/" target="_blank" rel="noopener">Gemini 3.6 Flash, 21 Jul 2026</a></p>"""},
        {"html": """        <h1>How a vision model “sees”</h1>
        <svg class="flow-svg" viewBox="0 0 760 130" aria-label="Patches to JSON">
          <defs><marker id="v5" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path class="arrow" d="M0,0 L6,3 L0,6 Z"/></marker></defs>
          <rect class="box-light" x="10" y="30" width="118" height="70" rx="12"/>
          <text x="69" y="70" text-anchor="middle" font-size="14" font-weight="800">Photo</text>
          <rect class="box-dark" x="160" y="22" width="150" height="86" rx="12"/>
          <text class="on-dark" x="235" y="68" text-anchor="middle" font-size="14" font-weight="800">32×32 patches</text>
          <rect class="box-light" x="342" y="22" width="150" height="86" rx="12"/>
          <text x="417" y="68" text-anchor="middle" font-size="14" font-weight="800">+ text tokens</text>
          <rect class="box-dark" x="524" y="22" width="226" height="86" rx="12"/>
          <text class="on-dark" x="637" y="68" text-anchor="middle" font-size="14" font-weight="800">Decoder → JSON</text>
        </svg>
        <p>GPT-5.6 covers the image with 32×32 px patches. Those tokens sit next to your prompt. Then it writes text.</p>
        <p class="takeaway">Pixels → tokens → words. You own the schema. The model owns the guess.</p>"""},
        {"html": """        <h1>What an image costs in tokens</h1>
        <ul>
          <li><strong>GPT-4o tiles:</strong> <code>detail=low</code> ~85 tokens; <code>high</code> = fit 2048², shortest side 768, then 512px tiles (85 + 170×tiles). 1024² ≈ 765 tokens.</li>
          <li><strong>GPT-5.6 patches:</strong> <code>ceil(W/32)×ceil(H/32)</code>. Low → 512² = 256 tokens. Default <code>original</code> does not shrink. 1024² = 1,024 tokens. 3000×2000 original ≈ 5,922.</li>
        </ul>
        <p class="source-note"><a href="https://developers.openai.com/api/docs/guides/images-vision" target="_blank" rel="noopener">OpenAI images &amp; vision</a> · <a href="https://developers.openai.com/api/docs/pricing" target="_blank" rel="noopener">pricing</a></p>"""},
        {"html": """        <h1>One product photo, three price tags</h1>
        <p>1024×1024, <code>detail=original</code> → 1,024 image tokens + ~200 JSON out. Standard short-context rates after 30 Jul 2026.</p>
        <table>
          <tr><th>Model</th><th>In / out per 1M</th><th>1 SKU</th><th>20 SKUs</th><th>10,000 SKUs</th></tr>
          <tr><td>Luna</td><td>$0.20 / $1.20</td><td>~$0.0004</td><td>~1¢</td><td>~$4–5</td></tr>
          <tr><td>Terra</td><td>$2 / $12</td><td>~$0.004</td><td>~9¢</td><td>~$45</td></tr>
          <tr><td>Sol</td><td>$5 / $30</td><td>~$0.011</td><td>~22¢</td><td>~$110</td></tr>
        </table>
        <p class="takeaway">HW3’s 20 SKUs is coffee money on Luna if you resize. 10k unresized originals is a budget line.</p>
        <p class="source-note"><a href="https://developers.openai.com/api/docs/pricing" target="_blank" rel="noopener">OpenAI API pricing</a> · <a href="https://community.openai.com/t/announcing-a-major-price-drop-for-5-6-terra-and-luna-and-fast-mode-for-5-6-sol/1388484" target="_blank" rel="noopener">30 Jul Luna/Terra cut</a></p>"""},
        {"html": """        <h1>20 photos should not wait in a line</h1>
        <ul>
          <li>HW3 Problem 2: concurrent vision calls (threads / asyncio) with a small worker cap (5–10).</li>
          <li>A sequential wait-for-each-image loop does not count. Retry failures; skip missing files; do not invent the shirt.</li>
        </ul>
        <p class="takeaway">Parallelism is a latency budget. Students write the script in HW3 — not from this slide.</p>"""},
        {"html": """        <h1>Vision is tokens + a schema</h1>
        <div class="diagram">{
  "sku": "TOY-CREST",
  "visual_description": "Navy tee, gold shield crest…",
  "search_tags": ["navy", "crest", "short sleeve"],
  "logo_or_text_cues": []
}</div>
        <p class="takeaway">Empty array is honest. A fake “YALE” you wanted to see is a grading fail.</p>"""},
        {"html": """        <h1>Don’t invent the crest</h1>
        <img src="../images/lec05/dont-invent.png" alt="Seen vs invented logo" style="width:100%;max-height:36vh;object-fit:cover;border-radius:14px">
        <table>
          <tr><th>Eval</th><th>What it catches</th></tr>
          <tr><td>OCR honesty</td><td>Words in JSON that are not on the garment</td></tr>
          <tr><td>Color / type</td><td>“hoodie” on a tee</td></tr>
          <tr><td>Skip log</td><td>Missing file filled from the product title</td></tr>
        </table>
        <p class="takeaway">Manager takeaway: vision is expensive tokens plus a schema. Evals still matter.</p>"""},
        {"html": """        <h1>This month in vision</h1>
        <ul>
          <li><strong>GPT-5.6 GA + 30 Jul price cut:</strong> Luna $0.20/$1.20, Terra $2/$12. Default image detail on 5.6 is original.</li>
          <li><strong>Gemini 3.6 Flash (21 Jul 2026):</strong> native image in; Flash workhorse.</li>
        </ul>
        <p class="source-note"><a href="https://openai.com/index/previewing-gpt-5-6-sol/" target="_blank" rel="noopener">OpenAI GPT-5.6</a> · <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/" target="_blank" rel="noopener">Gemini 3.6 Flash</a></p>"""},
        {"class": " section-slide", "html": """        <h1>→ Vibe coding</h1>
        <p>Two toy tees · one vision call · JSON schema · parallel pair</p>
        <p><a href="../vibe/lec05-vibe.html">Open vibe coding prompts →</a></p>
        <p class="takeaway">Do not unzip Homework 3. If you invent a logo on the plain tee, the run fails.</p>"""},
        {"html": """        <h1>What to remember</h1>
        <ul>
          <li>CLIP matched images to text. Modern VLMs <strong>write</strong> the text — and JSON.</li>
          <li>An image is tokens. <code>detail</code> and resolution are budget knobs.</li>
          <li>20 SKUs on Luna is cheap. 10k unresized originals is not. Parallelize; cap workers.</li>
          <li>Schema + evals: empty marks beat a hallucinated crest.</li>
        </ul>
        <p class="takeaway">Next: <strong>video</strong> — a clip is speech plus stills. Same honesty rule.</p>"""},
    ],
    "vibe": {
        "goal": "Turn two toy product photos into JSON captions a search index could use (visual_description, search_tags, logo_or_text_cues). Homework 3 Problem 2 shape — not the assignment. Do not unzip the Campus Customs pack.",
        "zip": "",
        "steps": [
            {
                "title": "Scaffold + two photos (0–6 min)",
                "desc": "Copy the class toy images. Do not unzip HW3.",
                "prompt": "Create lec05/ with products/, prompts/, output/. Copy toy-crest-tee.png and toy-plain-tee.png from the lecture images folder into lec05/products/. Write toy_skus.json with exactly 2 products: TOY-CREST (navy crest tee) and TOY-PLAIN (heather gray blank tee). prompts/describe_product.md stub. README: class toy, not the HW3 pack. .env.example. No real key.",
                "check": "Both pngs open on disk. JSON has 2 rows. No Homework 3 zip in the folder.",
            },
            {
                "title": "One image → a caption (6–14 min)",
                "desc": "First prove the model can see.",
                "prompt": "Create caption_one.py that sends products/toy-crest-tee.png to gpt-5.6-luna. Prompt: describe garment in 3 sentences; if you cannot read text, say so. Write output/crest_caption.txt. detail=low is fine. Load OPENAI_API_KEY from .env.",
                "check": "Caption mentions a navy/blue tee and a crest/shield. No Bitcoin, Yale wordmark, or Handsome Dan.",
            },
            {
                "title": "Same image, now JSON (14–24 min)",
                "desc": "Homework 3 grades fields, not vibes.",
                "prompt": "Fill prompts/describe_product.md: look at the image; do not invent logos/words/mascots. Return JSON only: visual_description, search_tags, logo_or_text_cues (empty if none). describe_one.py merges TOY-CREST inventory + vision into output/one_product.json.",
                "check": "one_product.json parses with sku TOY-CREST and the three vision keys. logo_or_text_cues has no unread words.",
            },
            {
                "title": "The trap photo: invent nothing (24–32 min)",
                "desc": "The plain tee is the eval.",
                "prompt": "Run the same describe prompt on products/toy-plain-tee.png. Save output/plain_product.json with sku TOY-PLAIN. logo_or_text_cues MUST be empty. Do not add a crest, bulldog, or wordmark.",
                "check": "If the JSON names a logo, the run fails. Fix the prompt; do not hand-edit the JSON.",
            },
            {
                "title": "Two images in parallel (32–38 min)",
                "desc": "HW3 P2 forbids a sequential wait-for-each-image loop.",
                "prompt": "describe_two.py vision-calls BOTH toy images concurrently (threads/asyncio) with max 2 workers. Write output/toy_catalog.json {products: [...]}. Retry a failed SKU once. Do not process the HW3 20-SKU pack.",
                "check": "Two products in one JSON. Not a blocking for-loop. Plain tee still has empty logo cues.",
            },
            {
                "title": "AI_prompts.md (38–40 min)",
                "desc": "Log what you asked, in your words.",
                "prompt": "Append a Lecture 5 section to AI_prompts.md: caption prompt, JSON schema prompt, and one sentence on whether the model invented a mark on the plain tee.",
                "check": "AI_prompts.md has a Lecture 5 heading and at least one prompt in your own words.",
                "extend": "Print estimated image tokens for one 1024×1024 photo using ceil(W/32)*ceil(H/32) and a Luna $ line. Optionally compare detail=low vs original on the crest tee.",
            },
        ],
    },
}

# Lec06 live HTML is hand-maintained (40 min lecture + 40 min vibe). Do not run
# build_lectures.py expecting to keep custom clocks / CSS. Keep this dict aligned
# so a rebuild does not restore CLIP/token-cost slides (those belong to Lecture 5).
DECK[6] = {
    "title": "Video Analysis",
    "slides": [
        {"class": " title-slide", "html": """        <style>
          .joke { margin-top:1rem; padding:0.85rem 1.1rem; border-radius:12px; background:linear-gradient(90deg,#fff3c4,#ffe0ef); border-left:6px solid #ff2d7b; font-weight:700; }
          .news-card { display:grid; grid-template-columns:1.05fr 1fr; gap:0.85rem; background:#0f1c33; color:#fff; border-radius:16px; overflow:hidden; border:3px solid #14c8c8; margin:0.45rem 0; }
          .news-card img { width:100%; height:148px; object-fit:cover; }
          .news-card .copy { padding:0.7rem 0.9rem; }
          .news-card a { color:#7ef0ff; font-weight:700; }
          .hero-pic { width:100%; max-height:260px; object-fit:cover; border-radius:14px; border:4px solid #ff2d7b; }
          .instructor-banner { background:#ff2d7b; color:#fff; font-weight:800; letter-spacing:0.04em; text-transform:uppercase; padding:0.5rem 0.9rem; border-radius:8px; font-size:0.88rem; margin:0 0 0.85rem; }
          .status-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:0.7rem; }
          .status { border-radius:12px; padding:0.85rem; color:#fff; }
          .status.go { background:#0a8f5a; } .status.maybe { background:#d97706; } .status.no { background:#c81e4a; }
        </style>
        <h1>Video Analysis</h1>
        <p class="subtitle">MGT 409 · Lecture 6 · Images &amp; videos</p>
        <p class="subtitle">A phone clip is speech plus stills. Match a SKU — or refuse.</p>"""},
        {"html": """        <div class="instructor-banner">Instructor outline — remove before class.</div>
        <h1>40-minute lecture clock</h1>
        <ul>
          <li><strong>0–4</strong> Cold open: last class was stills (Image Analysis). Today a clip is speech + a stack of stills. Campus Customs phone.</li>
          <li><strong>4–10</strong> Product: Lens Live; Search boxes take video. ChatGPT camera ≠ OpenAI frames API.</li>
          <li><strong>10–18</strong> Pipeline: transcribe → frames → crop in code → text shortlist → vision-compare → refuse.</li>
          <li><strong>18–26</strong> Speech carries size/color; the crop is a file.</li>
          <li><strong>26–34</strong> Three honest endings. How the loop fails.</li>
          <li><strong>34–38</strong> PII. HW3 P4–P7 is this pipeline; in-class is 3 toy SKUs.</li>
          <li><strong>38–40</strong> Handoff to vibe. CLIP / image-token formulas stay in Lecture 5.</li>
        </ul>"""},
        {"html": """        <h1>Last class vs this class</h1>
        <div class="two-col">
          <div class="compare-box"><h3>Lecture 5 · stills</h3><p>One photo → structured text. Catalog onboarding.</p></div>
          <div class="compare-box"><h3>Lecture 6 · video</h3><p>Audio + a stack of stills. Size/color may be spoken. The graphic may appear in only one frame.</p></div>
        </div>
        <p class="joke">Treat a clip as one fat JPEG and you pay for 200 blurry elbows — and still miss the logo.</p>"""},
        {"html": """        <h1>Campus Customs: a clip, not a barcode</h1>
        <img class="hero-pic" src="../images/lec06/campus-customs-phone-ask.png" alt="Associate looking at a phone video of a Yale shirt">
        <ul>
          <li><strong>Campus Customs</strong> (HW3): phone clip of a tee. Size and color are spoken. The mascot is pixels.</li>
          <li>You are cloning Amazon Lens on 20 SKUs, with a refusal button.</li>
        </ul>"""},
        {"html": """        <h1>Demo theater vs your API key</h1>
        <ul>
          <li>GPT-4o keynote showed live video. August 2026 ChatGPT still has a camera.</li>
          <li>OpenAI API: sample frames, then vision. Gemini API: native video files.</li>
        </ul>
        <p class="takeaway">The consumer demo and the API product are not the same SKU.</p>
        <p class="source-note"><a href="https://developers.openai.com/cookbook/examples/gpt_with_vision_for_video_understanding" target="_blank" rel="noopener">OpenAI video-as-frames cookbook</a> · <a href="https://ai.google.dev/gemini-api/docs/video-understanding" target="_blank" rel="noopener">Gemini video docs</a></p>"""},
        {"html": """        <h1>Customers already search with a clip</h1>
        <article class="news-card">
          <img src="../images/lec06/news-amazon-lens-live.png" alt="Amazon Lens Live screenshot">
          <div class="copy">
            <p><strong>Amazon Lens Live</strong> — camera on, matches in a carousel. You will not beat that index; you will learn the loop at closet scale.</p>
            <p><a href="https://www.aboutamazon.com/news/retail/search-image-amazon-lens-live-shopping-rufus" target="_blank" rel="noopener">aboutamazon.com →</a></p>
          </div>
        </article>
        <article class="news-card">
          <img src="../images/lec06/news-google-io-2026-search.png" alt="Google I/O 2026 Search blog">
          <div class="copy">
            <p>May 19, 2026 — Liz Reid: Search box inputs include <strong>videos</strong>.</p>
            <p><a href="https://blog.google/products-and-platforms/products/search/search-io-2026/" target="_blank" rel="noopener">blog.google I/O 2026 →</a></p>
          </div>
        </article>"""},
        {"html": """        <h1>Video is a pipeline, not a blob</h1>
        <svg class="flow-svg" viewBox="0 0 900 140" aria-label="Video pipeline">
          <defs><marker id="a6" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path class="arrow" d="M0,0 L6,3 L0,6 Z"/></marker></defs>
          <rect class="box-light" x="10" y="45" width="100" height="50" rx="8"/><text x="60" y="75" text-anchor="middle" font-size="12">Clip</text>
          <line x1="110" y1="70" x2="135" y2="70" stroke="#ff2d7b" stroke-width="3" marker-end="url(#a6)"/>
          <rect class="box-dark" x="135" y="45" width="110" height="50" rx="8"/><text class="on-dark" x="190" y="75" text-anchor="middle" font-size="12">Transcribe</text>
          <line x1="245" y1="70" x2="270" y2="70" stroke="#14c8c8" stroke-width="3" marker-end="url(#a6)"/>
          <rect class="box-light" x="270" y="45" width="110" height="50" rx="8"/><text x="325" y="75" text-anchor="middle" font-size="12">Frames</text>
          <line x1="380" y1="70" x2="405" y2="70" stroke="#ff2d7b" stroke-width="3" marker-end="url(#a6)"/>
          <rect class="box-light" x="405" y="45" width="110" height="50" rx="8"/><text x="460" y="75" text-anchor="middle" font-size="12">Crop in code</text>
          <line x1="515" y1="70" x2="540" y2="70" stroke="#ff2d7b" stroke-width="3" marker-end="url(#a6)"/>
          <rect class="box-dark" x="540" y="45" width="120" height="50" rx="8"/><text class="on-dark" x="600" y="75" text-anchor="middle" font-size="12">Text top 5</text>
          <line x1="660" y1="70" x2="685" y2="70" stroke="#f5c518" stroke-width="3" marker-end="url(#a6)"/>
          <rect class="box-light" x="685" y="45" width="190" height="50" rx="8"/><text x="780" y="75" text-anchor="middle" font-size="12">Vision-compare / none</text>
        </svg>
        <p class="takeaway">HW3: do not dump every frame into inventory search as step 1.</p>"""},
        {"html": """        <h1>Why not send the whole movie?</h1>
        <img class="hero-pic" src="../images/lec06/video-is-just-frames.png" alt="Film strip of shirt frames with one good frame circled">
        <p>A 10s clip at 30 fps is 300 frames. Most are ceiling, thumb, or blur. HW3: save at least five. Last class priced one still; today the lever is <em>which frames</em> you send — not CLIP or tile formulas.</p>"""},
        {"html": """        <h1>Speech carries size and color</h1>
        <ul>
          <li>Pixels show the graphic. Audio often carries color and size.</li>
          <li>Transcribe → <code>query_text.json</code>. Empty string if unspoken. Do not invent “medium.”</li>
        </ul>
        <p class="takeaway">Ignore speech and you match the right shirt in the wrong size.</p>"""},
        {"html": """        <h1>The crop has to be a file</h1>
        <ul>
          <li>Model proposes <code>x,y,w,h</code>. <strong>Your code</strong> writes the crop. Then vision looks at that file.</li>
        </ul>
        <p class="takeaway">If the crop only exists in the model’s imagination, it is not evidence.</p>"""},
        {"html": """        <h1>Shortlist, compare, refuse</h1>
        <ul>
          <li>Text search first (~5 SKUs). Vision-compare second. Weak text list → skip pixels.</li>
          <li><strong>match</strong> · <strong>variant_oos</strong> · <strong>not_in_inventory</strong>. Never mint a fake SKU.</li>
        </ul>"""},
        {"html": """        <h1>How video search fails</h1>
        <ul>
          <li>Wrong frame (wall poster) · invented SKU · ignored transcript · 200-frame dump.</li>
          <li>Customer video is PII. Keep crop + catalog photo + transcript snippet — not the selfie.</li>
        </ul>"""},
        {"html": """        <h1>Homework 3 map (do not solve now)</h1>
        <ul>
          <li>P2–P3: stills → text catalog + ranked text search (last lecture).</li>
          <li>P4–P6: transcribe, sample frames, crop tool. P7: agent loop + honest no-match.</li>
        </ul>
        <p class="takeaway">In-class vibe = toy clip and 3 SKUs · 40 minutes. HW3 = 20 Yale tees.</p>
        <p><a href="../vibe/lec06-vibe.html">Open vibe coding prompts →</a></p>"""},
        {"html": """        <h1>Summary</h1>
        <ul>
          <li>Video = speech + sampled stills. Agents choose; code crops; vision compares a shortlist.</li>
          <li>Retail shipped this (Lens Live). Search boxes take video (I/O 2026).</li>
          <li>Cap frames. Refuse when it is not in inventory.</li>
        </ul>"""},
    ],
    "vibe": {
        "goal": "40-minute lab. Wire a tiny video lookup: transcribe a short clip, sample frames, crop a region in code, describe it, and match against a 3-SKU toy catalog — or honestly say it is not in inventory. This is the Homework 3 shape, not the assignment. Do not build a CLIP index or a token spreadsheet.",
        "zip": None,
        "steps": [
            {
                "title": "Scaffold lec06 (0–6 min)",
                "desc": "Prompts in files. A catalog so small you can see when the agent is lying.",
                "prompt": "Create lec06/ with media/, prompts/transcribe_ask.md pick_frame.md describe_crop.md match_sku.md, toy_catalog.json with exactly 3 products (sku, name, color, sizes[], image_note), sample_frames.py, transcribe_ask.py, inspect_region.py, mini_lookup.py, output/frames/, output/crops/, requirements.txt (openai, python-dotenv, pillow). Optional opencv or imageio-ffmpeg. .env.example, .gitignore. No real API key.",
                "check": "Three SKUs in JSON; prompt files exist; no key in the repo.",
            },
            {
                "title": "Transcribe the ask (6–13 min)",
                "desc": "Speech carries size/color. Pixels carry the mascot.",
                "prompt": "Write prompts/transcribe_ask.md and transcribe_ask.py --video media/ask.mp4 --out-dir output. Use Whisper or OpenAI audio API. Save output/query_text.json with video_path, transcript, requested_color, requested_size (empty string if not spoken). Never invent a size.",
                "check": "JSON exists; unspoken size/color are empty strings.",
            },
            {
                "title": "Sample frames (13–20 min)",
                "desc": "Video in this course is stills you can point to.",
                "prompt": "sample_frames.py --video media/ask.mp4 --out-dir output. Save at least 5 jpgs under output/frames/ and output/frames.json with path + timestamp_sec. Document the sampling rule in README.",
                "check": "Five images on disk.",
            },
            {
                "title": "Best frame, then crop in code (20–30 min)",
                "desc": "Model may propose a box. Pillow must write the crop.",
                "prompt": "Vision picks best product frame into output/best_frame.json. inspect_region.py --frame PATH --x --y --w --h writes a crop under output/crops/, calls vision with describe_crop.md, saves output/crop_inspect.json with source_frame, crop_path, box, description. Crop file must come from code.",
                "check": "output/crops/ has an openable image.",
            },
            {
                "title": "Mini lookup: text then vision then refuse (30–38 min)",
                "desc": "Three SKUs only. Helpful hallucination is a fail.",
                "prompt": "mini_lookup.py reads query_text.json, crop_inspect.json, toy_catalog.json. Score 3 SKUs 0-100; if top score is weak, status=not_in_inventory and sku=\"\". Write output/mini_lookup.json with status, sku, reply, evidence. Do not invent a fourth SKU. Do not build an embedding index.",
                "check": "Banana clip (or similar) yields not_in_inventory.",
            },
            {
                "title": "Log prompts (38–40 min)",
                "desc": "What you typed, in your words.",
                "prompt": "Append Lecture 6 to AI_prompts.md with paraphrased prompts. Note one thing the first prompt got wrong.",
                "check": "AI_prompts.md has Lecture 6 with at least four bullets.",
                "extend": "Second run on a still that should not match; save output/mini_lookup_no_match.json. Do not spend class time on a frame-count cost spreadsheet.",
            },
        ],
    },
}

DECK[7] = {
    "title": "Web Applications",
    "slides": [
        {"class": " title-slide", "html": """        <p class="chip">Apps &amp; deployment · Lecture 7</p>
        <h1>Web Applications</h1>
        <p class="subtitle">MGT 409 · 40 min lecture + 40 min vibe · Homework 4</p>
        <p>College Street Music Hall: a guest site, not a terminal demo.</p>
        <p class="takeaway">Today is FastAPI + Vite + SQLite on your laptop. A public URL is Lecture 8.</p>"""},
        {"html": """        <p class="instructor-banner">Instructor outline — remove before class.</p>
        <h1>~40 minutes</h1>
        <table class="pace">
          <tr><th>Min</th><th>Beat</th></tr>
          <tr><td>0–5</td><td>Cold open: guests do not run python cs_agent.py</td></tr>
          <tr><td>5–12</td><td>Lovable $13.3B — generating HTML is cheap; owning auth/data/session is the product</td></tr>
          <tr><td>12–20</td><td>Stack: Vite :5173 → FastAPI :8000 → SQLite. CORS is the bouncer. Not a URL (L8)</td></tr>
          <tr><td>20–26</td><td>Grounding: SELECT FAQ rows; one cite/refuse brain</td></tr>
          <tr><td>26–34</td><td>Product: hashed login + chats that survive refresh</td></tr>
          <tr><td>34–37</td><td>Screenshot / voice are extra cables — typed chat still has to work</td></tr>
          <tr><td>37–40</td><td>HW4 map, failure modes, vibe handoff</td></tr>
        </table>
        <p class="takeaway">Then 40 min vibe: two processes + SQLite on localhost. Do not deploy today.</p>"""},
        {"html": """        <h1>Scripts shipped. Guests want a site.</h1>
        <div class="two-col">
          <div class="compare-box hot"><h3><code>python cs_agent.py</code></h3><p>You, a TA, flags, JSON files. Nobody at the merch table runs this.</p></div>
          <div class="compare-box cool"><h3>A page they can click</h3><p>Login, calendar, chat. SQLite keeps the thread. HW4 grades this — still on localhost today.</p></div>
        </div>
        <p class="takeaway">If a guest cannot click it, it is a lab notebook — not a product.</p>"""},
        {"html": """        <h1>The market priced “English → running app”</h1>
        <p>Aug 12, 2026: Lovable raises $400M at a $13.3B valuation (TechCrunch). They told the press ~$500M ARR run-rate.</p>
        <p class="source-note">Source: <a href="https://techcrunch.com/2026/08/12/lovable-confirms-new-13-3b-valuation-raises-another-400m/">TechCrunch, Julie Bort, Aug 12, 2026</a>; <a href="https://lovable.dev/blog/series-c">Lovable Series C post</a>.</p>
        <p class="takeaway">The scarce thing is no longer “can we generate a page.” It is “can we own auth, data, and the guest session.”</p>"""},
        {"html": """        <h1>You are not Lovable. You are the venue.</h1>
        <ul>
          <li>A prompt-to-app tool can fake a pretty UI in 90 seconds.</li>
          <li>It will also invent an elevator, store passwords in plaintext, and drop the chat on refresh.</li>
          <li>HW4: FastAPI + React (Vite) + hashed login + SQLite threads, grounded in a closed FAQ.</li>
        </ul>
        <p class="takeaway">Buy a demo. Grade a repo. Managers who cannot tell the difference will ship the demo.</p>"""},
        {"html": """        <h1>The stack, in one picture</h1>
        <div class="diagram">React / Vite  :5173  →  FastAPI  :8000  →  SQLite (users, faq, chats)
                                          ↘  cite / refuse agent  (no embeddings; keys stay here)</div>
        <p class="joke">CORS is the bouncer between 5173 and 8000. Forget it and the browser fails — the model is not “broken.”</p>"""},
        {"html": """        <h1>Two servers, one guest</h1>
        <table>
          <tr><th>Process</th><th>Job</th><th>Never put here</th></tr>
          <tr><td>Vite</td><td>Buttons, brand, the box they type in</td><td>API keys, hashes, the FAQ dump</td></tr>
          <tr><td>FastAPI</td><td>Auth, SQL, agent</td><td>Hard-coded passwords in git</td></tr>
          <tr><td>SQLite</td><td>Source of truth</td><td>A second copy of truth in random JSON</td></tr>
        </table>
        <p class="takeaway">React draws. FastAPI checks ID. The database is the guest list. Lecture 8 puts this at a URL — not today.</p>"""},
        {"html": """        <h1>A venue FAQ is a SELECT, not a vector store</h1>
        <ul>
          <li>HW4 P2: ≥4 categories, SELECT those rows, then answer.</li>
          <li>Do not embed the FAQ. One cite/refuse brain — not a swarm on a one-pager.</li>
        </ul>
        <p class="takeaway">If the bot invents lockers or an elevator, you stuffed the model instead of selected FAQ rows.</p>"""},
        {"html": """        <h1>Passwords are not a prompt</h1>
        <p>Salt + hash in SQLite (PBKDF2 settings in meta). Compare hashes. Never echo what they typed. Signup = new salt.</p>
        <p class="takeaway">If the users table is plaintext, you do not have a web app. You have a leak with CSS.</p>"""},
        {"html": """        <h1>Chats that survive a refresh</h1>
        <ul>
          <li>POST /chat writes both sides of the turn into SQLite.</li>
          <li>GET /chats is that user only. New chat starts a row; old threads stay.</li>
        </ul>
        <p class="takeaway">If the thread dies on refresh, you returned JSON and never INSERTed.</p>"""},
        {"html": """        <h1>Screenshot and voice are extra cables</h1>
        <p>Type must work first. Screenshot = capture the page, not a webcam. Voice = STT → same agent → TTS.</p>
        <p class="takeaway">HW4 P7–8. In vibe today these are stretch. The product is login + chat + a database.</p>"""},
        {"html": """        <h1>Homework 4 is this lecture, unzipped</h1>
        <ul>
          <li>P2 categorize FAQ · P3 cite/refuse · P4 hashed login</li>
          <li>P5 FastAPI + saved chats · P6 React Vite · P7–8 screenshot + voice</li>
        </ul>
        <table>
          <tr><th>Symptom</th><th>Actual problem</th></tr>
          <tr><td>Failed to fetch</td><td>CORS, wrong port, API not running</td></tr>
          <tr><td>Invented refunds</td><td>Stuffed the model, not selected FAQ rows</td></tr>
          <tr><td>Login always fails</td><td>Wrong hash settings / compared plaintext</td></tr>
          <tr><td>Chats vanish</td><td>Returned JSON, forgot to INSERT</td></tr>
          <tr><td>API key in the React bundle</td><td>The key is now in every guest’s browser</td></tr>
        </table>"""},
        {"class": " section-slide", "html": """        <h1>→ Vibe coding · 40 minutes</h1>
        <p>Toy FastAPI + Vite + SQLite chat. Not the HW4 zip. Not a deploy.</p>
        <p><a href="../vibe/lec07-vibe.html">Open the timed vibe prompts →</a></p>"""},
        {"html": """        <h1>What to remember</h1>
        <ul>
          <li>Web app = UI + API + database.</li>
          <li>Hash passwords. Persist chats. Ground answers in SELECTed rows.</li>
          <li>Next: Lecture 8, Application Deployment — a URL that is not localhost.</li>
        </ul>"""},
    ],
    "vibe": {
        "goal": "Leave with a React (Vite) page talking to FastAPI, with FAQ and chats in SQLite — the shape of Homework 4, not the assignment. Invent a 6-row fake venue FAQ. Do not deploy.",
        "zip": None,
        "steps": [
            {
                "title": "Two folders, SQLite seed (0–5 min)",
                "desc": "Empty project. Not the HW4 zip. SQLite from minute one.",
                "prompt": "Create lec07_web/backend/ and lec07_web/frontend/. In backend/, write seed_db.py that creates venue.db with faq, users (salt+hash only), and messages. Insert 6 FAQ rows (bag policy, door time, refunds, no elevator, food, tickets). README: FastAPI on 8000, Vite on 5173. Do not copy Homework 4 files. Do not add a Render/Dockerfile.",
                "check": "sqlite3 venue.db prints 6 FAQ rows. README names both ports.",
            },
            {
                "title": "FastAPI: health + chat from SQLite (5–14 min)",
                "desc": "Browser never holds the API key. SELECT FAQ rows — do not embed.",
                "prompt": "In backend/server.py make a FastAPI app with CORS for http://127.0.0.1:5173. GET /health → {\"ok\": true}. POST /chat JSON {message} SELECTs matching faq rows from venue.db, asks the OpenAI API to answer only from those rows, returns {answer, refused, citations}. Never invent an elevator. Run: uvicorn server:app --host 127.0.0.1 --port 8000",
                "check": "curl GET /health works. Elevator question cites the no-elevator row or refuses.",
            },
            {
                "title": "Vite React chat UI (14–24 min)",
                "desc": "A real frontend folder. Stay on localhost.",
                "prompt": "In frontend/ scaffold React + Vite. One CSS file (not only inline). Dark venue colors, big type. A text box + Send that POSTs to http://127.0.0.1:8000/chat and shows answer + refused. README: npm install && npm run dev. Do not put OPENAI_API_KEY in any frontend file.",
                "check": "From the browser you can ask about bags and see a reply.",
            },
            {
                "title": "Hash a password, persist the thread (24–34 min)",
                "desc": "Never store plaintext. Chats survive refresh.",
                "prompt": "Add backend/auth.py with hash_password and verify. Seed one user in venue.db (salt+hash only). POST /login {username, password} → {ok, token}. POST /chat INSERTs both sides into messages. GET /chats returns that user's turns. Frontend: login before chat; refresh restores prior turns.",
                "check": "Wrong password → ok false. users table has no plaintext. Refresh keeps the last turn.",
            },
            {
                "title": "AI_prompts.md (34–40 min)",
                "desc": "Log what you asked, in your words.",
                "prompt": "Create AI_prompts.md with a Lecture 7 section. One prompt summary per step. Note what broke (CORS, ports, hash mismatch, chats vanishing) and the follow-up prompt that fixed it.",
                "check": "Five step headings; at least one “what was lacking” sentence.",
                "extend": "Screenshot button that captures the current page (not a webcam) and POSTs it with the message. Typed chat must still work. Do not deploy.",
            },
        ],
    },
}
