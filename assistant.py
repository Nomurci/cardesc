import os
from openai import OpenAI

# the newest OpenAI model is "gpt-5" which was released August 7, 2025.
# do not change this unless explicitly requested by the user
AI_INTEGRATIONS_OPENAI_API_KEY = os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY")
AI_INTEGRATIONS_OPENAI_BASE_URL = os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL")

# This is using Replit's AI Integrations service, which provides OpenAI-compatible API access without requiring your own OpenAI API key.
client = OpenAI(
    api_key=AI_INTEGRATIONS_OPENAI_API_KEY,
    base_url=AI_INTEGRATIONS_OPENAI_BASE_URL
)

def get_ai_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": "You are a helpful banking assistant for the CARDESC application. Help users with their banking and payment queries."},
                {"role": "user", "content": user_input}
            ],
            max_completion_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"

def main():
    print("--- CARDESC AI Assistant ---")
    print("Type 'exit' to return to the main menu.")
    while True:
        user_input = input("\n[AI] You: ").strip()
        if user_input.lower() in ['exit', 'quit', '0']:
            break
        if not user_input:
            continue
        
        print("[AI] Assistant: Thinking...")
        answer = get_ai_response(user_input)
        print(f"[AI] Assistant: {answer}")

if __name__ == "__main__":
    main()
