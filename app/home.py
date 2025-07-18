import streamlit as st

from components.header import *
from components.footer import *
from src.config.settings import APP_NAME, APP_VERSION, APP_DESCRIPTION, APP_AUTHOR, APP_DATE, APP_REPO, APP_REPO_NAME

header_basic()

st.set_page_config(
    page_title=f"Inicio - {APP_NAME}",
    page_icon="👮🏻‍♂️",
    layout="wide"
)

st.write(f"### {APP_DESCRIPTION}")
st.write(f"#### *{APP_REPO_NAME} v.{APP_VERSION}*")
st.link_button("Ver en GitHub", APP_REPO)
st.text(f'Desarrollado por: {APP_AUTHOR} - {APP_DATE}')

footer_contact()