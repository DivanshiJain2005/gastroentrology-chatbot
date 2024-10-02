# Gastroenterology Chatbot

A Streamlit application that serves as a gastroenterology chatbot, allowing users to describe symptoms and upload medical reports for analysis and potential diagnoses.

## Features

- **Symptom Analysis**: Analyze user-described symptoms to suggest possible gastroenterological diseases.
- **Medical Report Upload**: Parse uploaded PDF medical reports to incorporate information into responses.
- **Conversational Interface**: Maintain a conversational history for an interactive experience.

## Requirements

- Python 3.7 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key:
   Open `app.py` and replace the following line with your actual API key:
   ```python
   openai.api_key = "your_openai_api_key"
   ```

## Running the Application

Start the Streamlit application:
```bash
streamlit run app.py
```

Access the chatbot at [http://localhost:8501](http://localhost:8501).

## Usage

1. **Describe Symptoms**: Enter your symptoms in the chat input box.
2. **Upload Medical Reports**: Use the file uploader to submit medical reports (PDF format).
3. **Receive Responses**: Get potential diagnoses and recommendations based on your input and uploaded reports.

## Disclaimer

This application is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified health provider regarding any medical conditions or concerns.
