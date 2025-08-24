# UNWORTHY EXPERIMENTAL CODE - DO NOT USE

import pyautogui
import pyperclip
import time
from client_1 import bot

# --- Helper function to clean last chat ---
def get_last_message(copied_text: str) -> str:
    """
    Extracts the last message content (without timestamp or sender name).
    Returns (sender_name, message_content).
    """
    lines = copied_text.strip().split("\n")
    last_line = lines[-1] if lines else ""

    # Format: [timestamp] Sender: Message
    if "] " in last_line:
        try:
            meta, content = last_line.split("] ", 1)
            if ": " in content:
                sender, message = content.split(": ", 1)
                return sender.strip(), message.strip()
            else:
                return "Unknown", content.strip()
        except:
            return "Unknown", last_line.strip()
    else:
        return "Unknown", last_line.strip()

# --- Main continuous loop ---
while True:
    time.sleep(2)  # time to switch to WhatsApp Web if needed

    # Step 1: Click chat window to focus
    pyautogui.click(1325, 1047) # To be adjusted for every env
    time.sleep(1)

    # Step 2: Move to starting point of text (inside message)
    pyautogui.moveTo(730, 121) # Adjust for env

    # Step 3: Double click to ensure text selection
    pyautogui.doubleClick()
    time.sleep(0)

    # Step 4: Hold and drag across message
    pyautogui.dragTo(791, 1009, duration=1, button='left') # Adjust
    time.sleep(1)

    # Step 5: Copy and release
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(689, 184)
    time.sleep(1)

    # Step 6: Paste into variable
    copied_text = pyperclip.paste()
    print("Captured text:\n", copied_text)

    # Step 7: Extract last message
    sender, last_message = get_last_message(copied_text)
    print(f"\nLast message from: {sender}\nMessage: {last_message}")

    # Step 8: Only reply if sender is not Aman
    if "Aman" not in sender:
        reply = bot(last_message)

        # Step 9: Click chat box and paste reply
        pyautogui.click(809, 974)  # Chat box coords
        pyperclip.copy(reply)
        pyautogui.hotkey("ctrl", "v")

        # Step 10: Wait before sending
        time.sleep(5)

        # Step 11: Click send button
        pyautogui.click(1870, 971)  # Send button coords
    else:
        print("No reply needed (last message was by Aman).")

    # --- Small delay before checking again ---
    time.sleep(5)
