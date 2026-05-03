import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", layout="wide")

# Encabezado con estilo
st.markdown(
    """
    <style>
    .titulo {
        font-size: 48px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .subtitulo {
        font-size: 24px;
        color: #555;
        text-align: center;
    }
    .card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="titulo">👋 Bienvenido a mi Portafolio</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Aquí encontrarás mis proyectos y actividades</div>', unsafe_allow_html=True)

st.write("---")

# Lista de proyectos
proyectos = {
    "📊 Proyecto 1 - Análisis de Datos": "https://github.com/usuario/proyecto1",
    "📈 Proyecto 2 - Visualización": "https://github.com/usuario/proyecto2",
    "🤖 Proyecto 3 - Machine Learning": "https://github.com/usuario/proyecto3",
}

# Mostrar proyectos en columnas tipo tarjetas
cols = st.columns(3)
for i, (nombre, link) in enumerate(proyectos.items()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="card">
                <h3>{nombre}</h3>
                <a href="{link}" target="_blank">🔗 Ver en GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("---")
st.success("✨ Portafolio creado con Streamlit. ¡Listo para desplegar en la nube!")
