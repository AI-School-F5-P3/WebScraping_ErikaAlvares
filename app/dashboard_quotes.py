import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def show_quotes_dashboard(selected_authors, selected_tags, show_index, authors_df, quotes_df, tags_df, quote_tag_df):
    st.title("Quotes Dashboard")

    # Filter data based on selections
    filtered_quotes = quotes_df.copy()
    filtered_quote_ids_by_tags = []

    if selected_authors:
        filtered_quotes = filtered_quotes[filtered_quotes['author'].isin(selected_authors)]

    # Obtener los ids de las citas filtradas
    filtered_quote_ids = filtered_quotes.index.tolist()

    if selected_tags:
        # Obtener los ids de las etiquetas seleccionadas
        selected_tag_ids = tags_df[tags_df['tag'].isin(selected_tags)].index.tolist()
        # Filtrar la tabla de relaciones para obtener solo las citas que tienen las etiquetas seleccionadas
        filtered_quote_tag_df = quote_tag_df[quote_tag_df['tag_id'].isin(selected_tag_ids)]
        # Obtener los ids de las citas que cumplen con las etiquetas seleccionadas
        filtered_quote_ids_by_tags = filtered_quote_tag_df['quote_id'].unique().tolist()
        # Filtrar las citas que están en ambos conjuntos (autores seleccionados y etiquetas seleccionadas)
        filtered_quote_ids = list(set(filtered_quote_ids) & set(filtered_quote_ids_by_tags))
    else:
        filtered_quote_ids_by_tags = filtered_quote_ids

    # Filtrar las citas finales basadas en los ids obtenidos
    filtered_quotes = quotes_df.loc[filtered_quote_ids]

    # KPI section
    st.markdown("""
        <div style="background-color: #2ECC71; padding: 1rem; border-radius: 10px;">
            <h2 style="color: #FFFFFF;">Key Performance Indicators</h2>
            <div style="display: flex; justify-content: space-around;">
                <div style="background: #ECF0F1; padding: 1rem; border-radius: 10px; color: #2C3E50; width: 30%; text-align: center;">
                    <h3>Total Quotes</h3>
                    <p style="font-size: 1.8rem;">{}</p>
                </div>
                <div style="background: #ECF0F1; padding: 1rem; border-radius: 10px; color: #2C3E50; width: 30%; text-align: center;">
                    <h3>Total Authors</h3>
                    <p style="font-size: 1.8rem;">{}</p>
                </div>
                <div style="background: #ECF0F1; padding: 1rem; border-radius: 10px; color: #2C3E50; width: 30%; text-align: center;">
                    <h3>Total Tags</h3>
                    <p style="font-size: 1.8rem;">{}</p>
                </div>
            </div>
        </div>
    """.format(len(filtered_quotes), len(filtered_quotes['author'].unique()), len(filtered_quote_ids_by_tags)), unsafe_allow_html=True)

    # Quotes by Author and Top Authors side by side
    col1, col2 = st.columns([2, 1])  # Proporción 2:1 para gráfica y tabla
    with col1:
        st.subheader("Quotes by Author")
        if 'author' in filtered_quotes.columns:
            author_count = filtered_quotes['author'].value_counts().reset_index()
            author_count.columns = ['author', 'count']
            fig_author = px.bar(
                author_count, 
                x='author', 
                y='count', 
                title="Number of Quotes by Author",
                color_discrete_sequence=['#FFA500']  # Color naranja
            )
            fig_author.update_traces(marker=dict(
                color='rgba(255, 165, 0, 0.9)',  # Naranja con opacidad
                line=dict(color='rgba(255, 165, 0, 1.0)', width=2)
            ))
            fig_author.update_layout(
                font=dict(size=16, color="#2C3E50"),  # Aumenta el tamaño y oscurece el color
                title_font=dict(size=20, color="#2C3E50"),  # Título más grande y oscuro
                xaxis=dict(tickfont=dict(size=14, color="#2C3E50")),  # Etiquetas del eje X más grandes y oscuras
                yaxis=dict(tickfont=dict(size=14, color="#2C3E50"))   # Etiquetas del eje Y más grandes y oscuras
            )
            st.plotly_chart(fig_author, use_container_width=True)
        else:
            st.error("La columna 'author' no está presente en filtered_quotes.")

    with col2:
        st.subheader("Top 10 Authors")
        if 'author' in author_count.columns:
            top_authors = author_count.head(10)
            st.table(top_authors.set_index('author') if show_index else top_authors)
        else:
            st.error("La columna 'author' no está presente en author_count.")

    # Quotes by Tag and Top Tags side by side
    col1, col2 = st.columns([2, 1])  # Proporción 2:1 para gráfica y tabla
    with col1:
        st.subheader("Quotes by Tag")
        if not selected_tags:
            if selected_authors:
                tag_count = filtered_quotes.merge(quote_tag_df, left_index=True, right_on='quote_id')['tag_id'].value_counts().reset_index()
            else:
                tag_count = quote_tag_df['tag_id'].value_counts().reset_index()
            tag_count.columns = ['tag_id', 'count']
            tag_count = tag_count.merge(tags_df, left_on='tag_id', right_index=True)
            tag_count = tag_count[['tag', 'count']]
            fig_tag = px.bar(
                tag_count, 
                x='tag', 
                y='count', 
                title="Number of Quotes by Tag",
                color_discrete_sequence=['#FFA500']  # Color naranja
            )
            fig_tag.update_traces(marker=dict(
                color='rgba(255, 165, 0, 0.9)',  # Naranja con opacidad
                line=dict(color='rgba(255, 165, 0, 1.0)', width=2)
            ))

            fig_tag.update_layout(
                font=dict(size=16, color="#2C3E50"),  # Aumenta el tamaño y oscurece el color
                title_font=dict(size=20, color="#2C3E50"),  # Título más grande y oscuro
                xaxis=dict(tickfont=dict(size=14, color="#2C3E50")),  # Etiquetas del eje X más grandes y oscuras
                yaxis=dict(tickfont=dict(size=14, color="#2C3E50"))   # Etiquetas del eje Y más grandes y oscuras
            )

            st.plotly_chart(fig_tag, use_container_width=True)
        else:
            tag_count = filtered_quote_tag_df['tag_id'].value_counts().reset_index()
            tag_count.columns = ['tag_id', 'count']
            tag_count = tag_count.merge(tags_df, left_on='tag_id', right_index=True)
            tag_count = tag_count[['tag', 'count']]
            fig_tag = px.bar(
                tag_count, 
                x='tag', 
                y='count', 
                title="Number of Quotes by Tag",
                color_discrete_sequence=['#FFA500']  # Color naranja
            )
            fig_tag.update_traces(marker=dict(
                color='rgba(255, 165, 0, 0.8)',  # Naranja con opacidad
                line=dict(color='rgba(255, 165, 0, 1.0)', width=2)
            ))
            fig_tag.update_layout(
                font=dict(size=14),
                xaxis=dict(tickfont=dict(size=12, color="#2C3E50")),
                yaxis=dict(tickfont=dict(size=12, color="#2C3E50"))
            )
            st.plotly_chart(fig_tag, use_container_width=True)
    with col2:
        st.subheader("Top 10 Tags")
        if 'tag' in tag_count.columns:
            top_tags = tag_count.head(10)
            st.table(top_tags.set_index('tag') if show_index else top_tags)
        else:
            st.error("La columna 'tag' no está presente en tag_count.")

    # Custom CSS for background gradient and font size
    st.markdown("""
        <style>
            body {
                font-size: 16px;
            }
            .css-1d391kg {
                background-color: #F0F2F6;
            }
            .stMetric {
                background: linear-gradient(to right, #2ECC71, #ECF0F1);
                padding: 1rem;
                border-radius: 10px;
                color: #2C3E50;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                font-size: 1.2rem;
            }
            .css-1y0tads {
                gap: 2rem;
            }
            .stMarkdown h1 {
                color: #2C3E50;
                font-size: 2.5rem;
            }
            .stMarkdown h2 {
                color: #2C3E50;
                font-size: 2rem;
            }
            .stMarkdown h3 {
                color: #2C3E50;
                font-size: 1.5rem;
            }
            .stTable {
                width: 100%;
                font-size: 1.1rem;  # Aumenta el tamaño de la fuente
            }
            .stTable thead tr th {
                background-color: #2C3E50;
                color: white;
                font-size: 1.2rem;  # Aumenta el tamaño de la fuente del encabezado
            }
            .stTable tbody tr td {
                color: #000000;  # Cambia a negro para mayor contraste
                font-size: 1.1rem;
            }
            .stTable tbody tr:nth-of-type(even) {
                background-color: #D0D3D4;  # Fondo más oscuro para las filas pares
            }            
            .sidebar .sidebar-content {
                background-color: #F0F2F6;
                color: #2C3E50;
                font-size: 1.1rem;
            }
            .stSidebarHeader, .stSidebarButton {
                color: #1B2631;
                font-size: 1.2rem;
            }
            .stSelectbox, .stMultiselect {
                background-color: #ECF0F1;
                color: #1B2631;
                font-size: 1.1rem;
            }
            .stButton button {
                background-color: #E67E22;
                color: white;
                font-size: 1.1rem;
            }
            @media (max-width: 768px) {
                .css-1y0tads {
                    flex-direction: column;
                }
                .stMetric {
                    font-size: 1.3rem;
                }
            }
        </style>
    """, unsafe_allow_html=True)
