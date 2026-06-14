from brain.gemini_client import GeminiClient

ai = GeminiClient()

question = input("Ask Jarvis: ")

response = ai.ask(question)

print("\nJarvis:")
print(response)