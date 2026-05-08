import streamlit as st
from graph.workflow import app

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="NexaCore Knowledge Assistant",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ======================================================
# GLOBAL STYLES
# ======================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

/* ── ROOT TOKENS ── */
:root {
    --bg-base:       #0a0d14;
    --bg-surface:    #10151f;
    --bg-elevated:   #161d2b;
    --bg-card:       #1a2236;
    --border:        #1e2d47;
    --border-accent: #243855;
    --text-primary:  #e8edf5;
    --text-secondary:#8a9ab8;
    --text-muted:    #4a5a78;
    --accent-cyan:   #00c9ff;
    --accent-blue:   #4a7bff;
    --accent-violet: #7c5cfc;
    --accent-glow:   rgba(0, 201, 255, 0.15);
    --success:       #00e5a0;
    --warning:       #ffb340;
    --radius-sm:     6px;
    --radius-md:     12px;
    --radius-lg:     18px;
    --font-display:  'Syne', sans-serif;
    --font-body:     'DM Sans', sans-serif;
    --font-mono:     'DM Mono', monospace;
}

/* ── GLOBAL RESET ── */
html, body, [class*="css"] {
    font-family: var(--font-body);
    background-color: var(--bg-base);
    color: var(--text-primary);
}

/* ── STREAMLIT CHROME OVERRIDES ── */
.stApp { background: var(--bg-base); }

header[data-testid="stHeader"] {
    background: transparent;
    border-bottom: 1px solid var(--border);
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: var(--bg-surface) !important;
    border-right: 1px solid var(--border) !important;
    padding: 0 !important;
}

section[data-testid="stSidebar"] > div {
    padding: 2rem 1.5rem;
}

/* Sidebar brand mark */
.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--border);
}

.sidebar-hexagon {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-violet));
    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    flex-shrink: 0;
}

.sidebar-brand-text {
    font-family: var(--font-display);
    font-size: 1rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1.2;
}

.sidebar-brand-sub {
    font-size: 0.65rem;
    font-weight: 500;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* Sidebar section label */
.sidebar-label {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.75rem;
    margin-top: 1.5rem;
}

/* Feature pills */
.feature-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0.55rem 0.75rem;
    border-radius: var(--radius-sm);
    margin-bottom: 4px;
    transition: background 0.2s;
}

.feature-row:hover { background: var(--bg-elevated); }

.feature-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--accent-cyan);
    flex-shrink: 0;
    box-shadow: 0 0 6px var(--accent-cyan);
}

.feature-dot.violet { background: var(--accent-violet); box-shadow: 0 0 6px var(--accent-violet); }
.feature-dot.blue   { background: var(--accent-blue);   box-shadow: 0 0 6px var(--accent-blue); }
.feature-dot.success{ background: var(--success);        box-shadow: 0 0 6px var(--success); }

.feature-text {
    font-size: 0.82rem;
    color: var(--text-secondary);
    font-weight: 400;
}

/* Status indicator */
.status-bar {
    margin-top: 2rem;
    padding: 0.75rem 1rem;
    background: var(--bg-elevated);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    border-left: 3px solid var(--success);
}

.status-label {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 4px;
}

.status-value {
    font-size: 0.78rem;
    color: var(--success);
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 6px;
}

.status-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--success);
    animation: pulse-green 2s ease-in-out infinite;
}

@keyframes pulse-green {
    0%, 100% { opacity: 1; box-shadow: 0 0 0 0 rgba(0,229,160,0.4); }
    50% { opacity: 0.7; box-shadow: 0 0 0 5px rgba(0,229,160,0); }
}

/* ── MAIN CONTENT ── */
.main-header {
    margin-bottom: 2.5rem;
}

.header-eyebrow {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent-cyan);
    margin-bottom: 0.6rem;
}

.header-title {
    font-family: var(--font-display);
    font-size: 2.6rem;
    font-weight: 800;
    line-height: 1.1;
    color: var(--text-primary);
    letter-spacing: -0.02em;
    margin-bottom: 0.8rem;
}

.header-title span {
    background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue), var(--accent-violet));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.header-desc {
    font-size: 0.95rem;
    color: var(--text-secondary);
    line-height: 1.6;
    max-width: 580px;
    font-weight: 300;
}

