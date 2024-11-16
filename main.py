import streamlit as st
from controller.controller import ControladorPlaystore

controlador = ControladorPlaystore()
st.title("Dados da Playstore")
controlador.executar_aplicacao()
