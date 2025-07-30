import streamlit as st
import time

def generate_fixed_reasoning_steps():
    """Generate fixed reasoning steps for the social media credibility evaluation task."""
    return [
        {
            "summary": "Analyzing vague claims and missing citations",
            "detail": "\"BREAKING: New peer-reviewed study from Stanford University\" - This is a vague claim without a specific citation. Real scientific breakthroughs would be properly cited.",
            "duration": 1
        },
        {
            "summary": "Evaluating dramatic statistical claims",
            "detail": "\"proves that drinking 3 cups of green tea daily reduces cancer risk by 87%\" - The word \"proves\" is a red flag. Scientific studies rarely \"prove\" anything definitively, especially with such a specific and dramatic reduction percentage. An 87% reduction would be extraordinary and would be front-page news everywhere.",
            "duration": 4
        },
        {
            "summary": "Assessing study methodology claims",
            "detail": "\"The study followed 50,000 participants for 10 years\" - While this sounds like it could be a legitimate study design, without verification it's just numbers that could be made up.",
            "duration": 7
        },
        {
            "summary": "Identifying conspiracy theory elements",
            "detail": "\"Big Pharma doesn't want you to know this!\" - This is a classic conspiracy theory trope used in health misinformation.",
            "duration": 2
        },
        {
            "summary": "Recognizing urgency manipulation tactics",
            "detail": "\"Share before they take it down!\" - This is a common tactic to create urgency and get people to share without fact-checking.",
            "duration": 3
        },
        {
            "summary": "Analyzing misleading hashtags",
            "detail": "Hashtags like \"#GreenTeaCure #CancelCancer\" - These suggest the post is claiming green tea can cure or prevent cancer, which would be a medical claim requiring substantial evidence.",
            "duration": 2
        },
        {
            "summary": "Planning verification research",
            "detail": "I should search for recent Stanford studies on green tea and cancer to see if there's any legitimate research this could be referring to, even if the post is exaggerating the findings.",
            "duration": 6
        }
    ]

