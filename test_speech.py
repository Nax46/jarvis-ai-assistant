from voice.listener import Listener

Listener.record()

text = Listener.transcribe()

print("\nYou Said:")
print(text)