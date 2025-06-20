from gtts import gTTS

def synthesize_speech(text: str, output_path: str, lang="fr"):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)