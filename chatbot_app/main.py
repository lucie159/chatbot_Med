from fastapi import FastAPI
from routers.voice_chat import router as voice_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Chatbot Vocal Médical")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app = FastAPI(title="Chatbot Vocal Médical")
app.include_router(voice_router, prefix="/chatbot", tags=["Vocal Chat"])