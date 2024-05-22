import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Título de la sección
st.title(" Básico: Tu Señal de Identificación")

# Descripción de la sección
st.write("""
En esta sección, puedes crear tu propia señal de identificación personalizada. 

En la comunidad de personas sordas, la presentación de los nombres se realiza de manera única y significativa a través del lenguaje de señas. 
Este proceso no solo implica deletrear el nombre con el alfabeto manual, sino también, en muchas ocasiones, incluir un "nombre en señas". 
Este nombre en señas, asignado por otros miembros de la comunidad sorda, captura una característica distintiva de la persona, ya sea física, de personalidad o relacionada con una experiencia memorable.
De esta manera, la presentación de un nombre en lenguaje de señas va más allá de la mera identificación, convirtiéndose en un reflejo de la identidad y la conexión social dentro de la comunidad.
Sigue los pasos a continuación para crear la tuya.
""")

# Video explicativo
st.write("""
Mira este video para conocer mas detalles sobre la señal de identificación.
""")
video_url = "https://www.youtube.com/watch?v=sGg6p03wADw" 
st.video(video_url)

st.write("""
## Ponlo en Práctica
Sigue los pasos a continuación para crear tu señal de identificación:
""")

img_file_buffer = st.camera_input("Toma una Foto")

if img_file_buffer is not None:
    # Convertir la entrada de la cámara en una imagen de PIL
    image = Image.open(img_file_buffer)
    st.image(image, caption="Tu Señal de Identificación")
    
    st.download_button(
        label="Descargar",
        data=open("señal_identificacion.jpg", "rb").read(),
        file_name="señal_identificacion.jpg",
         mime="image/jpeg" 
    )
st.write("""
### ¡Comparte tu Señal!
Una vez que hayas creado tu señal de identificación, compártela con tus amigos y familiares para que puedan reconocerte fácilmente en la comunidad.
""")
