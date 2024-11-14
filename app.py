import paho.mqtt.client as paho
import streamlit as st
import json
import base64  # Para convertir la imagen a base64

# Configuración del broker MQTT
broker = "broker.mqttdashboard.com"
port = 1883

# Funciones MQTT
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convertir la imagen de fondo local a base64
background_image = get_base64_of_bin_file("Fondo.png")  # Cambia a la ruta de tu imagen local

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

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):  # Función de callback para publicación
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)
# Crear columnas para centrar los botones principales

# Botón para Luces con persistencia de estado
if st.button("Luces"):
    st.link_button("Iluminación", "https://clase-9-mflbrgrvxqeszl3edhdegx.streamlit.app/")

# Botón para Música con persistencia de estado
if st.button("Música"):
    st.link_button("Playlist", "https://musica.streamlit.app/")

st.link_button("Control por voz", "https://controlporvoz-zuvfuyxes7wbobtbqgsuat.streamlit.app/")