def get_fixed_response():
    """Return the fixed response for the credibility evaluation."""
    return """Based on my search of recent Stanford research and the broader scientific literature on green tea and cancer, **this post should be flagged as misleading**. Here's why:

**Red Flags in the Post:**
1. **No verifiable study found**: Despite searching Stanford's recent cancer research, I found no study matching these claims. Stanford researchers are currently working on AI cancer prediction tools, new surgical techniques, and immunotherapies - but nothing about green tea.
2. **Exaggerated language**: The use of "PROVES" is a major red flag. Scientific studies show "mixed" evidence for green tea's cancer-fighting properties, with some studies showing "promising correlations" while others "have found little to no significant impact on cancer incidence" Green tea and cancer | EBSCO Research Starters.
3. **Unrealistic claim**: An 87% reduction in cancer risk would be extraordinary and would be front-page news worldwide. Current research shows "mixed findings" for most cancer types and "mostly null association" for several others Green tea and cancer and cardiometabolic diseases: a review of the current epidemiological evidence | European Journal of Clinical Nutrition.
4. **Conspiracy theory elements**: "Big Pharma doesn't want you to know" and "Share before they take it down" are classic misinformation tactics designed to bypass critical thinking.

**What the Science Actually Shows:**
Research indicates green tea "may be linked to a reduced risk of certain cancers, particularly stomach cancer in populations with high green tea consumption" but "clinical evidence regarding green tea's cancer-fighting properties is mixed" Green tea and cancer | EBSCO Research Starters. For most cancer types, studies show "mixed findings" or "mostly null association" Green tea and cancer and cardiometabolic diseases: a review of the current epidemiological evidence | European Journal of Clinical Nutrition.

**Recommendations for Users:**
1. **Don't share** - This appears to be health misinformation
2. **Check sources** - Look for peer-reviewed studies with proper citations
3. **Be skeptical** of dramatic health claims with conspiracy elements
4. **Consult healthcare providers** for evidence-based health information

**Verdict**: This post is misleading and potentially harmful as it may discourage people from seeking proven cancer prevention methods in favor of unsubstantiated claims."""

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .stApp { background-color: white; }

    .main-title {
        text-align: center; font-size: 28px; font-weight: 400; color: #2d2d2d; margin: 20px 0;
    }

    .user-message {
        background-color: #f0f0f0;
        border-radius: 18px;
        padding: 12px 16px;
        margin: 8px 0 8px auto;
        max-width: 70%;
        font-size: 16px;
        color: #2d2d2d;
        line-height: 1.5;
    }

    .assistant-message {
        background-color: white;
        padding: 12px 0;
        margin: 8px 0;
        max-width: 100%;
        font-size: 16px;
        color: #2d2d2d;
        line-height: 1.6;
    }

    .reasoning-step {
        margin: 12px 16px;
        padding-left: 16px;
        background-color: transparent;
        line-height: 1.5;
        font-size: 16px;
        color: #2d2d2d;
    }

    .thought-process-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: 16px 0 8px 0;
        padding: 0 4px;
    }

    .thought-process-title {
        font-weight: 600;
        font-size: 16px;
        color: #2d2d2d;
    }

    .thinking-time {
        font-size: 14px;
        color: #666;
        font-weight: normal;
    }

    .reasoning-box {
        background-color: #f8f9fa;
        border: 1px solid #e1e5e9;
        border-radius: 8px;
        margin: 6px 0;
        overflow: hidden;
    }

    .reasoning-summary {
        padding: 12px 16px;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: background-color 0.2s;
    }

    .reasoning-summary:hover {
        background-color: #e9ecef;
    }

    .reasoning-summary-text {
        font-size: 15px;
        color: #2d2d2d;
        font-weight: 500;
    }

    .dropdown-arrow {
        color: #666;
        font-size: 12px;
        transition: transform 0.2s;
    }

    .dropdown-arrow.expanded {
        transform: rotate(180deg);
    }

    .reasoning-detail {
        padding: 0 16px 12px 16px;
        border-top: 1px solid #e1e5e9;
        background-color: white;
        font-size: 14px;
        color: #555;
        line-height: 1.5;
    }

    .generating-status {
        display: flex;
        align-items: center;
        gap: 8px;
        margin: 16px 0;
        padding: 12px 16px;
        background-color: #f8f9fa;
        border-radius: 8px;
        border-left: 4px solid #007bff;
    }

    .generating-text {
        font-size: 15px;
        color: #2d2d2d;
        font-weight: 500;
    }

    .spinner {
        width: 16px;
        height: 16px;
        border: 2px solid #e1e5e9;
        border-top: 2px solid #007bff;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    .reasoning-box.fade-in {
        animation: fadeIn 0.4s ease-out;
    }

    /* Hide streamlit expander styling */
    [data-testid="stExpander"] > div:first-child {
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    [data-testid="stExpanderContent"] {
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    [data-testid="stExpanderHeader"] svg {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# ─── Title ────────────────────────────────────────────────────────────────────
st.markdown('<h1 class="main-title">What\'s on the agenda today?</h1>', unsafe_allow_html=True)

# ─── Session State Init ───────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_reasoning_history" not in st.session_state:
    st.session_state.current_reasoning_history = []
if "reasoning_step_counter" not in st.session_state:
    st.session_state.reasoning_step_counter = 0

# ─── Helper Functions ─────────────────────────────────────────────────────────
def render_reasoning_step_live(step, container):
    """Show a single reasoning step appearing in real-time."""
    with container.container():
        # Show header with thinking status
        st.markdown(f"""
        <div class="thought-process-header">
            <span class="thought-process-title">Thinking...</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Show current reasoning step with dropdown
        with st.expander(step["summary"], expanded=False):
            st.markdown(f'<div class="reasoning-step">{step["detail"]}</div>', unsafe_allow_html=True)

def render_interactive_reasoning_live(reasoning_steps, container):
    """Show reasoning steps appearing one by one, each replacing the previous."""
    for step in reasoning_steps:
        # Clear container and show current step
        render_reasoning_step_live(step, container)
        time.sleep(step["duration"])  # Use the duration from each step

def render_interactive_reasoning_final(reasoning_steps, thinking_time):
    """Render the final interactive reasoning with all steps in one expandable section."""
    
    # Header with final timing
    st.markdown(f"""
    <div class="thought-process-header">
        <span class="thought-process-title">Thought Process</span>
        <span class="thinking-time">{thinking_time}s</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Show all reasoning in one expandable section
    with st.expander("Complete reasoning analysis", expanded=False):
        # Combine all reasoning steps into one continuous text
        full_reasoning = """This social media post contains several red flags that suggest it's likely misleading or false. Let me analyze each element:

1. "BREAKING: New peer-reviewed study from Stanford University" - This is a vague claim without a specific citation. Real scientific breakthroughs would be properly cited.

2. "proves that drinking 3 cups of green tea daily reduces cancer risk by 87%" - The word "proves" is a red flag. Scientific studies rarely "prove" anything definitively, especially with such a specific and dramatic reduction percentage. An 87% reduction would be extraordinary and would be front-page news everywhere.

3. "The study followed 50,000 participants for 10 years" - While this sounds like it could be a legitimate study design, without verification it's just numbers that could be made up.

4. "Big Pharma doesn't want you to know this!" - This is a classic conspiracy theory trope used in health misinformation.

5. "Share before they take it down!" - This is a common tactic to create urgency and get people to share without fact-checking.

6. Hashtags like "#GreenTeaCure #CancelCancer" - These suggest the post is claiming green tea can cure or prevent cancer, which would be a medical claim requiring substantial evidence.

I should search for recent Stanford studies on green tea and cancer to see if there's any legitimate research this could be referring to, even if the post is exaggerating the findings."""
        
        st.markdown(f'<div class="reasoning-step">{full_reasoning}</div>', unsafe_allow_html=True)

# ─── Render Chat History ──────────────────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        # Show reasoning if present
        if "reasoning" in msg:
            render_interactive_reasoning_final(msg["reasoning"], msg.get("thinking_time", 0))
        
        st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)

# ─── Chat Input & Processing Flow ─────────────────────────────────────────────
if prompt := st.chat_input("Ask anything..."):
    # Record & display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

    # Reset reasoning history, increment counter
    st.session_state.current_reasoning_history = []
    st.session_state.reasoning_step_counter += 1

    # Generate fixed reasoning steps
    reasoning_steps = generate_fixed_reasoning_steps()
    
    # PHASE 1: Show reasoning process in real-time
    start_time = time.time()
    thinking_container = st.empty()
    
    render_interactive_reasoning_live(reasoning_steps, thinking_container)
    
    thinking_duration = int(time.time() - start_time)
    
    # Clear the live thinking display
    thinking_container.empty()
    
    # PHASE 2: Show fixed response
    fixed_response = get_fixed_response()
    
    # Display the response immediately (no streaming needed since it's fixed)
    st.markdown(f'<div class="assistant-message">{fixed_response}</div>', unsafe_allow_html=True)

    # Store assistant message with reasoning info
    st.session_state.messages.append({
        "role": "assistant",
        "content": fixed_response,
        "reasoning": reasoning_steps,
        "thinking_time": thinking_duration
    })

    # Rerun to show final reasoning interface above the response
    st.rerun()
