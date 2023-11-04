
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import base64
st.set_page_config(
    page_title="Ropa y calzado",
    layout="wide"
)

st.header("HELLO")


left, center, right = st.columns((1,1,1))
with left:
    st.write("Imagen1")
    with open("Ropa_ejemplo.jfif", "rb") as f:
        data_uri = base64.b64encode(f.read()).decode("utf-8")
        markdown = f"""
        <div class="image">
        <img src="data:image/png;base64, {data_uri}" alt="image" />
        </div>
        """
        st.markdown(markdown, unsafe_allow_html=True)
        st.write("Imagen3")
with center:
    st.write("Imagen2")
    with open("Ropa_ejemplo.jfif", "rb") as f:
        data_uri = base64.b64encode(f.read()).decode("utf-8")
        markdown = f"""
        <div class="image">
        <img src="data:image/png;base64, {data_uri}" alt="image" />
        </div>
        """
        st.markdown(markdown, unsafe_allow_html=True)
with right:
    st.write("Imagen3")
    with open("Ropa_ejemplo.jfif", "rb") as f:
        data_uri = base64.b64encode(f.read()).decode("utf-8")
        markdown = f"""
        <div class="image">
        <img src="data:image/png;base64, {data_uri}" alt="image" />
        </div>
        """
