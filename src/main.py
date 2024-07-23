# Script principal para ejecutar todo el flujo de trabajo.

import pandas as pd
from data_processing import process_data

# Cargar el DataFrame desde el archivo CSV (este archivo debe estar en la carpeta 'data')
quotes_df = pd.read_csv('../data/quotes_pandas.csv')

# Procesar y guardar los datos
process_data(quotes_df)
