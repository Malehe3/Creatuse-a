import streamlit as st
from PIL import Image
import base64
from io import BytesIO

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

# Componente de cámara con botón de voz
st.write("""
### Toma una Foto
Presiona el botón y di la palabra "FOTO" para capturar una imagen.
""")

# HTML y JavaScript para el reconocimiento de voz
stt_html = """
    <script>
    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.continuous = true;
    recognition.lang = 'es-ES';
    recognition.interimResults = false;

    recognition.onresult = function(event) {
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                var transcript = event.results[i][0].transcript.trim();
                if (transcript.toLowerCase() === "foto") {
                    document.getElementById("take-photo-button").click();
                }
            }
        }
    };

    function startRecognition() {
        recognition.start();
    }
    </script>
"""

# HTML para capturar foto usando cámara
camera_html = """
    <div>
        <video id="video" width="640" height="480" autoplay></video>
        <button id="take-photo-button" style="display:none;">Tomar Foto</button>
        <canvas id="canvas" style="display:none;"></canvas>
    </div>
    <script>
    var video = document.getElementById('video');
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;
            video.play();
        });

    document.getElementById('take-photo-button').addEventListener('click', function() {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
        var dataUrl = canvas.toDataURL('image/jpeg');
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({ image: dataUrl }));
    });
    </script>
"""

st.markdown(stt_html, unsafe_allow_html=True)
st.markdown(camera_html, unsafe_allow_html=True)

# Endpoint para recibir la imagen capturada
from flask import Flask, request
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json['image']
    image_data = base64.b64decode(data.split(',')[1])
    image = Image.open(BytesIO(image_data))
    st.session_state['captured_image'] = image
    return '', 200

if 'captured_image' in st.session_state:
    st.image(st.session_state['captured_image'], caption="Tu Señal de Identificación")
    
    buffered = BytesIO()
    st.session_state['captured_image'].save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    st.download_button(
        label="Descargar",
        data=base64.b64decode(img_str),
        file_name="señal_identificacion.jpg",
        mime="image/jpeg"
    )

st.write("""
### ¡Comparte tu Señal!
Una vez que hayas creado tu señal de identificación, compártela con tus amigos y familiares para que puedan reconocerte fácilmente en la comunidad.
""")

