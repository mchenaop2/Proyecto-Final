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
st.image("LOGO.png", use_column_width=True)  # Cambia "ruta_al_logo.png" a la ruta de tu logo

# Almacenar el estado de los botones en `st.session_state`
if 'luces' not in st.session_state:
    st.session_state.luces = False
if 'musica' not in st.session_state:
    st.session_state.musica = False
if 'temperatura' not in st.session_state:
    st.session_state.temperatura = 0.0

# Columnas para centrar los botones en el medio
col1, col2, col3 = st.columns([1, 2, 1])  # La columna central es más ancha para centrar los botones

with col2:
    st.subheader("Control de Funciones")
       with st.expander("See explanation"):
        st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
       ''')
       st.button("Luces 2",key="otro")    
    # Botón de luces con persistencia de estado
    if st.button('Luces'):
        st.session_state.luces = not st.session_state.luces  # Alterna el estado de luces
        if st.session_state.luces:
            publish_message("cmqtt_luces", {"Luces": "ON"})
        else:
            publish_message("cmqtt_luces", {"Luces": "OFF"})
        st.write("Luces encendidas" if st.session_state.luces else "Luces apagadas")

    # Botón de música con persistencia de estado
    if st.button('Música'):
        st.session_state.musica = not st.session_state.musica  # Alterna el estado de música
        if st.session_state.musica:
            publish_message("cmqtt_musica", {"Musica": "Play"})
        else:
            publish_message("cmqtt_musica", {"Musica": "Stop"})
        st.write("Música reproduciendo" if st.session_state.musica else "Música detenida")

    # Control de temperatura con slider y botón de envío
    temp = st.slider('Temperatura', 0.0, 100.0, st.session_state.temperatura)
    if st.button('Enviar temperatura'):
        st.session_state.temperatura = temp
        publish_message("cmqtt_temperatura", {"Temperatura": temp})
        st.write(f"Temperatura ajustada a {temp} °C")
