import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Cargar los tres DataFrames
df_partidos = pd.read_csv('df_partidos.csv')
df_nacional = pd.read_csv('df_nacional.csv')
df_combinado = pd.read_csv('df_combinados.csv')
# Título del Dashboard
st.title("Dashboard de Análisis de Conectividad")

# Título de la aplicación
st.title("Distribución de conexiones por tipo")

# Usamos el DataFrame `df_combinado` ya cargado
df_combinado.columns = df_combinado.columns.str.strip()

# Selección de columnas relevantes
columnas = ['adsl', 'cablemodem', 'fibra óptica', 'wireless', 'otros']
columnas_normalizadas = [col.lower() for col in columnas]

# Eliminar filas con valores nulos en las columnas relevantes
df_combinado = df_combinado.dropna(subset=columnas_normalizadas)

# Convertir las columnas relevantes a valores numéricos
for col in columnas_normalizadas:
    df_combinado[col] = pd.to_numeric(df_combinado[col], errors='coerce')

# Filtros interactivos
st.sidebar.subheader("Filtros")
min_anio = int(df_combinado['año'].min())
max_anio = int(df_combinado['año'].max())

rango_anios = st.sidebar.slider(
    "Selecciona el rango de años",
    min_value=min_anio,
    max_value=max_anio,
    value=(min_anio, max_anio)
)

# Filtrar datos por rango de años
df_filtrado = df_combinado[(df_combinado['año'] >= rango_anios[0]) & (df_combinado['año'] <= rango_anios[1])]

# Comprobar si el DataFrame filtrado contiene datos
if not df_filtrado.empty:
    # Agrupar datos por año y calcular la suma de conexiones por tipo
    data_agrupada = df_filtrado.groupby('año')[columnas_normalizadas].sum()

    # Crear gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    data_agrupada.plot(kind='bar', ax=ax)

    ax.set_title('Cantidad de conexiones por tipo (por año)')
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de conexiones')
    ax.legend(title='Tipo de conexión')
    st.pyplot(fig)
else:
    st.warning("No hay datos disponibles para el rango de años seleccionado.")

st.title("Tendencia del Total de Conexiones a lo Largo del Tiempo")

# Ordenar el DataFrame por 'año'
df_combinado = df_combinado.sort_values(by='año')

# Eliminar filas con valores nulos en 'año' o 'total_conexion'
df_combinado = df_combinado.dropna(subset=['año', 'total_conexion'])

# Asegurarse de que 'año' y 'total_conexion' sean numéricos
df_combinado['año'] = pd.to_numeric(df_combinado['año'], errors='coerce')
df_combinado['total_conexion'] = pd.to_numeric(df_combinado['total_conexion'], errors='coerce')

# Crear el gráfico de tendencia
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=df_combinado, x='año', y='total_conexion', ax=ax)
ax.set_title("Tendencia total conexion a lo largo del tiempo", fontsize=16)
ax.set_xlabel("Año", fontsize=12)
ax.set_ylabel("Total de Conexiones", fontsize=12)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


# Convertir columnas a cadenas para evitar errores
df_combinado["año"] = df_combinado["año"].astype(str)
df_combinado["provincia"] = df_combinado["provincia"].astype(str)


# Limpieza de datos: asegurarse de que las columnas relevantes sean tipo string
df_combinado['año'] = df_combinado['año'].fillna("Desconocido").astype(str)  # Convertir 'año' a str
df_combinado['provincia'] = df_combinado['provincia'].fillna("Desconocido").astype(str)  # Convertir 'provincia' a str

# Mostrar los filtros en el sidebar de Streamlit
st.title("Análisis de Conexiones por Año y Provincia")
st.sidebar.header("Filtros año, prov.")

# Asegurarse de que los valores únicos sean de tipo str
años = df_combinado['año'].unique().astype(str)  # Convertir valores únicos de 'año' a str
provincias = df_combinado['provincia'].unique().astype(str)  # Convertir valores únicos de 'provincia' a str

# Filtros en Streamlit para seleccionar año y provincia
año_seleccionado = st.sidebar.selectbox("Selecciona el año:", años, key="año_filtro")
provincia_seleccionada = st.sidebar.selectbox("Selecciona la provincia:", provincias, key="provincia_filtro")

# Filtrar los datos basados en los valores seleccionados
df_filtrado = df_combinado[
    (df_combinado['año'] == año_seleccionado) & (df_combinado['provincia'] == provincia_seleccionada)
]

