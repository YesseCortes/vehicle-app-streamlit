import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de vehículos en venta')

show_hist = st.checkbox('Mostrar histograma de kilometraje')

if show_hist:
    st.write('Distribución del kilometraje de los vehículos')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

show_scatter = st.checkbox('Mostrar gráfico Precio vs Año del modelo')

if show_scatter:
    st.write('Relación entre el precio y el año del modelo')
    fig2 = px.scatter(df, x='model_year', y='price')
    st.plotly_chart(fig2, use_container_width=True)
