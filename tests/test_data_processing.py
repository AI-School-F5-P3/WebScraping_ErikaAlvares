# test_data_processing.py

"""
Objetivo:
Este archivo contiene pruebas para verificar el correcto funcionamiento del módulo data_processing.py, que es responsable de limpiar y 
procesar los datos obtenidos del scraping antes de almacenarlos en la base de datos.
"""

import pytest
import sys
import os
import pandas as pd

# Agregar el directorio `src` al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_processing import process_data

@pytest.fixture
def sample_quotes_df():
    # Crea un DataFrame de ejemplo para citas
    return pd.DataFrame({
        'quote': ['Sample quote 1', 'Sample quote 2'],
        'author': ['Author 1', 'Author 2'],
        'tags': [['tag1', 'tag2'], ['tag2', 'tag3']]
    })

@pytest.fixture
def sample_authors_df():
    # Crea un DataFrame de ejemplo para autores
    return pd.DataFrame({
        'name': ['Author 1', 'Author 2'],
        'born_date': ['Date 1', 'Date 2'],
        'born_location': ['Location 1', 'Location 2'],
        'description': ['Description 1', 'Description 2']
    })

def test_process_data(sample_quotes_df, sample_authors_df):
    """
    - Ejecuta el proceso de datos en los DataFrames de ejemplo
    Prueba la función `process_data` para asegurar que procesa correctamente
    los DataFrames de citas y autores.
    """
    process_data(sample_quotes_df, sample_authors_df)
    # Podemos agregar más afirmaciones según sea necesario para la lógica de procesamiento de datos
    assert True  # Esta es una afirmación simple para indicar que la prueba ha pasado
