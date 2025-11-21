import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# --- CONFIG ---
st.set_page_config(page_title="Interview Prep Bot", page_icon=":robot_face:", layout="wide")

# --- GROQ SETUP ---
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# --- UI METADATA ---
st.sidebar.title("Interview Metadata")
role = st.sidebar.selectbox("Select Role", ["Software Engineer", "Data Scientist", "Cloud Engineer","Full Stack Developer","AI Engineer","Data Engineer","HR Manager", "Product Manager"])
jd_text = st.sidebar.text_area("Paste Job Description Here", height=120)
st.sidebar.markdown("Customize your metadata-driven interview experience!")

st.title("PrepMate")
st.caption("Interview Preparation Chatbot Powered by ChatGroq LLM and Streamlit")

# Initialize chat history in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": f"Welcome to your interview preparation bot, Paste a job description and start chatting."}
    ]

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Get user input ---
if prompt := st.chat_input("Ask me an interview question, or say 'start mock interview'"):
    # Store user prompt in chat history with metadata
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Prepare contextual system prompt using metadata
    sys_prompt = (
        f"You are an expert interviewer preparing candidates for the role of {role}. "
        f"The job description is: {jd_text[:500]}. "
        "Ask technical, HR, and behavioral questions, give feedback on answers, and guide the candidate to improve."
    )

    # Send messages to Groq LLM (conversation context)
    messages = [
        {"role": "system", "content": sys_prompt},
    ] + [
        {"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history
    ]

    # Call Groq API for chat completion
    try:
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",    # Replace with 'llama-3.1-8b-instant' or preferred Groq-hosted model
            max_tokens=1000,
        )
        llm_reply = response.choices[0].message.content
    except Exception as e:
        llm_reply = f"Error from LLM: {e}"

    # Append assistant reply to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": llm_reply})
    with st.chat_message("assistant"):
        st.markdown(llm_reply)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #EDF6F9;
    }
    .sidebar .sidebar-content {
        background-color: #33AACC;
        color: #fff;
    }
    .st-bd {
        background-color: #A7C7E7;
    }
    </style>
    """, unsafe_allow_html=True
)
