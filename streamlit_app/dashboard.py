import streamlit as st
import pandas as pd
import os

def show_dashboard():
    # Ruta a los archivos CSV
    data_path = os.path.join(os.path.dirname(__file__), '../data/')

    # Cargar los datos
    quotes_df = pd.read_csv(os.path.join(data_path, 'quotes.csv'))
    authors_df = pd.read_csv(os.path.join(data_path, 'authors.csv'))
    tags_df = pd.read_csv(os.path.join(data_path, 'tags.csv'))

    st.title('Dashboard de Citas')
    st.write('Estadísticas basadas en las citas extraídas.')

    st.subheader('Citas por Autor')
    author_counts = quotes_df['author'].value_counts()
    st.bar_chart(author_counts)

    st.subheader('Citas por Etiqueta')
    tags_list = quotes_df['tags'].apply(lambda x: x.strip("[]").replace("'", "").split(", "))
    tags_exploded = tags_list.explode()
    tag_counts = tags_exploded.value_counts()
    st.bar_chart(tag_counts)

    st.subheader('Filtrar Citas')
    selected_author = st.selectbox('Selecciona un autor', authors_df['name'].unique())
    filtered_quotes = quotes_df[quotes_df['author'] == selected_author]
    st.write(filtered_quotes)

    selected_tag = st.selectbox('Selecciona una etiqueta', tags_df['tag'].unique())
    filtered_quotes_by_tag = quotes_df[quotes_df['tags'].apply(lambda x: selected_tag in x)]
    st.write(filtered_quotes_by_tag)

