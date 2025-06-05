# Aquí irá la lógica de procesamiento de audio (STT) 

import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result["text"] 