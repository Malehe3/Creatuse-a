import streamlit as st
from PIL import Image

# Título de la sección
st.title("Tu Señal de Identificación")

# Descripción de la sección
st.write("""
En esta sección, puedes crear tu propia señal de identificación personalizada. La señal de identificación es una forma única de ser reconocido en la comunidad sorda y oyente. Sigue los pasos a continuación para crear la tuya.
""")

# Video explicativo
st.write("""
## Video Explicativo

Mira este video para obtener instrucciones detalladas sobre cómo crear tu señal de identificación.
""")
# Incrustar un video (por ejemplo, un video de YouTube)
video_url = "https://www.youtube.com/watch?v=tu_video_id"  # Reemplaza con la URL de tu video
st.video(video_url)

# Subtítulo de la sección de práctica
st.write("""
## Ponlo en Práctica
Sigue los pasos a continuación para crear tu señal de identificación:
""")

# Botón para activar la cámara y tomar una foto
img_file_buffer = st.camera_input("Toma una Foto")

# Mostrar la foto tomada
if img_file_buffer is not None:
    # Convertir la entrada de la cámara en una imagen de PIL
    image = Image.open(img_file_buffer)
    st.image(image, caption="Tu Señal de Identificación")

    # Botón para descargar la foto
    if st.button("Descargar Señal"):
        # Guardar la imagen en el disco
        image.save("señal_identificacion.jpg", format="JPEG")

        # Ofrecer la imagen como una descarga
        st.download_button(
            label="Descargar",
            data=open("señal_identificacion.jpg", "rb").read(),
            file_name="señal_identificacion.jpg",
            mime="image/jpeg"
        )

