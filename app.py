import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Título de la aplicación ---
st.header("Análisis de Vehículos")

# --- Cargar los datos ---
car_data = pd.read_csv('vehicles_us.csv')

st.write("Selecciona qué gráficos deseas visualizar:")

# --- Casillas de verificación ---
show_hist = st.checkbox('Mostrar histograma del odómetro')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# --- Generar histograma si se selecciona la casilla ---
if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(
        title="Distribución del Odómetro",
        xaxis_title="Kilometraje",
        yaxis_title="Cantidad de Vehículos",
        bargap=0.2
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# --- Generar scatter plot si se selecciona la casilla ---
if show_scatter:
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje')
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    )])
    fig_scatter.update_layout(
        title="Precio vs Kilometraje",
        xaxis_title="Kilometraje",
        yaxis_title="Precio",
        height=500
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

