# Aquí irá la lógica de síntesis de voz 
from TTS.api import TTS
import os
import numpy as np

tts_model = os.getenv("COQUI_TTS_MODEL", "tts_models/en/ljspeech/tacotron2-DDC")
tts = TTS(tts_model)

def synthesize_voice(text: str) -> bytes:
    wav = tts.tts(text=text)
    return (wav * 32767).astype("int16").tobytes() 