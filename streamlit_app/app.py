import streamlit as st  # Importa el módulo Streamlit para crear la interfaz web.
from dashboard import show_dashboard  # Importa la función show_dashboard desde el módulo dashboard.py.
from logs_dashboard import show_logs_dashboard  # Importa la función show_logs_dashboard desde el módulo logs_dashboard.py.
from random_quote import show_random_quote  # Importa la función show_random_quote desde el módulo random_quote.py.
from dashboard_quotes import show_dashboard_quotes
from new_menu import show_new_menu  # Importa la función show_new_menu desde el módulo new_menu.py.


# Crea una barra lateral con opciones de navegación.
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a", ["Dashboard", "Logs", "Cita Aleatoria", "Dashboard - Quotes", "Nuevo Menú"])  # Agrega una nueva opción "Nuevo Menú".

# Redirige a la página seleccionada en el menú.
if page == "Dashboard":
    show_dashboard()  # Muestra el dashboard principal.
elif page == "Logs":
    show_logs_dashboard()  # Muestra el dashboard de logs.
elif page == "Cita Aleatoria":
    show_random_quote()  # Muestra la página de citas aleatorias.
elif page == "Dashboard - Quotes":
    show_dashboard_quotes()
elif page == "Nuevo Menú":
    show_new_menu()  # Muestra la nueva página del menú.
