from scraping import scrape_quotes
from data_processing import process_data
from logging_config import logger
from termcolor import colored
import time

def main():
    try:
        start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(colored(f"Título: PROCESO DE WEB SCRAPING\nEl proceso de Web Scraping acaba de empezar – {start_time}", 'green'))

        quotes_df, authors_df, tags_df, quote_tag_df = scrape_quotes()

        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(colored(f"El proceso de Web Scraping acaba de finalizar – {end_time}", 'green'))
        print(colored(f"Resumen Proceso de Web Scraping\nHan sido scrapeado(s) {len(quotes_df)} registro(s) al total\n", 'yellow'))

        start_clean_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(colored(f"El proceso de Limpieza de los datos acaba de empezar – {start_clean_time}", 'green'))

        quotes_df, authors_df, tags_df, author_count, tag_count, quote_count = process_data(quotes_df, authors_df, tags_df)

        end_clean_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(colored(f"El proceso de Limpieza acaba de finalizar – {end_clean_time} \n", 'green'))

        response = input("¿Deseas generar un archivo .csv para Quotes, Authors, Tags y Quote_Tag? (S/N): ")
        if response.lower() == 's':
            quotes_df.to_csv('data/quotes.csv', index=False)
            authors_df.to_csv('data/authors.csv', index=False)
            tags_df.to_csv('data/tags.csv', index=False)
            quote_tag_df.to_csv('data/quote_tag.csv', index=False)  # Exportar quote_tag_df
            print(colored("Los archivos CSV han sido generados en la carpeta 'data'.", 'green'))
        else:
            print(colored("No se generaron archivos CSV.", 'red'))

    except Exception as e:
        logger.error(f"Error en el proceso principal: {e}")
        print(colored(f"Error en el proceso principal: {e}", 'red'))

if __name__ == '__main__':
    main()
