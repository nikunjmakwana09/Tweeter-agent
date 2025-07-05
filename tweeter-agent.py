# this is reflect agent that can generate tweets based on user input
# it uses the Google Gemini API to generate tweets

from dotenv import load_dotenv
load_dotenv()  # this loads environment variables from .env

import os
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise EnvironmentError("API key not found. Please set API_KEY in your environment.")

import google.generativeai as genai

genai.configure(api_key=API_KEY) # type: ignore

model = genai.GenerativeModel('models/gemini-1.5-flash') # type: ignore

def tweet_generator(prompt_text: str) -> str:
    tweet_prompt = (
    "You are a very talented social media assistant. "
    "Write a tweet (280 characters max) based on this prompt: "
    f"'{prompt_text}'. "
    "Keep it short, creative, and use hashtags."
)
    try:
        response = model.generate_content(tweet_prompt)
        tweet = response.text.strip()
        if len(tweet) > 280:
                tweet = tweet[:277] + "..."
        return tweet
    except Exception as e:
        return f"Error generating tweet: {e}"

def main():
    print("=== 🚀 Tweet Generator using Gemini 1.5 Flash ===\n")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("Enter a prompt for the tweet: ").strip()
        if prompt.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        if not prompt:
            print("⚠️ Prompt cannot be empty. Try again.\n")
            continue

        tweet = tweet_generator(prompt)
        print(f"\n✅ Generated Tweet:\n{tweet}\n")

if __name__ == "__main__":
    main()