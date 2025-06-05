import os
import requests
from glob import glob
from TTS.api import TTS

SUPABASE_VOICE_DIR = "https://rmhgbdxpoczxowtpnqct.supabase.co/storage/v1/object/public/avatar/voz/anonymous/"
LOCAL_AUDIO_DIR = "/tmp/voice_samples/"
EMBEDDING_OUTPUT = "/data/voice/anonymous/embedding.wav"

# 1. Descarga todos los audios de Supabase
def list_supabase_files():
    # Aquí deberías usar la API de Supabase para listar los archivos, pero para ejemplo, lista manual
    # Si tienes la API key, puedes hacer una petición a /object/list
    # Por ahora, asume que tienes una lista de nombres
    return ["voice1.wav", "voice2.wav"]  # Reemplaza por la lógica real

def download_voices():
    os.makedirs(LOCAL_AUDIO_DIR, exist_ok=True)
    files = list_supabase_files()
    for fname in files:
        url = SUPABASE_VOICE_DIR + fname
        local_path = os.path.join(LOCAL_AUDIO_DIR, fname)
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return [os.path.join(LOCAL_AUDIO_DIR, f) for f in files]

# 2. Genera el embedding/modelo de voz con Coqui TTS
def create_embedding(audio_files, output_path):
    tts_model = os.getenv("COQUI_TTS_MODEL", "tts_models/multilingual/multi-dataset/xtts_v2")
    tts = TTS(tts_model)
    # XTTS v2 permite crear un speaker embedding a partir de varios audios
    tts.create_speaker_embedding(audio_files, output_path)

if __name__ == "__main__":
    audio_files = download_voices()
    create_embedding(audio_files, EMBEDDING_OUTPUT)
    print(f"Embedding/modelo de voz guardado en: {EMBEDDING_OUTPUT}") 