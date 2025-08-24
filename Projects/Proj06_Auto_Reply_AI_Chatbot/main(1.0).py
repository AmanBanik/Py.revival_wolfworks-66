import pyautogui
import pyperclip
import time
from client_1 import bot   # Importing the Gemini bot


time.sleep(2)  # time to switch to WhatsApp Web

# Step 1: Click chat window to focus
pyautogui.click(1325, 1047) # To be adjusted for every new env
time.sleep(1)

# Step 2: Move to starting point of text (inside message)
pyautogui.moveTo(730,121) # To be adjusted for every new env

# Step 3: Double click to ensure text selection is activated
pyautogui.doubleClick()
time.sleep(0) # no delay to ensure double click is registered and no item is being dragged or selected

# Step 4: Hold and drag across message
pyautogui.dragTo(791,1009, duration=1, button='left') # To be adjusted for every new env
time.sleep(1)

# Step 5: Copy and release
pyautogui.hotkey("ctrl", "c")
pyautogui.click(689,184)
time.sleep(1)

# Step 6: Paste into variable
copied_text = pyperclip.paste()
print("Captured text:\n", copied_text)

# Step 7: Send captured text to Gemini bot 
reply = bot(copied_text)

# # Step 8: Click WhatsApp Web again to focus
# pyautogui.click(1325, 1047) # WhatsApp icon
# time.sleep(1)

# Step 9: Click chat box and paste reply
pyautogui.click(809,974)  # <-- Replace with chat box coordinates
pyperclip.copy(reply)
pyautogui.hotkey("ctrl", "v")

# Step 10: Wait before sending
time.sleep(5)

# # Step 11: Click send button
# pyautogui.click(1870,971)  # <-- Replace with send button coordinates
