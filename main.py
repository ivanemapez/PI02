import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título del dashboard
st.title("Dashboard internet")

# Cargar datos desde un archivo en GitHub
url = "df_agrupado.csv"
url = "df_combinados.csv"
url = "df_nacional.csv"
url = "df_partidos.csv"
data = pd.read_csv(url)

# Mostrar datos
st.write("Vista previa de los datos", data.head())

# Agregar gráficos
st.line_chart(data)
