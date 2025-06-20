import whisper
stt_model = whisper.load_model("base")

def transcribe_audio(audio_path: str) -> str:
    result = stt_model.transcribe(audio_path)
    return result["text"]