import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Acta Digital", layout="centered")

st.title("Acta Digital")
st.write("Escribe los puntos del acta y guarda una copia localmente.")

with st.form("form_acta"):
    fecha = st.date_input("Fecha", value=datetime.today())
    asistentes = st.text_area("Asistentes (separa por comas)")
    puntos = st.text_area("Puntos tratados")
    decisiones = st.text_area("Decisiones / Acuerdos")
    enviar = st.form_submit_button("Generar acta")

if enviar:
    contenido = f"""
ACTA - {fecha}

Asistentes:
{asistentes}

Puntos tratados:
{puntos}

Decisiones / Acuerdos:
{decisiones}
"""
    filename = f"acta_{fecha}.txt".replace(" ", "_")
    st.download_button("Descargar acta (.txt)", contenido, file_name=filename, mime="text/plain")
    st.success("Acta generada. Puedes descargarla con el botón.")
