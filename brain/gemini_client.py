import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiClient:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(
            api_key=api_key
        )

    def ask(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
                     You are Jarvis, a voice assistant.

                     Rules:
                     - Reply in 2-3 short sentences.
                     - Be direct.
                     - Speak naturally.
                     - Avoid long paragraphs.

                     User: {prompt}
                    """
        )

        return response.text