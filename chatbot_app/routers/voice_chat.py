from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import uuid
import os
from services.stt_service import transcribe_audio
from services.gpt_service import generate_response
from services.tts_service import synthesize_speech

router = APIRouter()

@router.post("/voice")
async def chatbot_voice(file: UploadFile = File(...)):
    temp_audio = f"temp_{uuid.uuid4().hex}.mp3"
    with open(temp_audio, "wb") as f:
        f.write(await file.read())

    user_text = transcribe_audio(temp_audio)
    response_text = generate_response(user_text)

    audio_output = f"response_{uuid.uuid4().hex}.mp3"
    synthesize_speech(response_text, audio_output)

    os.remove(temp_audio)
    return FileResponse(audio_output, media_type="audio/mpeg", filename="response.mp3")