# Aquí irá la lógica de procesamiento de audio (STT) 

from faster_whisper import WhisperModel
import numpy as np
import tempfile

model = WhisperModel("base")

def transcribe_audio(audio_path: str) -> str:
    segments, info = model.transcribe(audio_path)
    return " ".join([segment.text for segment in segments])

def transcribe_audio_bytes(audio_bytes: bytes) -> str:
    # Guarda los bytes en un archivo temporal y transcribe
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=True) as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        return transcribe_audio(tmp.name) 