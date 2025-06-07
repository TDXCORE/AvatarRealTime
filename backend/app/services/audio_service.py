# Aquí irá la lógica de procesamiento de audio (STT) 

import whisper
import numpy as np
import tempfile

model = whisper.load_model("base")

def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result["text"]

def transcribe_audio_bytes(audio_bytes: bytes) -> str:
    # Guarda los bytes en un archivo temporal y transcribe
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=True) as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        return transcribe_audio(tmp.name) 