# Verificación si el DataFrame filtrado no está vacío
if not df_filtrado.empty:
    # Definir las columnas de las conexiones
    conexiones = ['banda ancha fija', 'dial up', 'cablemodem', 'fibra óptica', 'wireless']
    
    # Extraer los valores de las conexiones para el gráfico
    valores_conexiones = df_filtrado[conexiones].iloc[0]  # Usar el primer valor después de filtrar

    # Crear gráfico de barras interactivo con plotly
    fig = px.bar(
        x=conexiones,
        y=valores_conexiones,
        labels={"x": "Tipo de Conexión", "y": "Cantidad de conexiones"},
        title=f"Conexiones en {provincia_seleccionada} durante {año_seleccionado}",
        color=conexiones,  # Agregar color para diferenciar las barras
        color_discrete_sequence=px.colors.qualitative.Set1  # Cambiar colores de las barras
    )
    
    # Mostrar el gráfico en streamlit
    st.plotly_chart(fig)
else:
    st.warning("No hay datos disponibles para los filtros seleccionados.")



# Agrupar por año y sumar los ingresos
df_agrupado = df_nacional.groupby('año')['ingresos (miles de pesos)'].sum().reset_index()

# Crear gráfico lineal
st.title('Gráfico Lineal de Ingresos por Año')

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(df_agrupado['año'], df_agrupado['ingresos (miles de pesos)'], marker='o', color='tab:blue', label='Ingresos')
ax.set_xlabel('Año')
ax.set_ylabel('Ingresos (miles de pesos)')
ax.set_title('Ingresos Totales por Año')
ax.grid(True)

# Mostrar gráfico en Streamlit
st.pyplot(fig)



# Filtro para seleccionar la provincia
provincia_seleccionada = st.selectbox("Selecciona la provincia", df_partidos['Provincia'].unique())

# Filtrar partidos según la provincia seleccionada
partidos_provincia = df_partidos[df_partidos['Provincia'] == provincia_seleccionada]['Partido'].unique()

# Filtro para seleccionar el partido
partido_seleccionado = st.selectbox("Selecciona el partido", partidos_provincia)

# Filtrar localidades y tecnologías según el partido seleccionado
df_partido_filtrado = df_partidos[df_partidos['Partido'] == partido_seleccionado]

# Mostrar un resumen de los datos filtrados
st.write(f"Datos filtrados para el partido {partido_seleccionado} en la provincia {provincia_seleccionada}")


# Contar las tecnologías disponibles en el partido seleccionado
tecnologias_count = df_partido_filtrado['Tecnologia'].value_counts()

# Mostrar gráfico circular de la distribución de tecnologías
fig, ax = plt.subplots()
tecnologias_count.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90, legend=True)
ax.set_ylabel('')  # Eliminar la etiqueta del eje Y

# Mostrar el gráfico en Streamlit
st.pyplot(fig)



# Filtro para seleccionar la provincia
provincia_seleccionada = st.selectbox(
    "Selecciona la provincia",
    df_partidos['Provincia'].unique(),
    key="provincia_select"
)

# Filtrar datos según la provincia seleccionada
df_provincia_filtrada = df_partidos[df_partidos['Provincia'] == provincia_seleccionada]

# Mostrar un resumen de los datos filtrados
st.write(f"Datos filtrados para la provincia {provincia_seleccionada}")

# Contar las tecnologías disponibles en la provincia seleccionada
tecnologias_count = df_provincia_filtrada['Tecnologia'].value_counts()

# Mostrar gráfico circular de la distribución de tecnologías
fig, ax = plt.subplots()
tecnologias_count.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90, legend=True)
ax.set_ylabel('')  # Eliminar la etiqueta del eje Y

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


# Limpiar y convertir "accesos por cada 100 hogares" a numérico
df_combinado['accesos por cada 100 hogares'] = (
    df_combinado['accesos por cada 100 hogares']
    .str.replace(',', '.', regex=False)  # Cambiar coma por punto
    .astype(float)  # Convertir a flotante
)

# Crear un único filtro para seleccionar la provincia (con clave única)
provincia_seleccionada = st.selectbox(
    "Selecciona una provincia",
    df_combinado['provincia'].unique(),
    key="provincia_selectbox_key"  # Clave única
)

# Filtrar el DataFrame para la provincia seleccionada
df_filtrado = df_combinado[df_combinado['provincia'] == provincia_seleccionada]

# Definir el incremento del 2%
incremento = 0.02

# Calcular el nuevo acceso y el KPI
df_filtrado['nuevo acceso'] = df_filtrado['accesos por cada 100 hogares'] * (1 + incremento)
df_filtrado['KPI'] = ((df_filtrado['nuevo acceso'] - df_filtrado['accesos por cada 100 hogares']) /
                      df_filtrado['accesos por cada 100 hogares']) * 100

