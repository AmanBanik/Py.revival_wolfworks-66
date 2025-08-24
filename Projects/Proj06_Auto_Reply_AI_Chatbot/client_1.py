# client.py
import google.generativeai as genai

# Configure Gemini with your API key
genai.configure(api_key="#Add your Gemini Api key#")

# Initialize model (choose based on speed/quality)
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

def bot(user_input: str) -> str:
    """
    Takes last sender chat text and returns a Gemini-generated reply
    based on Aman's persona.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are a person named Aman who speaks Bengali, Hindi, and English. "
                "You are from India and are a coder. You analyze chat history and respond like Aman, "
                "but focus only on the most recent message from the sender."
                "Reply directly in first person, without prefixing your name."
            )
        },
        {"role": "user", "content": user_input.strip()}
    ]

    # Build a simplified prompt (Gemini doesn’t support messages directly)
    prompt = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in messages])

    try:
        response = model.generate_content(prompt)
        generated_reply = response.text.strip() if response.text else "[No reply generated]"
    except Exception as e:
        generated_reply = f"[Error generating reply: {str(e)}]"

    # Print to terminal
    print("\nBot Reply:\n", generated_reply)

    return generated_reply
