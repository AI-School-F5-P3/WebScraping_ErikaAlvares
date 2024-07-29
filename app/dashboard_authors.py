# app/dashboard_authors.py

import streamlit as st
import pandas as pd

def show_authors_dashboard(selected_born_location, selected_authors, authors_df, quotes_df):
    st.title("Authors Dashboard")
    
    # Filtrar datos según la selección
    if selected_born_location:
        filtered_authors = authors_df[authors_df['born_location'].isin(selected_born_location)]
    else:
        filtered_authors = authors_df.copy()
    
    if selected_authors:
        filtered_authors = filtered_authors[filtered_authors['name'].isin(selected_authors)]
    
    st.subheader("Authors Details")
    
    for idx, row in filtered_authors.iterrows():
        st.markdown(f"""
            <div style="background-color: #ECF0F1; padding: 1rem; border-radius: 10px; margin-top: 2rem;">
                <h2 style="color: #2C3E50;">{row['name']}</h2>
                <p><strong>Born Date:</strong> {row['born_date']}</p>
                <p><strong>Born Location:</strong> {row['born_location']}</p>
                <p>{row['description']}</p>
            </div>
            <hr style="border-top: 1px solid #2C3E50;" />
        """, unsafe_allow_html=True)