/* ── QUERY CARD ── */
.query-card {
    background: var(--bg-card);
    border: 1px solid var(--border-accent);
    border-radius: var(--radius-lg);
    padding: 1.75rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}

.query-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent-cyan), transparent);
    opacity: 0.6;
}

.query-label {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.75rem;
}

/* Text input overrides */
.stTextInput > div > div {
    background: var(--bg-elevated) !important;
    border: 1.5px solid var(--border-accent) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-body) !important;
    font-size: 0.95rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}

.stTextInput > div > div:focus-within {
    border-color: var(--accent-cyan) !important;
    box-shadow: 0 0 0 3px rgba(0, 201, 255, 0.12) !important;
}

.stTextInput input {
    color: var(--text-primary) !important;
    background: transparent !important;
    font-family: var(--font-body) !important;
    caret-color: var(--accent-cyan) !important;
}

.stTextInput input::placeholder {
    color: var(--text-muted) !important;
}

/* Button overrides */
.stButton > button {
    background: linear-gradient(135deg, var(--accent-blue), var(--accent-violet)) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: var(--radius-md) !important;
    font-family: var(--font-display) !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.65rem 2rem !important;
    transition: opacity 0.2s, transform 0.15s, box-shadow 0.2s !important;
    box-shadow: 0 4px 20px rgba(74, 123, 255, 0.3) !important;
}

.stButton > button:hover {
    opacity: 0.92 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 28px rgba(74, 123, 255, 0.45) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── RESPONSE CARD ── */
.response-wrapper {
    background: var(--bg-card);
    border: 1px solid var(--border-accent);
    border-radius: var(--radius-lg);
    padding: 2rem;
    position: relative;
    overflow: hidden;
    animation: fadeSlideUp 0.4s ease;
}

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

.response-wrapper::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent-violet), var(--accent-cyan), transparent);
}

.response-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 1.25rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border);
}

.response-icon {
    width: 32px;
    height: 32px;
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-violet));
    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    flex-shrink: 0;
}

.response-title {
    font-family: var(--font-display);
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: 0.03em;
}

