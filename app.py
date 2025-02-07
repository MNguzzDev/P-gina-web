import streamlit as st
from PIL import Image
import requests

 
st.set_page_config(page_title="gugutata", page_icon="🇻🇪", layout= "wide")



#intro

with st.container():
    st.header("hola, pagina de mrd")
    st.title("esta página es una mrd y ni sirve para nada")
    st.write("y bueno, estás es para perder el tiempo porque no creo que puedas a más")
    st.write("ya ni modo > (https://google.com)")

#sbore más
  
with st.container():
    st.write("---")
    text_column, animation_column = st.columns((2))
    with text_column:
        st.header("que quieres saber sapo?")
        st.write("acaso usted es sapo o que? Mejor venga y le explico como peinar a un perro")
    with animation_column:
        st.empty()
       

#otras cosas

with st.container():
    st.write("---")
    st.write("primer paso 😏")
    st.write("---")
    st.write("tenés que saber que peine usar, porque no puede ser cualquier peine malo"
            "---" 
        "Segundo: una buena delicadeza a la hora del peinado"
"---"
        "Tercero: peinar de arria hacaia abajo preferiblemente con un guante"
        "---"
        "cuarto: esto es opcional pero si quieres lo bañas primero para quitarle cualquier mugre"
        "")
