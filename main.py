import streamlit as st
from streamlit_option_menu import option_menu
from app.sidebar import create_sidebar
from app.dashboard_quotes import show_quotes_dashboard
from app.dashboard_authors import show_authors_dashboard

# Configuración de la página para que ocupe todo el ancho
st.set_page_config(layout="wide")

# Configuración del menú
selected = option_menu(
    menu_title=None, 
    options=["Home", "Quotes", "Authors"], 
    icons=["house", "book", "person"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "green"}
    },
)

# Crear la barra lateral para todas las páginas y manejar los retornos según la página seleccionada
if selected == "Authors":
    selected_born_location, selected_authors, _, authors_df, quotes_df, tags_df, quote_tag_df = create_sidebar(selected)
elif selected == "Quotes":
    selected_authors, selected_tags, show_index, authors_df, quotes_df, tags_df, quote_tag_df = create_sidebar(selected)
else:
    authors_df, quotes_df, tags_df, quote_tag_df = create_sidebar(selected)

# Navegación entre pantallas
if selected == "Home":
    st.title("Web Scraping")
    st.markdown("""
        <style>
            .intro {
                font-size: 1.2rem;
                line-height: 1.6;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 1.2rem;
                color: white;
                background-color: green;
                border: none;
                border-radius: 5px;
                text-align: center;
                text-decoration: none;
                cursor: pointer;
            }
            .button:hover {
                background-color: #004d00;
            }
            .button-icon {
                margin-right: 8px;
            }
            .button:visited, .button:link, .button:hover, .button:active {
                color: white;
                text-decoration: none;
            }
        </style>
        <div class="intro">
            <p>Proyecto de Web Scraping y Normalización de Datos desarrollado para una empresa ficticia llamada empresa XYZ Corp.</p>
            <p>El trabajo consiste en realizar web scraping en el sitio Quotes to Scrape para extraer citas, autores y etiquetas. Los datos son limpiados y normalizados antes de ser almacenados en una base de datos MySQL. El proceso puede ser acompañado por la consola (terminal del computador).</p>
            <p>Cuando el proceso de scraping termina, da la opción de generar ficheros en formato .csv con los datos que han sido scrapeados.</p>
            <p>Una vez estando con los archivos en formato csv, se almacenan en Github y se queda disponible para la próxima etapa del proyecto que es la creación de un Front-End donde el usuario podrá tener acceso a sus datos.</p>
            <p>De momento no es posible subir la base de datos a la nube de Streamlit entonces decidí trabajar en esta plataforma con los archivos CSVs generados localmente.</p>
            <p>Dando secuencia al desarrollo del proyecto con web scrapping y atendiendo a los requisitos de nivel medio, dejaré este proyecto como público en Github y estará almacenada en la rama "frontend_streamlit" para que no se mezcle con los demás proyectos de niveles esencial, medio y avanzado sobre el mismo tema.</p>
            <a href="https://github.com/AI-School-F5-P3/WebScraping_ErikaAlvares/tree/frontend_streamlit" class="button" target="_blank">
                <svg class="button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="orange" d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.438 9.8 8.205 11.385.6.111.82-.26.82-.577 0-.285-.011-1.04-.017-2.04-3.338.726-4.042-1.613-4.042-1.613-.546-1.387-1.333-1.757-1.333-1.757-1.09-.745.083-.729.083-.729 1.204.084 1.838 1.237 1.838 1.237 1.07 1.834 2.809 1.305 3.492.998.107-.775.42-1.305.763-1.605-2.665-.305-5.467-1.333-5.467-5.932 0-1.31.468-2.381 1.236-3.221-.124-.304-.536-1.526.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.005.404 2.291-1.553 3.297-1.23 3.297-1.23.655 1.65.243 2.872.12 3.176.77.84 1.236 1.911 1.236 3.221 0 4.61-2.806 5.625-5.476 5.921.432.372.815 1.104.815 2.222 0 1.606-.015 2.896-.015 3.293 0 .32.216.694.824.576C20.565 21.796 24 17.308 24 12c0-6.63-5.37-12-12-12z"/></svg>
                Acceda al Github
            </a>
        </div>
        
    """, unsafe_allow_html=True)
elif selected == "Quotes":
    show_quotes_dashboard(selected_authors, selected_tags, show_index, authors_df, quotes_df, tags_df, quote_tag_df)
elif selected == "Authors":
    show_authors_dashboard(selected_born_location, selected_authors, authors_df, quotes_df)
