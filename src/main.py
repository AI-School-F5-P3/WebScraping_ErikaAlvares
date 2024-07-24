from scraping import scrape_quotes
from data_processing import process_data

def main():
    """
    Punto de entrada del programa. Realiza el scraping y procesa los datos.
    """
    # Realizar el web scraping y obtener los DataFrames (scraping.py)
    quotes_df, authors_df = scrape_quotes()

    # Procesar y guardar los datos en la base de datos (data_processing.py)
    process_data(quotes_df, authors_df)

if __name__ == '__main__':
    main()
