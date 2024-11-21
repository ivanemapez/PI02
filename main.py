import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título del dashboard
st.title("Dashboard internet")

# Cargar datos desde un archivo en GitHub
url = "https://github.com/ivanemapez/PI02/blob/main/df_agrupado.csv"
url = "https://github.com/ivanemapez/PI02/blob/main/df_combinados.csv"
url = "https://github.com/ivanemapez/PI02/blob/main/df_nacional.csv"
url = "https://github.com/ivanemapez/PI02/blob/main/df_partidos.csv"
data = pd.read_csv(url)

# Mostrar datos
st.write("Vista previa de los datos", data.head())

# Agregar gráficos
st.line_chart(data)
