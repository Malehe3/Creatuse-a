import streamlit as st
from PIL import Image
from streamlit_webrtc import webrtc_streamer
import av
import speech_recognition as sr

st.title("¡Aprende Lenguaje de Señas Colombiano!")

st.write("""
### Básico: Tu Señal de Identificación

En esta sección, puedes crear tu propia señal de identificación personalizada. 
En la comunidad de personas sordas, la presentación de los nombres se realiza de manera única y significativa a través del lenguaje de señas. 
Este proceso no solo implica deletrear el nombre con el alfabeto manual, sino también, en muchas ocasiones, incluir un "nombre en señas". 
Este nombre en señas, va más allá de la mera identificación, es en un reflejo de la identidad y la conexión social dentro de la comunidad.
""")

# Video explicativo
st.write("""
Mira este video para conocer más detalles sobre la señal de identificación.
""")
video_url = "https://www.youtube.com/watch?v=sGg6p03wADw" 
st.video(video_url)

st.write("""
## ¡Ponlo en Práctica!
Captura una característica distintiva, ya sea física, de personalidad o relacionada con una experiencia memorable y crea tu propia seña:
""")

class VideoProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.capture_frame = None

    def recv(self, frame):
        image = frame.to_image()
        self.capture_frame = image

        with self.mic as source:
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language='es-ES')
                if "foto" in text.lower():
                    st.session_state.captured_image = image
            except sr.UnknownValueError:
                pass
        
        return av.VideoFrame.from_image(image)

webrtc_ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
)

if "captured_image" in st.session_state:
    st.image(st.session_state.captured_image, caption="Tu Señal de Identificación")
    
    st.download_button(
        label="Descargar",
        data=st.session_state.captured_image.tobytes(),
        file_name="señal_identificacion.jpg",
        mime="image/jpeg"
    )

st.write("""
### ¡Comparte tu Señal!
Una vez que hayas creado tu señal de identificación, compártela con tus amigos y familiares para que puedan reconocerte fácilmente en la comunidad.
""")

