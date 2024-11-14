import paho.mqtt.client as paho
import streamlit as st
import json
import base64  # Para convertir la imagen a base64

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

# Función para cargar imagen y convertir a base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Carga la imagen de fondo localmente y conviértela a base64
background_image = get_base64_of_bin_file("Fondo.png")  # Cambia la ruta a la de tu imagen

# CSS para imagen de fondo
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{background_image}");
    background-size: cover;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

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
