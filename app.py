import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

# Configuración del broker
broker = "broker.mqttdashboard.com"
port = 1883

# Funciones MQTT
def on_publish(client, userdata, result):
    print("El dato ha sido publicado \n")
    pass

def publish_message(topic, message):
    client = paho.Client("GIT-HUB")
    client.on_publish = on_publish
    client.connect(broker, port)
    client.publish(topic, json.dumps(message))

# Título y logo
st.title("Casa Inteligente")
st.image("ruta_al_logo.png", use_column_width=True)  # Cambia "ruta_al_logo.png" a la ruta de tu logo

# Crear espacio para centrar el menú en la pantalla
st.write("###")  # Salto de línea para centrar verticalmente

# Columnas para centrar los botones en el medio
col1, col2, col3 = st.columns([1, 2, 1])  # La columna central es más ancha para centrar los botones

with col2:
    st.subheader("Control de Funciones")
    if st.button('Luces'):
        st.write("Selecciona un modo para las luces:")
        if st.button('Encender Luces'):
            publish_message("cmqtt_luces", {"Luces": "ON"})
        elif st.button('Apagar Luces'):
            publish_message("cmqtt_luces", {"Luces": "OFF"})
    
    if st.button('Música'):
        st.write("Selecciona un modo para la música:")
        if st.button('Reproducir Música'):
            publish_message("cmqtt_musica", {"Musica": "Play"})
        elif st.button('Detener Música'):
            publish_message("cmqtt_musica", {"Musica": "Stop"})
    
    if st.button('Temperatura'):
        st.write("Selecciona un valor de temperatura:")
        temp = st.slider('Temperatura', 0.0, 100.0)
        if st.button('Enviar temperatura'):
            publish_message("cmqtt_temperatura", {"Temperatura": temp})
