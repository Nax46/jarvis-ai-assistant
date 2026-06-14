import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


class Listener:

    @staticmethod
    def record():

        duration = 5
        sample_rate = 16000

        print("Listening...")

        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(
            "recording.wav",
            sample_rate,
            audio
        )

        print("Recording Saved")

    @staticmethod
    def transcribe():

        model = WhisperModel(
            "base",
            compute_type="int8"
        )

        segments, info = model.transcribe(
            "recording.wav"
        )

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()