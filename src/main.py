from scraping import scrape_quotes
from data_processing import process_data
from logging_config import logger

def main():
    """
    Punto de entrada del programa. Realiza el scraping y procesa los datos.
    """
    try:
        # Realizar el web scraping y obtener los DataFrames
        quotes_df, authors_df = scrape_quotes()

        # Procesar y guardar los datos en la base de datos
        process_data(quotes_df, authors_df)
        logger.info('Proceso principal completado con éxito.')

    except Exception as e:
        logger.error(f"Error en el proceso principal: {e}")

if __name__ == '__main__':
    main()
