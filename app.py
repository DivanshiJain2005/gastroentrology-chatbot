# also supports uploading docs

import streamlit as st
import openai
from typing import List, Dict
import fitz 

# Initialize OpenAI API (make sure to set your API key)
openai.api_key = "your_openai_api_key"

# Define your symptom list and possible diagnoses
SYMPTOMS: List[str] = [
    "Abdominal pain", "Nausea", "Vomiting", "Diarrhea", "Constipation",
    "Bloating", "Heartburn", "Loss of appetite", "Weight loss", "Fatigue"
]

POSSIBLE_DIAGNOSES: Dict[str, List[str]] = {
    "Gastroesophageal Reflux Disease (GERD)": ["Heartburn", "Chest pain", "Difficulty swallowing"],
    "Peptic Ulcer Disease": ["Abdominal pain", "Nausea", "Vomiting"],
    "Irritable Bowel Syndrome (IBS)": ["Abdominal pain", "Bloating", "Change in bowel habits"],
    "Inflammatory Bowel Disease (IBD)": ["Abdominal pain", "Diarrhea", "Weight loss", "Fatigue"],
    "Gastroenteritis": ["Nausea", "Vomiting", "Diarrhea", "Abdominal cramps"],
}

def get_ai_response(message: str, conversation_history: List[Dict[str, str]]) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are an expert gastroenterologist AI assistant. Your task is to:

1. Analyze the symptoms provided by the user and predict potential gastroenterological diseases.
2. If needed, ask for additional details such as symptom duration, severity, and associated symptoms to refine your diagnosis.
3. Provide a detailed explanation of the potential disease(s) based on the symptoms.
4. Suggest temporary relief measures for the symptoms.
5. Recommend appropriate over-the-counter medications or when to seek professional medical help.

Important guidelines:
- Always ask about the symptom duration, severity, and any associated symptoms if not provided.
- Inquire about the patient's medical history and recent diet if relevant to the symptoms.
- Provide a severity assessment for the reported symptoms.
- Offer clear, concise advice for temporary relief of symptoms.
- When recommending medications, always advise the patient to consult with a healthcare provider before taking any new medication.
- Include a disclaimer that your advice is not a substitute for professional medical diagnosis or treatment.

Conduct the conversation in a friendly, empathetic manner while maintaining professionalism. Remember, you are an amazing doctor in the field of gastroenterology, capable of providing insightful diagnoses based on the symptoms presented."""},
                *conversation_history,
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error in getting AI response: {str(e)}")
        return "I'm sorry, but I encountered an error. Please try again later."

def parse_medical_report(uploaded_file):
    """Parse the uploaded medical report PDF and extract text."""
    if uploaded_file is not None:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    return ""

def main():
    st.title("Gastroenterology Chatbot")
    st.write("Welcome! I'm here to help you with your gastroenterology-related concerns. Please describe your symptoms or upload your medical report.")

    # Initialize session state for conversation history
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    # File uploader for medical reports
    uploaded_file = st.file_uploader("Upload your medical report (PDF)", type="pdf")

    # Parse the uploaded medical report if any
    report_text = parse_medical_report(uploaded_file)

    # Display parsed report text (if available)
    if report_text:
        st.write("Parsed Medical Report:")
        st.text_area("Report Content", report_text, height=200)

    # Display conversation history
    for message in st.session_state.conversation:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Get user input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Add user message to conversation
        st.session_state.conversation.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Include report text in the AI response if available
        full_message = f"{user_input}\n\nMedical Report Details: {report_text}" if report_text else user_input

        # Get AI response
        ai_response = get_ai_response(full_message, st.session_state.conversation)

        # Add AI response to conversation
        st.session_state.conversation.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"):
            st.write(ai_response)

if __name__ == "__main__":
    main()
