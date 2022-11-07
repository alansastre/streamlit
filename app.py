import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

st.write("Hello world!")

st.title("Ejemplo de prueba Streamlit")
st.header("Ejemplo de header")
st.subheader("Ejemplo de subheader")
st.text("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.
""")

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

st.sidebar.header("Ejemplo de sidebar")

st.button("Click")

st.radio("Elige una opción", ["opción 1", "opción 2"])
st.selectbox("select", ["opción 1", "opción 2"])
st.multiselect("multiselect", ["opción 1", "opción 2"])
st.slider("Elige rango de precios", 0, 100)

st.text_input("Escribe algo")
st.text_area("Escribe algo largo")

df = pd.DataFrame(np.random.randn(20, 2), columns=["a", "b"])
st.line_chart(df)














