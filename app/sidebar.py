# app/sidebar.py

import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    authors_df = pd.read_csv('data/authors.csv')
    quotes_df = pd.read_csv('data/quotes.csv')
    tags_df = pd.read_csv('data/tags.csv')
    quote_tag_df = pd.read_csv('data/quote_tag.csv')
    return authors_df, quotes_df, tags_df, quote_tag_df

def create_sidebar(page):
    authors_df, quotes_df, tags_df, quote_tag_df = load_data()

    if page == 'Home':
        st.sidebar.markdown(
            '<div style="font-size: 1rem;">Desarrollado por <a href="https://www.erikaalvares.es" target="_blank">Erika Alvares</a></div>',
            unsafe_allow_html=True
        )
        return authors_df, quotes_df, tags_df, quote_tag_df

    st.sidebar.header('Filters')

    if page == 'Quotes':
        selected_authors = st.sidebar.multiselect('Select Authors', authors_df['name'].unique(), key='quotes_authors')
        selected_tags = st.sidebar.multiselect('Select Tags', tags_df['tag'].unique(), key='quotes_tags')
        show_index = st.sidebar.checkbox('Show Index', value=True, key='quotes_show_index')
        return selected_authors, selected_tags, show_index, authors_df, quotes_df, tags_df, quote_tag_df

    elif page == 'Authors':
        selected_born_location = st.sidebar.multiselect('Select Born Location', authors_df['born_location'].unique(), key='authors_born_location')
        if selected_born_location:
            filtered_authors_df = authors_df[authors_df['born_location'].isin(selected_born_location)]
        else:
            filtered_authors_df = authors_df
        selected_authors = st.sidebar.multiselect('Select Authors', filtered_authors_df['name'].unique(), key='authors_names')
        return selected_born_location, selected_authors, None, authors_df, quotes_df, tags_df, quote_tag_df

    return None, None, None, authors_df, quotes_df, tags_df, quote_tag_df
