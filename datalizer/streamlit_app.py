import streamlit as st

st.set_page_config(page_title="DataLizer", layout="wide")

# TODO Rol 5: estado de la sesión y barra lateral (sección 14.5)

st.navigation([
    st.Page("pages/1_Inicio.py", title="Inicio", default=True),
    st.Page("pages/2_Preparacion.py", title="Preparación"),
    st.Page("pages/3_Analisis.py", title="Análisis"),
]).run()

