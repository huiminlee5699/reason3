import streamlit as st
import time
from openai import OpenAI

def generate_reasoning_steps_for_credibility_task():
    """Generate realistic reasoning steps for the social media credibility evaluation task."""
    return [
        {
            "summary": "Analyzing the post's claims systematically",
            "detail": "I need to evaluate this social media post about green tea and cancer prevention for credibility. Let me break down the claims systematically."
        },
        {
            "summary": "Examining specific statistical claims",
            "detail": "First, I'll examine the specific claims: 1) A peer‑reviewed Stanford study exists, 2) 50,000 participants over 10 years, 3) 87% cancer risk reduction from 3 cups daily, 4) 'Big Pharma doesn't want you to know.'"
        },
        {
            "summary": "Checking methodology plausibility",
            "detail": "Checking the methodology claims: A 10‑year study with 50,000 participants sounds plausible for epidemiological research, but I need to verify if such a study actually exists from Stanford."
        },
        {
            "summary": "Evaluating effect size credibility",
            "detail": "The 87% risk reduction is an extremely high effect size that would be groundbreaking if true. Such dramatic results would typically be widely reported in major medical journals and news outlets."
        },
        {
            "summary": "Identifying misinformation red flags",
            "detail": "Red flags I'm noticing: 1) The 'Big Pharma conspiracy' language, 2) Urgency to 'share before they take it down,' 3) Hashtags like #GreenTeaCure suggest oversimplification, 4) No citation of the actual study."
        },
        {
            "summary": "Comparing with legitimate research",
            "detail": "I should also consider what legitimate research says about green tea and cancer. While some studies suggest modest benefits, the scientific consensus doesn't support such dramatic claims."
        },
        {
            "summary": "Analyzing persuasive language patterns",
            "detail": "The post uses persuasive but unscientific language patterns common in health misinformation: definitive claims ('proves'), conspiracy theories, and emotional appeals."
        },
        {
            "summary": "Final credibility assessment",
            "detail": "Based on my analysis, this appears to be misleading health information that could potentially harm people by promoting false hope or delaying proper medical care."
        }
    ]

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
        border-left: 3px solid #e1e5e9;
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

# ─── OpenAI Client ────────────────────────────────────────────────────────────
openai_api_key = st.secrets["openai_api_key"]
client = OpenAI(api_key=openai_api_key)

# ─── Session State Init ───────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_reasoning_history" not in st.session_state:
    st.session_state.current_reasoning_history = []
if "reasoning_step_counter" not in st.session_state:
    st.session_state.reasoning_step_counter = 0

# ─── Helper Functions ─────────────────────────────────────────────────────────
def render_interactive_reasoning_live(reasoning_steps, container):
    """Show reasoning buckets appearing one by one, with previous ones disappearing."""
    
    # Create grouped reasoning buckets
    reasoning_buckets = [
        {
            "summary": "Initial Analysis & Claims Examination",
            "steps": reasoning_steps[:3]  # First 3 steps
        },
        {
            "summary": "Credibility Assessment & Red Flags", 
            "steps": reasoning_steps[3:6]  # Next 3 steps
        },
        {
            "summary": "Final Evaluation & Conclusion",
            "steps": reasoning_steps[6:]   # Remaining steps
        }
    ]
    
    for bucket in reasoning_buckets:
        # Clear container and show current bucket
        with container.container():
            # Show header
            st.markdown(f"""
            <div class="thought-process-header">
                <span class="thought-process-title">Thinking...</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Show current reasoning bucket with dropdown
            with st.expander(bucket["summary"], expanded=False):
                for i, step in enumerate(bucket["steps"], start=1):
                    st.markdown(f'<div class="reasoning-step"><strong>Step {i}:</strong> {step["detail"]}</div>', unsafe_allow_html=True)
        
        time.sleep(2.0)  # Delay before next bucket

def render_interactive_reasoning_final(reasoning_steps, thinking_time):
    """Render the final interactive reasoning with first bucket only."""
    
    # Header with final timing
    st.markdown(f"""
    <div class="thought-process-header">
        <span class="thought-process-title">Thought Process</span>
        <span class="thinking-time">{thinking_time}s</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Show only the first bucket summary with all reasoning steps inside
    with st.expander("Initial Analysis & Claims Examination", expanded=False):
        for i, step in enumerate(reasoning_steps, start=1):
            st.markdown(f'<div class="reasoning-step"><strong>Step {i}:</strong> {step["detail"]}</div>', unsafe_allow_html=True)

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

    # Generate reasoning steps
    reasoning_steps = generate_reasoning_steps_for_credibility_task()
    
    # PHASE 1: Show reasoning process in real-time
    start_time = time.time()
    thinking_container = st.empty()
    
    render_interactive_reasoning_live(reasoning_steps, thinking_container)
    
    thinking_duration = int(time.time() - start_time)
    
    # Clear the live thinking display
    thinking_container.empty()
    
    # PHASE 2: Generate actual GPT response
    full_response = ""
    response_placeholder = st.empty()
    
    try:
        
        stream = client.chat.completions.create(
            model="o1-mini",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        )
        
        # Clear the generating status
        
        # Stream the response
        for chunk in stream:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                response_placeholder.markdown(f'<div class="assistant-message">{full_response}</div>', unsafe_allow_html=True)

        # Store assistant message with reasoning info
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response,
            "reasoning": reasoning_steps,
            "thinking_time": thinking_duration
        })

        # Rerun to show final reasoning interface above the response
        st.rerun()

    except Exception as e:
        st.error(f"Error generating response: {e}")
