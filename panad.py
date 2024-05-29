# Importar las bibliotecas necesarias
import streamlit as st  # Para la creación de la aplicación web
import pandas as pd      # Para la manipulación y análisis de datos
import numpy as np       # Para operaciones numéricas
import matplotlib.pyplot as plt  # Para la visualización de datos

# Ajuste de visualización de Pandas para mostrar todas las filas y columnas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Título principal de la aplicación web
st.title('Análisis de Datos COVID-19 en Perú')

# Rutas de los archivos CSV
positivos_filepath = 'positivos_covid.csv'
fallecidos_filepath = 'fallecidos_covid.csv'

# Función para cargar los datos desde los archivos CSV
@st.cache_data
def load_data(filepath, encoding='latin-1', date_column=None):
    data = pd.read_csv(filepath, encoding=encoding, parse_dates=[date_column])
    return data

# Cargar los datos de casos positivos y fallecidos utilizando la función anterior
peru_pos = load_data(positivos_filepath, date_column='FECHA_RESULTADO')
peru_fall = load_data(fallecidos_filepath, date_column='FECHA_FALLECIMIENTO')

# Interpreta los datos de casos positivos COVID-19
st.subheader('Interpretación de Datos de Positivos COVID-19:')
st.write('- El conjunto de datos de positivos COVID-19 contiene información sobre los casos confirmados de COVID-19 en Perú.')
st.write('- Incluye la fecha en que se obtuvo el resultado positivo para cada caso.')
st.write('- El análisis de estos datos puede ayudar a comprender la evolución de la propagación del virus.')

# Visualizar datos de positivos COVID-19
st.subheader('Datos de Positivos COVID-19:')
st.write(peru_pos)

# Interpreta los datos de fallecidos COVID-19
st.subheader('Interpretación de Datos de Fallecidos COVID-19:')
st.write('- El conjunto de datos de fallecidos COVID-19 contiene información sobre las personas fallecidas a causa del COVID-19 en Perú.')
st.write('- Incluye la fecha de fallecimiento de cada persona.')
st.write('- Analizar estos datos puede ayudar a comprender la gravedad de la situación y la evolución de la mortalidad.')

# Visualizar datos de fallecidos COVID-19
st.subheader('Datos de Fallecidos COVID-19:')
st.write(peru_fall)

# Gráfico de evolución de casos positivos
st.subheader('Evolución de Casos Positivos de COVID-19:')  #crea el subtitulo
peru_pos['FECHA_RESULTADO'] = pd.to_datetime(peru_pos['FECHA_RESULTADO']) #convierte la columna FECHA_RESULTADO' del DataFrame
positivos_por_fecha = peru_pos.groupby('FECHA_RESULTADO').size()   # se agryupa a las columnba frecha resultado

plt.figure(figsize=(10, 5))
plt.plot(positivos_por_fecha.index, positivos_por_fecha.values, label='Casos positivos')
plt.xlabel('Fecha')
plt.ylabel('Número de casos')
plt.title('Evolución de casos positivos de COVID-19 en Perú')
plt.legend()
plt.grid(True)
st.pyplot(plt)

# Gráfico de evolución de fallecidos
st.subheader('Evolución de Fallecidos por COVID-19:')
peru_fall['FECHA_FALLECIMIENTO'] = pd.to_datetime(peru_fall['FECHA_FALLECIMIENTO'])
fallecidos_por_fecha = peru_fall.groupby('FECHA_FALLECIMIENTO').size()

plt.figure(figsize=(10, 5))
plt.plot(fallecidos_por_fecha.index, fallecidos_por_fecha.values, label='Fallecidos', color='red')
plt.xlabel('Fecha')
plt.ylabel('Número de fallecidos')
plt.title('Evolución de fallecidos por COVID-19 en Perú')
plt.legend()
plt.grid(True)
st.pyplot(plt)