.response-subtitle {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    color: var(--text-muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.response-body {
    font-size: 0.93rem;
    line-height: 1.75;
    color: var(--text-secondary);
    font-weight: 300;
}

.response-body p { margin-bottom: 0.85rem; }

/* ── SPINNER OVERRIDE ── */
.stSpinner > div {
    border-top-color: var(--accent-cyan) !important;
}

/* ── EXAMPLE QUERIES ── */
.examples-section {
    margin-top: 1rem;
}

.examples-label {
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.65rem;
}

.example-chip {
    display: inline-block;
    background: var(--bg-elevated);
    border: 1px solid var(--border-accent);
    border-radius: 100px;
    padding: 0.35rem 0.9rem;
    font-size: 0.78rem;
    color: var(--text-secondary);
    margin: 0 6px 6px 0;
    cursor: pointer;
    transition: background 0.2s, border-color 0.2s, color 0.2s;
}

.example-chip:hover {
    background: var(--bg-card);
    border-color: var(--accent-cyan);
    color: var(--accent-cyan);
}

/* ── WARNING / INFO ── */
.stWarning {
    background: rgba(255, 179, 64, 0.08) !important;
    border: 1px solid rgba(255, 179, 64, 0.25) !important;
    border-radius: var(--radius-md) !important;
    color: var(--warning) !important;
}

/* ── DIVIDERS ── */
hr {
    border: none;
    border-top: 1px solid var(--border);
    margin: 2rem 0;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: var(--border-accent); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

/* ── METRIC CARDS ── */
.metrics-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.75rem;
}

.metric-card {
    flex: 1;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 1rem 1.25rem;
}

.metric-label {
    font-family: var(--font-mono);
    font-size: 0.6rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 4px;
}

.metric-value {
    font-family: var(--font-display);
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-primary);
}

.metric-value.cyan   { color: var(--accent-cyan); }
.metric-value.violet { color: var(--accent-violet); }
.metric-value.success { color: var(--success); }
</style>
""",
    unsafe_allow_html=True,
)

# ======================================================
# SIDEBAR
# ======================================================
with st.sidebar:
    st.markdown(
        """
    <div class="sidebar-brand">
        <div class="sidebar-hexagon"></div>
        <div>
            <div class="sidebar-brand-text">NexaCore</div>
            <div class="sidebar-brand-sub">Knowledge Assistant</div>
        </div>
    </div>

    <div class="sidebar-label">Agentic Pipeline</div>

    <div class="feature-row">
        <div class="feature-dot"></div>
        <span class="feature-text">LangGraph Workflow</span>
    </div>
    <div class="feature-row">
        <div class="feature-dot blue"></div>
        <span class="feature-text">Agentic RAG</span>
    </div>
    <div class="feature-row">
        <div class="feature-dot violet"></div>
        <span class="feature-text">ChromaDB Vector Store</span>
    </div>
    <div class="feature-row">
        <div class="feature-dot success"></div>
        <span class="feature-text">Ollama Embeddings</span>
    </div>

    <div class="sidebar-label">Intelligence Layer</div>

    <div class="feature-row">
        <div class="feature-dot"></div>
        <span class="feature-text">Gemini LLM</span>
    </div>
    <div class="feature-row">
        <div class="feature-dot blue"></div>
        <span class="feature-text">Source Citations</span>
    </div>
    <div class="feature-row">
        <div class="feature-dot violet"></div>
        <span class="feature-text">LLM-based Evaluation</span>
    </div>
    <div class="feature-row">
        <div class="feature-dot success"></div>
        <span class="feature-text">Query Rewriting</span>
    </div>

    <div class="status-bar">
        <div class="status-label">System Status</div>
        <div class="status-value">
            <span class="status-dot"></span>
            All systems operational
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ======================================================
# MAIN HEADER
# ======================================================
st.markdown(
    """
<div class="main-header">
    <div class="header-eyebrow">⬡ Enterprise Intelligence Platform</div>
    <div class="header-title">Ask the <span>Knowledge Graph</span></div>
    <div class="header-desc">
        Query enterprise policies, onboarding guides, security procedures,
        AI governance, and internal workflows — powered by an agentic retrieval pipeline.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ======================================================
# METRIC ROW
# ======================================================
st.markdown(
    """
<div class="metrics-row">
    <div class="metric-card">
        <div class="metric-label">Documents Indexed</div>
        <div class="metric-value cyan">16</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Vector Store</div>
        <div class="metric-value violet">ChromaDB</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">Retrieval Mode</div>
        <div class="metric-value success">Agentic</div>
    </div>
    <div class="metric-card">
        <div class="metric-label">LLM</div>
        <div class="metric-value" style="color: var(--accent-blue);">Gemini</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ======================================================
# QUERY CARD
# ======================================================
st.markdown(
    """
<div class="query-card">
    <div class="query-label">⬡ Query Interface</div>
</div>
""",
    unsafe_allow_html=True,
)

col1, col2 = st.columns([5, 1])

with col1:
    query = st.text_input(
        label="query_input",
        placeholder="e.g. What is the PTO carryover policy for senior employees?",
        label_visibility="collapsed",
    )

with col2:
    ask_clicked = st.button("Ask →", use_container_width=True)

# Example chips (visual only — users can manually type these)
st.markdown(
    """
<div class="examples-section">
    <div class="examples-label">Try asking</div>
    <span class="example-chip">What is the parental leave policy?</span>
    <span class="example-chip">How do I report a security incident?</span>
    <span class="example-chip">What AI tools are approved?</span>
    <span class="example-chip">Explain the deployment process</span>
    <span class="example-chip">What is the P1 SLA for enterprise clients?</span>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# PROCESS QUERY
# ======================================================
if ask_clicked:
    if query.strip():
        with st.spinner("Running agentic retrieval pipeline..."):
            result = app.invoke({"query": query})
            answer = result["final_answer"]

        st.markdown(
            f"""
        <div class="response-wrapper">
            <div class="response-header">
                <div class="response-icon"></div>
                <div>
                    <div class="response-title">Agent Response</div>
                    <div class="response-subtitle">Retrieved · Graded · Synthesized</div>
                </div>
            </div>
            <div class="response-body">
                {answer.replace(chr(10), "<br>")}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    else:
        st.warning("Please enter a question before submitting.")
