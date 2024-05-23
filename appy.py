import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings
import speech_recognition as sr
import tempfile
import os
import time

# Configuración de WebRTC
WEBRTC_CLIENT_SETTINGS = ClientSettings(
    media_stream_constraints={
        "audio": True,
        "video": False,
    },
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
)

def recognize_speech_from_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='es-ES')
            return text.lower()
        except sr.UnknownValueError:
            return "No se ha entendido lo que has dicho"
        except sr.RequestError as e:
            return f"Error al realizar la solicitud de reconocimiento de voz; {e}"

def main():
    st.title("Detector de palabra")
    st.write("Presiona el botón para grabar y hablar")

    webrtc_ctx = webrtc_streamer(
        key="example", mode=WebRtcMode.SENDRECV, client_settings=WEBRTC_CLIENT_SETTINGS
    )

    if st.button("Start"):
        if webrtc_ctx.audio_receiver:
            st.write("Grabando... di 'foto'")
            time.sleep(3)  # Graba durante 3 segundos
            audio_frames = webrtc_ctx.audio_receiver.get_frames(timeout=1)
            if len(audio_frames) > 0:
                audio_data = b"".join([af.to_ndarray().tobytes() for af in audio_frames])

                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as audio_file:
                    audio_file.write(audio_data)
                    audio_file_path = audio_file.name

                spoken_text = recognize_speech_from_audio(audio_file_path)
                os.remove(audio_file_path)
                st.write(f"Has dicho: {spoken_text}")
                if "foto" in spoken_text:
                    st.write("Correcto")
                else:
                    st.write("Incorrecto")

if __name__ == "__main__":
    main()
