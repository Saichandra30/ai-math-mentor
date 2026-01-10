import streamlit as st
import time

from agents.parser_agent import parser_agent
from agents.solver_agent import solver_agent
from agents.verifier_agent import verifier_agent
from agents.intent_router import intent_router_agent
from agents.explainer_agent import explainer_agent

from multimodal.text_input import get_text_input
from multimodal.image_ocr import extract_text_from_image
from multimodal.audio_asr import transcribe_audio

from rag.retriever import retrieve_context
from hitl.hitl_manager import check_confidence
from memory.memory_store import save_experience, find_similar_problem

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Math Mentor", layout="wide")

st.title("📘 AI Math Mentor")
st.subheader("Multimodal | RAG | Agents | HITL")

# ---------------- SESSION STATE INIT ----------------
if "extracted_data" not in st.session_state:
    st.session_state.extracted_data = None
if "parsed_output" not in st.session_state:
    st.session_state.parsed_output = None
if "solver_output" not in st.session_state:
    st.session_state.solver_output = None
if "verified" not in st.session_state:
    st.session_state.verified = False

# ---------------- SIDEBAR: MEMORY ----------------
st.sidebar.title("🧠 Memory Bank")
st.sidebar.info("System learns from your verified solutions.")


# ---------------- INPUT MODE ----------------
input_mode = st.selectbox("Choose input mode", ["Text", "Image", "Audio"])

# ---------------- TEXT ----------------
if input_mode == "Text":
    user_text = st.text_area("Enter math problem")
    if st.button("Process Text"):
        st.session_state.extracted_data = get_text_input(user_text)
        st.session_state.parsed_output = None
        st.session_state.solver_output = None

# ---------------- IMAGE ----------------
elif input_mode == "Image":
    image_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
    if image_file:
        st.image(image_file, caption="Uploaded Image", width=400)
        if st.button("Extract Text"):
            with st.spinner("Running OCR..."):
                st.session_state.extracted_data = extract_text_from_image(image_file)
                st.session_state.parsed_output = None
                st.session_state.solver_output = None

# ---------------- AUDIO ----------------
elif input_mode == "Audio":
    audio_file = st.file_uploader("Upload audio", type=["wav", "mp3"])
    if audio_file:
        st.audio(audio_file)
        if st.button("Transcribe Audio"):
            with st.spinner("Transcribing..."):
                st.session_state.extracted_data = transcribe_audio(audio_file)
                st.session_state.parsed_output = None
                st.session_state.solver_output = None

# ---------------- PREVIEW & EDIT ----------------
if st.session_state.extracted_data:
    st.markdown("### 🔍 Extracted Text (Editable)")
    
    extracted = st.session_state.extracted_data
    edited_text = st.text_area("Review / Edit", value=extracted["text"] or "")
    
    st.progress(min(extracted.get("confidence", 0.0), 1.0))
    if extracted.get("confidence", 0.0) < 0.6:
        st.warning("⚠️ Low confidence extraction - Please verify text above.")

    # ---------------- 1. PARSER AGENT ----------------
    if st.button("Step 1: Parse & Plan"):
        with st.spinner("Analyzing problem structure..."):
            parsed = parser_agent(edited_text)
            st.session_state.parsed_output = parsed
            st.session_state.solver_output = None

# ---------------- PIPELINE FLOW ----------------
if st.session_state.parsed_output:
    parsed = st.session_state.parsed_output
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧠 Parser Output")
        st.json(parsed)
        
        # Intent Router Check
        intent = intent_router_agent(parsed["problem_text"])
        st.markdown(f"**Detected Topic:** {intent.get('topic', 'Unknown')}")
        
    with col2:
        st.markdown("### 📚 Memory & RAG")
        
        # Check Memory First
        similar_prob = find_similar_problem(parsed["problem_text"])
        if similar_prob:
            st.success("✨ Found similar solved problem in Memory!")
            with st.expander("View Similar Solution"):
                st.write(similar_prob)
        
        # RAG Retrieval
        retrieved_chunks = retrieve_context(parsed["problem_text"])
        if not retrieved_chunks:
            st.warning("No knowledge base documents found.")
        else:
            with st.expander(f"View {len(retrieved_chunks)} Source Docs"):
                for i, c in enumerate(retrieved_chunks):
                    st.write(f"**Doc {i+1}:** {c[:200]}...")

    # HITL Guardrail for Ambiguity
    if parsed.get("needs_clarification"):
        st.error(f"🛑 Clarification Needed: {parsed['clarification_question']}")
        st.stop()

    # ---------------- 2. SOLVER AGENT ----------------
    if st.button("Step 2: Solve Problem"):
        with st.spinner("Solving with RAG + Agents..."):
            st.session_state.solver_output = solver_agent(
                parsed["problem_text"], 
                retrieved_chunks,
                intent.get("topic")
            )

# ---------------- SOLUTION DISPLAY ----------------
if st.session_state.solver_output:
    sol = st.session_state.solver_output
    st.markdown("---")
    st.markdown("### 🧮 Solution")
    
    # HITL Confidence Check
    hitl_status = check_confidence(sol)
    
    if hitl_status["trigger"]:
        st.warning(f"⚠️ HITL Triggered: {hitl_status['reason']}")
    else:
        st.success(f"Confidence: {sol['confidence']}")

    st.markdown(f"**Final Answer:** `{sol['solution']}`")
    
    with st.expander("Show Steps"):
        for s in sol.get("steps", []):
            st.write(f"- {s}")

    # ---------------- 3. EXPLAINER & VERIFIER ----------------
    st.markdown("### 👩‍🏫 Tutor Explanation")
    explanation = explainer_agent(
        st.session_state.parsed_output["problem_text"],
        sol.get("steps", []),
        sol["solution"]
    )
    st.info(explanation)
    
    # ---------------- FEEDBACK LOOP ----------------
    st.markdown("---")
    st.markdown("### ✅ Verification & Learning")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("👍 Correct (Save to Memory)"):
            save_experience(
                st.session_state.parsed_output["problem_text"],
                sol["solution"],
                True
            )
            st.success("Saved to memory! System is smarter now.")
            
    with c2:
        if st.button("👎 Incorrect (Flag)"):
            st.error("Flagged for review. This will help tune the agents.")
