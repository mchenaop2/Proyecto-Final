import paho.mqtt.client as paho
import streamlit as st
import json

# Ruta a la imagen de fondo
image_base64 = get_base64_image("Fondo.png")  
# CSS para personalización de fondo y tipografía
st.markdown(
    f"""
    <style>
    .main {{
        background-image: url("data:image/png;base64,{image_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# Configuración del broker MQTT
broker = "broker.mqttdashboard.com"
port = 1883

# Funciones MQTT
def on_publish(client, userdata, result):
    print("El dato ha sido publicado \n")

def publish_message(topic, message):
    client = paho.Client("GIT-HUB")
    client.on_publish = on_publish
    client.connect(broker, port)
    client.publish(topic, json.dumps(message))

# Interfaz de usuario
st.title("Casa Inteligente")
st.image("LOGO.png", use_column_width=True)  # Cambia "LOGO.png" a la ruta de tu logo en el repositorio

# Configurar el estado de los botones en session_state para persistencia
if 'show_lights_options' not in st.session_state:
    st.session_state.show_lights_options = False
if 'show_music_options' not in st.session_state:
    st.session_state.show_music_options = False

# Crear columnas para centrar los botones principales


    # Botón para Luces con persistencia de estado
if st.button("Luces"):
     st.link_button("Iluminación", "https://clase-9-mflbrgrvxqeszl3edhdegx.streamlit.app/")



    # Botón para Música con persistencia de estado
if st.button("Música"):
    st.link_button("Playlist", "https://musica.streamlit.app/")

    

st.link_button("Control por voz", "https://controlporvoz-zuvfuyxes7wbobtbqgsuat.streamlit.app/")






