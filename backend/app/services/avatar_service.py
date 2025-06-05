# Aquí irá la lógica de lipsync ROI rendering 

import subprocess
import os
import requests
import cv2
import mediapipe as mp
import json

def download_file(url: str, dest_path: str):
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(dest_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

def extract_mouth_keypoints(video_path: str, output_json: str) -> str:
    mp_face_mesh = mp.solutions.face_mesh
    mouth_landmarks = list(range(61, 88))  # Indices de la boca en mediapipe
    cap = cv2.VideoCapture(video_path)
    results = []
    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1) as face_mesh:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res = face_mesh.process(rgb)
            if res.multi_face_landmarks:
                face = res.multi_face_landmarks[0]
                mouth = [{"x": face.landmark[i].x, "y": face.landmark[i].y} for i in mouth_landmarks]
                results.append(mouth)
            else:
                results.append([])
    cap.release()
    with open(output_json, "w") as f:
        json.dump(results, f)
    return output_json

def lipsync_video(video_url: str, audio_path: str, output_path: str, wav2lip_path: str = "./Wav2Lip") -> str:
    # Descargar el video base desde Supabase
    video_path = "/tmp/base_video.mp4"
    download_file(video_url, video_path)
    # Ejecuta el script de Wav2Lip para generar el video con labios sincronizados
    command = [
        "python", os.path.join(wav2lip_path, "inference.py"),
        "--checkpoint_path", os.path.join(wav2lip_path, "checkpoints/wav2lip_gan.pth"),
        "--face", video_path,
        "--audio", audio_path,
        "--outfile", output_path
    ]
    subprocess.run(command, check=True)
    # Extraer keypoints de la boca del video generado
    keypoints_json = output_path + ".keypoints.json"
    extract_mouth_keypoints(output_path, keypoints_json)
    return keypoints_json 