# client.py

import google.generativeai as genai
import os

API_KEY = "#ADD YOUR GeminiApi key#"

# Configure the Gemini API client with the API key
genai.configure(api_key=API_KEY)

# Initialize a chat session for the Gemini model.
chat = genai.GenerativeModel("gemini-2.5-flash-preview-05-20").start_chat(history=[])

# The persona prompt is sent first, followed by the user's message.
messages = [
    {
        "role": "user", 
        "parts": ["A virtual assistant like Alexa and Google Cloud. This assistant obtains data via searching and is an expert in coding, math, and other subjects. Also make responses shorter and brief whenever explanation is not necessary"]
    }
]

# Send the persona to initialize the assistant
chat.send_message(messages[0]["parts"][0])

# Function to send a message to Gemini and save response to file
def send_and_save(user_input):
    try:
        response = chat.send_message(user_input)

        file_path = r"C:\\DevField\\Python\\Py.revival\\Projects\\Proj05_JARVIS_Voice_Activated_VA\\Chat_Hist.txt"

        with open(file_path, "a") as f:
            f.write(f"User: {user_input}\n")
            f.write(f"Assistant: {response.text}\n\n")

        print(f"\nConversation appended to {file_path}")

        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, I am having trouble connecting to my service. Please try again later."
