import streamlit as st
import numpy as np
import pandas as pd

# Screen Size
st.set_page_config(page_title= "Cargatron", 
                   page_icon=":fire:",
                   layout="wide")

def home():
    # Title
    st.title("Cargatron")

    #Home image
    st.image("Streamlit/Practica/img/puntos-recarga-madrid.jpg", width=500)

    # Description
    exp = st.expander = st.expander("Descripción")
    exp.write("Bienvenido al cargatron de Madrid. Localiza las estaciones de carga electrica de la ciudad.")

def data():
    # Dataframe
    df = st.file_uploader("Upload a CSV file", type=["csv"])
    if df is not None:
        st.dataframe(df)
        st.balloons()










