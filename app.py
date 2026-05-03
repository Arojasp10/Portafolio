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
        color: #620462;
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

st.markdown(
    """
    <style>
    .card {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
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
