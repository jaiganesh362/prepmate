# PrepMate — AI Interview Preparation Chatbot

An intelligent AI-powered interview assistant built using ChatGroq Llama-3.1, Streamlit, and metadata-driven prompting.  
PrepMate helps job seekers practice mock interviews, analyze job descriptions, and get real-time feedback — all inside a clean ChatGPT-style interface.

<img width="1919" height="999" alt="Screenshot 2025-11-21 162809" src="https://github.com/user-attachments/assets/68981712-e482-414d-ac65-c160ce0f90e3" />

---

## Features

### Interview Preparation Tools

- Mock Interview Mode – Ask “start mock interview” and get role-specific interview questions
- JD-Aware Questioning – Paste any job description for tailored questions
- Feedback Evaluator – Get detailed feedback on your answers
- Role-Based Metadata – Choose your target role for customized interview flow

### Tech Stack

- Streamlit (Frontend UI)
- Groq Llama-3.1 (LLM Backend)
- python-dotenv (API key handling)
- Custom Metadata Logic
- CSS (UI Styling)

## Setup & Run Locally

### 1. Clone the repository:

```bash
git clone https://github.com/jaiganesh362/PrepMate.git
cd PrepMate
```

### 2. Create `.env` file:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Install dependencies:

```bash
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
```

### 4. Run app:
```bash
   python -m streamlit run main.py
```

## Demo Video








