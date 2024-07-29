import streamlit as st
import pandas as pd
import os

def show_logs_dashboard():
    # Ruta a los archivos de log
    log_path = os.path.join(os.path.dirname(__file__), '../data/logs/')
    log_file = os.path.join(log_path, 'webscraping.log')

    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            log_data = file.readlines()

        st.title('Dashboard de Logs')
        st.write('Estadísticas basadas en los logs.')

        log_info = [line for line in log_data if 'INFO' in line]
        log_errors = [line for line in log_data if 'ERROR' in line]

        st.write(f'Total Logs: {len(log_data)}')
        st.write(f'Total INFO: {len(log_info)}')
        st.write(f'Total ERROR: {len(log_errors)}')

        st.subheader('Detalles de Logs')
        log_type = st.selectbox('Selecciona el tipo de log', ['INFO', 'ERROR'])

        if log_type == 'INFO':
            st.write(log_info)
        else:
            st.write(log_errors)
    else:
        st.write('No se encontró el archivo de log.')
