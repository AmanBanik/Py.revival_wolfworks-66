import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os

# ------------------ CONFIG ------------------
YOUR_NAME = "Aman Banik"   # Your name in WhatsApp
API_KEY = "#Add your Gemini Api key#"  # replace with your Gemini key
MODEL_NAME = "gemini-2.5-flash-preview-05-20"

# Coordinates (adjust if needed for your system)
CHROME_ICON = (1322,1045)
CHAT_START = (727,130)
CHAT_END = (754,1012)
CHAT_CLICK = (1872,725)
TEXTBOX = (828,974)

# ------------------ INIT ------------------
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

def is_last_message_from_me(chat_log, sender_name=YOUR_NAME):
    """Check if last copied message belongs to you"""
    try:
        last_msg = chat_log.strip().split("\n")[-1]  # last line
        return sender_name in last_msg
    except Exception as e:
        print(f"[ERROR-check]: {e}")
        return True  # fail-safe → assume it's yours

def generate_response(chat_history):
    """Call Gemini and return response"""
    try:
        prompt = (
            "You are a person named Aman Banik who speaks Bengali, Hindi, English. "
            "You are from India and a coder. You analyze chat history "
            "Respond wisely, whenever needed for serious questions, "
            "and roast people in a funny way. Output should ONLY be the next chat message. "
            "Reply directly in first person, without prefixing your name."
        )
        response = model.generate_content(f"{prompt}\n\nChat:\n{chat_history}")
        return response.text.strip()
    except Exception as e:
        print(f"[ERROR-gemini]: {e}")
        return None

def main():
    # Open Chrome
    pyautogui.click(*CHROME_ICON)
    time.sleep(1)

    while True:
        try:
            time.sleep(5)

            # Select chat area
            pyautogui.moveTo(*CHAT_START)
            pyautogui.dragTo(*CHAT_END, duration=2.0, button='left')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)

            # Ensure focus on chat
            pyautogui.click(*CHAT_CLICK)

            # Get copied chat
            chat_history = pyperclip.paste().strip()
            if not chat_history:
                print("[INFO] No chat history copied.")
                continue

            print("\n[CHAT HISTORY]:\n", chat_history[-500:])  # last 500 chars

            # Check last message
            if is_last_message_from_me(chat_history):
                print("[INFO] Last message is yours → skipping reply.")
                continue

            # Generate response
            reply = generate_response(chat_history)
            if not reply:
                continue

            print("[BOT REPLY]:", reply)
            pyperclip.copy(reply)

            # Paste into textbox
            pyautogui.click(*TEXTBOX)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')

        except KeyboardInterrupt:
            print("\n[EXIT] Stopped manually.")
            break
        except Exception as e:
            print(f"[ERROR-loop]: {e}")
            time.sleep(5)  # wait before retry

if __name__ == "__main__":
    main()
