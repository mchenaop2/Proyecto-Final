import paho.mqtt.client as paho
import streamlit as st
import json

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
st.image("logo.png", use_column_width=True)  # Cambia "logo.png" a la ruta de tu logo en el repositorio

# Crear columnas para centrar los botones principales
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.subheader("Control de Funciones")
    
    # Sección de Luces
    if st.button("Luces"):
        st.write("Selecciona un modo de luces:")
        if st.button("Relajación"):
            publish_message("cmqtt_luces", {"Luces": "Cálidas y tenues"})
        elif st.button("Concentración"):
            publish_message("cmqtt_luces", {"Luces": "Frías"})
        elif st.button("Fiesta"):
            publish_message("cmqtt_luces", {"Luces": "Colores"})
        elif st.button("Despertar"):
            publish_message("cmqtt_luces", {"Luces": "Aumento gradual"})
        elif st.button("Cine"):
            publish_message("cmqtt_luces", {"Luces": "Apagadas"})
    
    # Sección de Música
    if st.button("Música"):
        st.write("Selecciona una emoción para la música:")
        
        col_music1, col_music2 = st.columns(2)
        
        with col_music1:
            if st.button("🎵 Tristeza"):
                publish_message("cmqtt_musica", {"Musica": "Tristeza"})
            if st.button("🎵 Romántico"):
                publish_message("cmqtt_musica", {"Musica": "Romántico"})
                
        with col_music2:
            if st.button("🎵 Felicidad"):
                publish_message("cmqtt_musica", {"Musica": "Felicidad"})
            if st.button("🎵 Meditación"):
                publish_message("cmqtt_musica", {"Musica": "Meditación"})
