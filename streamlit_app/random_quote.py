import streamlit as st
import pandas as pd
import os
import random

def show_random_quote():
    # Ruta a los archivos CSV
    data_path = os.path.join(os.path.dirname(__file__), '../data/')

    # Cargar los datos
    quotes_df = pd.read_csv(os.path.join(data_path, 'quotes.csv'))

    st.title('Generador de Citas Aleatorias')
    st.write('Selecciona cómo te sientes hoy y recibirás una cita aleatoria.')

    mood = st.selectbox('¿Cómo te sientes hoy?', ['Feliz', 'Triste', 'Motivado', 'Estresado', 'Curioso'])

    if st.button('Generar Cita'):
        random_quote = quotes_df.sample(n=1)
        st.write(random_quote['quote'].values[0])
        st.write(f"- {random_quote['author'].values[0]}")
