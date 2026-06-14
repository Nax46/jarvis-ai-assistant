import asyncio
import edge_tts
from playsound3 import playsound


class Speaker:

    @staticmethod
    def speak(text):

        async def generate():
            communicate = edge_tts.Communicate(
                text,
                # voice="en-US-AriaNeural"
                voice="en-IN-NeerjaNeural"
            )

            await communicate.save("temp.mp3")

        asyncio.run(generate())

        playsound("temp.mp3")