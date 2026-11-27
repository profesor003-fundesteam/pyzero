import streamlit as st

from datos import DEMOS

st.title("DataLizer")
st.caption("Página en construcción · Rol 5")

# TODO Rol 5: galería con tarjetas, carga de archivo y contexto
for nombre in DEMOS:
    st.write(nombre)
