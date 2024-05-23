import streamlit as st
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import speech_recognition as sr

def record_audio(duration, fs):
    st.write("Grabando...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype=np.int16)
    sd.wait()  # Esperar a que termine la grabación
    st.write("Grabación completa.")
    return recording, fs

def save_audio(file_path, recording, fs):
    wav.write(file_path, fs, recording)

def recognize_speech_from_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
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

    duration = st.slider("Duración de la grabación (segundos)", 1, 10, 3)
    fs = 44100  # Frecuencia de muestreo

    if st.button("Grabar"):
        recording, fs = record_audio(duration, fs)
        file_path = "recorded_audio.wav"
        save_audio(file_path, recording, fs)
        spoken_text = recognize_speech_from_file(file_path)
        st.write(f"Has dicho: {spoken_text}")
        if "foto" in spoken_text:
            st.write("Correcto")
        else:
            st.write("Incorrecto")

if __name__ == "__main__":
    main()

