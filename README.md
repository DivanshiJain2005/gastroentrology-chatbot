# Gastroenterology Chatbot

This is a Streamlit application that serves as a gastroenterology chatbot. It allows users to describe their symptoms and upload medical reports in PDF format, which are then parsed to provide relevant medical advice and potential diagnoses based on the user's input.

## Features

- **Symptom Analysis**: Users can describe their symptoms, and the chatbot will analyze them to suggest possible gastroenterological diseases.
- **Medical Report Upload**: Users can upload their medical reports in PDF format. The chatbot will parse the report and incorporate the information into its responses.
- **Conversational Interface**: The chatbot maintains a conversational history for a more interactive experience.

## Requirements

To run this application, you need to have Python 3.7 or higher installed on your machine. You can create a virtual environment and install the necessary dependencies listed in `requirements.txt`.

## Installation

1. Clone the repository or download the files.
   
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

    ```bash
    pip install -r requirements.txt

4. Set your OpenAI API key in the code:

Open the app.py file and replace the line:

    ```bash
    openai.api_key = "your_openai_api_key"
with your actual OpenAI API key.

5. Running the Application
To start the Streamlit application, run the following command:

    ```bash
    streamlit run app.py

Open your web browser and go to http://localhost:8501 to interact with the chatbot.

## Usage

Describe Symptoms: Enter your symptoms in the chat input box.
Upload Medical Reports: Use the file uploader to upload your medical report (PDF format).
Receive Responses: The chatbot will analyze your input and provide potential diagnoses and recommendations based on the symptoms described and the content of the uploaded report.

## Disclaimer
This application is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.