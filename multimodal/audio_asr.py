import whisper
import tempfile
import os

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    """
    Converts audio to text using Whisper
    """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        temp_path = tmp.name

    try:
        result = model.transcribe(temp_path)

        text = result.get("text", "").strip()

        confidence = 0.9 if len(text) > 5 else 0.4

        return {
            "text": text,
            "confidence": confidence
        }
    finally:
        os.remove(temp_path)
