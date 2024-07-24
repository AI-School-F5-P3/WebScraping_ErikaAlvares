import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

def clean_text(text):
    """
    Limpia el texto eliminando caracteres no ASCII.
    """
    return re.sub(r'[^\x00-\x7F]+', '', text).strip()

def scrape_quotes():
    """
    Realiza el web scraping de la página de citas (quotes) y devuelve dos DataFrames:
    uno con las citas (quotes) y otro con los autores (authors).
    """
    # Utiliza una sesión para mantener conexiones persistentes
    session = requests.Session()
    quotes = []
    authors = []
    tags = []

    # URL inicial
    url = 'http://quotes.toscrape.com/'
    while url:
        # Realiza la solicitud HTTP
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrae las citas y la información de los autores
        for quote in soup.select('.quote'):
            text = clean_text(quote.select_one('.text').get_text())
            author_name = clean_text(quote.select_one('.author').get_text())
            tags_list = [clean_text(tag.get_text()) for tag in quote.select('.tag')]
            quote_page = quote.select_one('a')['href']
            author_url = f"http://quotes.toscrape.com{quote_page}"
            author_response = session.get(author_url)
            author_soup = BeautifulSoup(author_response.text, 'html.parser')
            born_date = clean_text(author_soup.select_one('.author-born-date').get_text())
            born_location = clean_text(author_soup.select_one('.author-born-location').get_text())
            description = clean_text(author_soup.select_one('.author-description').get_text())

            quotes.append((text, author_name, tags_list))
            authors.append((author_name, born_date, born_location, description))

        # Encuentra el enlace a la siguiente página
        next_page = soup.select_one('.next > a')
        url = f"http://quotes.toscrape.com{next_page['href']}" if next_page else None

        # Reduce la latencia entre solicitudes
        time.sleep(0.1)  # Ajusta según sea necesario

    # Crea DataFrames a partir de las listas recopiladas
    quotes_df = pd.DataFrame(quotes, columns=['quote', 'author', 'tags'])
    authors_df = pd.DataFrame(authors, columns=['name', 'born_date', 'born_location', 'description']).drop_duplicates()

    return quotes_df, authors_df