# Agrupar por trimestre y calcular las sumas
df_resumen_trimestre = df_filtrado.groupby('trimestre').agg({
    'accesos por cada 100 hogares': 'sum',
    'nuevo acceso': 'sum',
    'KPI': 'mean'  # Usamos la media para el KPI porque es un porcentaje
}).reset_index()

# Mostrar resumen por trimestre
st.write("Resumen por trimestre:")
#st.write(df_resumen_trimestre)

# Crear un único filtro para seleccionar la tecnología a graficar (con clave única)
opciones_columnas = ["banda ancha fija", "dial up", "adsl", "cablemodem", "fibra óptica", "wireless"]
columna_seleccionada = st.selectbox(
    "Selecciona una tecnología para graficar",
    opciones_columnas,
    key="tecnologia_selectbox_key"  # Clave única
)

# Verificar si la columna seleccionada está en el DataFrame
if columna_seleccionada not in df_filtrado.columns:
    st.error(f"La columna {columna_seleccionada} no está disponible en los datos.")
else:
    # Graficar la distribución de la columna seleccionada
    valores = df_filtrado[columna_seleccionada].value_counts()

    # Verificar si hay datos para graficar
    if valores.empty:
        st.warning(f"No hay datos disponibles para la tecnología seleccionada: {columna_seleccionada}.")
    else:
        fig, ax = plt.subplots()
        ax.pie(valores, labels=valores.index, autopct='%1.1f%%', startangle=90)
        ax.set_title(f"Distribución de {columna_seleccionada} en {provincia_seleccionada}")
        st.pyplot(fig)


# Limpiar y convertir "ingresos (miles de pesos)" a numérico
df_nacional['ingresos (miles de pesos)'] = (
    df_nacional['ingresos (miles de pesos)']
    .str.replace('.', '', regex=False)  # Eliminar separadores de miles
    .str.replace(',', '.', regex=False)  # Cambiar coma por punto como separador decimal
    .str.strip()  # Eliminar espacios adicionales
    .astype(float)  # Convertir a flotante
)

# Agrupar por año y sumar los trimestres
df_ingresos = df_nacional.groupby('año')['ingresos (miles de pesos)'].sum().reset_index()

# Calcular el crecimiento porcentual año a año (YoY)
df_ingresos['crecimiento_ingresos'] = df_ingresos['ingresos (miles de pesos)'].pct_change() * 100

# Calcular CAGR (Crecimiento Anual Compuesto) entre 2014 y 2024
try:
    ingresos_inicio = df_ingresos.loc[df_ingresos['año'] == 2014, 'ingresos (miles de pesos)'].values[0]
    ingresos_final = df_ingresos.loc[df_ingresos['año'] == 2024, 'ingresos (miles de pesos)'].values[0]
    cagr = ((ingresos_final / ingresos_inicio) ** (1 / 10)) - 1
except IndexError:
    cagr = None
    st.warning("Datos faltantes para 2014 o 2024. No se puede calcular el CAGR.")

# Mostrar el DataFrame con crecimiento YoY
st.write("Crecimiento porcentual de ingresos año a año:")
#st.write(df_ingresos)

if cagr is not None:
    st.write(f"CAGR entre 2014 y 2024: {cagr * 100:.2f}%")

# Gráfico de crecimiento YoY
fig, ax = plt.subplots()
ax.plot(df_ingresos['año'], df_ingresos['crecimiento_ingresos'], marker='o', label='Crecimiento %')
ax.set_title("Crecimiento porcentual de ingresos (YoY)")
ax.set_xlabel("Año")
ax.set_ylabel("Crecimiento (%)")
ax.axhline(0, color='red', linestyle='--', label='Referencia')
ax.legend()
st.pyplot(fig)

# Comparación entre dos años seleccionados
st.write("Comparación de ingresos entre dos años seleccionados:")
año_1 = st.selectbox("Selecciona el primer año", df_ingresos['año'].unique(), key="año_1")
año_2 = st.selectbox("Selecciona el segundo año", df_ingresos['año'].unique(), key="año_2")

ingresos_año_1 = df_ingresos.loc[df_ingresos['año'] == año_1, 'ingresos (miles de pesos)'].values[0]
ingresos_año_2 = df_ingresos.loc[df_ingresos['año'] == año_2, 'ingresos (miles de pesos)'].values[0]

fig, ax = plt.subplots()
ax.bar([año_1, año_2], [ingresos_año_1, ingresos_año_2], color=['blue', 'orange'])
ax.set_title(f"Comparación de ingresos entre {año_1} y {año_2}")
ax.set_ylabel("Ingresos (miles de pesos)")
st.pyplot(fig)
