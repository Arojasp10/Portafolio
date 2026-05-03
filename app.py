import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", layout="wide")

# Estilos CSS para cards y títulos
st.markdown(
    """
    <style>
    .titulo {
        font-size: 48px;
        font-weight: bold;
        color: #620462;
        text-align: center;
    }
    .subtitulo {
        font-size: 24px;
        color: #555;
        text-align: center;
    }
    .card {
        background: linear-gradient(135deg, #f3defe 0%, #fcdefe 100%);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 15px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        text-align: center;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }
    .card h3 {
        color: #620462;
        margin-bottom: 10px;
    }
    .card a {
        text-decoration: none;
        font-weight: bold;
        color: #007BFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Encabezado
st.markdown('<div class="titulo"> Bienvenido a mi Portafolio</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Aquí encontrarás mis proyectos y actividades</div>', unsafe_allow_html=True)

st.write("---")

# Lista de proyectos
proyectos = {
    "🌟 Proyecto 1 - Clase 01": "https://intro-26-02-2026-mirprimerappeninterfaces10.streamlit.app/",
    "✨ Proyecto 2 - Control por voz inteligente": "https://ctrlvoice-controlxvoz-arp07.streamlit.app/",
    "🌟 Proyecto 3 - Tablero Inteligente": "https://drawrecode0111.streamlit.app/",
    "✨ Proyecto 4 - Reconocimiento de dígitos a mano": "https://gvg6qqomh6vofairthbflj.streamlit.app/",
    "🌟 Proyecto 5 - Conversión texto-audio": "https://im-class6-labasequepasoelprofe.streamlit.app/",   
    "✨ Proyecto 6 - RAG ": "https://chatpdf-563hjncbbazkw2zpmjkwq8.streamlit.app/",
    "🌟 Proyecto 7 - Generador de Texto LSTM": "https://lstmnlp-kno59sekzgxzj4ss73dsec.streamlit.app/",
    "✨ Proyecto 8 - Lector de imágenes": "https://7j5f9mvnfz4wv4ybjrk6zb.streamlit.app/",
    "🌟 Proyecto 9 - Reconocimiento óptico y transcripción": "https://ocr-audio-c7khzhtv5d3xhgarj3ww4b.streamlit.app/",
    "✨ Proyecto 10 - Lector sensor MQTT": "https://recepmqtt-ang10.streamlit.app/",
    "🌟 Proyecto 11 - MQTT Control": "https://sendcmqtt-ang10recibirmsj-mqtt.streamlit.app/",
    "✨ Proyecto 12 - Análisis sentimiento": "https://sentimenta-8cpozjsvsqjmb8td7c6dce.streamlit.app/",
    "🌟 Proyecto 13 - Tablero para dibujo": "https://tablero-cs5y4l5a4mxt7a37mbb5en.streamlit.app/",
    "✨ Proyecto 14 - Demo TF-IDF Español": "https://tdfesp-bwvzb43a7mjkpdmmgzg58f.streamlit.app/",
    "🌟 Proyecto 15 - Demo TF-IDF Preguntas y respuestas": "https://ddkivd7kpctzjvszaqjemt.streamlit.app/",
    "✨ Proyecto 16 - Reconocimiento de Imágenes": "https://3ztdbjn8rti39uuup5wzvg.streamlit.app/",
    "🌟 Proyecto 17 - Traductor": "https://traductor-dj7eknpxterzom6jcqksvx.streamlit.app/",
    "✨ Proyecto 18 - Análisis de Imagen": "https://visionapp-fzhbfxynukfkteugdisjsd.streamlit.app/",
    "🌟 Proyecto 19 - WordCloud": "https://wordcloud-zv6qtjhrx4r5nw6uxev4xv.streamlit.app/",
    "✨ Proyecto 20 - YOLO": "https://yolov5-pdstfhzmscsgf9ghwethfa.streamlit.app/",
}

# Mostrar proyectos en columnas tipo tarjetas
cols = st.columns(3)
for i, (nombre, link) in enumerate(proyectos.items()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="card">
                <h3>{nombre}</h3>
                <a href="{link}" target="_blank">🔗 Ver Proyecto</a>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("---")
