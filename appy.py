import streamlit as st
import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Di algo...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-ES')
        return text.lower()
    except sr.UnknownValueError:
        return "No se ha entendido lo que has dicho"
    except sr.RequestError as e:
        return f"Error al realizar la solicitud de reconocimiento de voz; {e}"

def main():
    st.title("Detector de palabra")
    st.write("Presiona el botón para hablar")

    if st.button("Hablar"):
        spoken_text = recognize_speech()
        if "foto" in spoken_text:
            st.write("Correcto")
        else:
            st.write("Incorrecto")

if __name__ == "__main__":
    main()
