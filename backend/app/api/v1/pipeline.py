from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.app.services.audio_service import transcribe_audio
from backend.app.services.agentic_service import ask_llm
from backend.app.services.tts_service import synthesize_voice
from backend.app.services.avatar_service import lipsync_video
import os

router = APIRouter()

SUPABASE_VIDEO_URL = "https://rmhgbdxpoczxowtpnqct.supabase.co/storage/v1/object/public/avatar/video/anonymous/base_video.mp4"
SPEAKER_EMBEDDING_PATH = "/data/voice/anonymous/embedding.wav"  # Ajusta esta ruta según donde guardes el embedding/modelo de voz

# Este endpoint es solo para pruebas directas (no LiveKit)
@router.post("/test")
def pipeline_test(audio: UploadFile = File(...)):
    # Guardar archivo temporal de audio
    audio_path = f"/tmp/{audio.filename}"
    with open(audio_path, "wb") as f:
        f.write(audio.file.read())

    # 1. STT
    text = transcribe_audio(audio_path)
    # 2. LLM
    response = ask_llm(text)
    # 3. TTS (usa el embedding/modelo de voz ya entrenado)
    tts_path = f"/tmp/tts_{audio.filename}.wav"
    synthesize_voice(response, SPEAKER_EMBEDDING_PATH, tts_path)
    # 4. Libsync (descarga el video base desde Supabase y devuelve keypoints)
    lipsync_keypoints = lipsync_video(SUPABASE_VIDEO_URL, tts_path, tts_path + ".mp4")

    return {"text": text, "llm_response": response, "tts_audio": tts_path, "lipsync_keypoints": lipsync_keypoints}

# Aquí iría la integración con LiveKit para recibir y enviar streams en tiempo real.
# Esto requiere un worker o proceso asíncrono que se conecte como participante a la sala,
# reciba el audio, ejecute el pipeline y publique el resultado como un nuevo track o DataTrack. 