# src/scraping.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
from logging_config import logger  # gestión de logs

def clean_text(text):
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Elimina caracteres no ASCII
    text = re.sub(r'\s+', ' ', text)  # Reemplaza cualquier espacio en blanco (incluyendo nuevas líneas) por un espacio
    return text.strip()

def scrape_quotes():
    session = requests.Session()
    quotes = []
    authors = []
    tags = []
    quote_tag = []

    url = 'http://quotes.toscrape.com/'

    while url:
        try:
            response = session.get(url)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa
            soup = BeautifulSoup(response.text, 'html.parser')

            for quote in soup.select('.quote'):
                text = clean_text(quote.select_one('.text').get_text())
                author_name = clean_text(quote.select_one('.author').get_text())
                tags_list = [clean_text(tag.get_text()) for tag in quote.select('.tag')]
                quote_page = quote.select_one('a')['href']
                author_url = f"http://quotes.toscrape.com{quote_page}"
                author_response = session.get(author_url)
                author_response.raise_for_status()  # Verifica si la solicitud fue exitosa
                author_soup = BeautifulSoup(author_response.text, 'html.parser')
                born_date = clean_text(author_soup.select_one('.author-born-date').get_text())
                born_location = clean_text(author_soup.select_one('.author-born-location').get_text())
                description = clean_text(author_soup.select_one('.author-description').get_text())

                quotes.append((text, author_name, tags_list))
                authors.append((author_name, born_date, born_location, description))
                tags.extend(tags_list)

            next_page = soup.select_one('.next > a')
            url = f"http://quotes.toscrape.com{next_page['href']}" if next_page else None

            time.sleep(0.1)  # Ajusta según sea necesario

            logger.info(f'Scraped page: {response.url}')

        except requests.RequestException as e:
            logger.error(f"Error durante la solicitud HTTP: {e}")
            break
        except Exception as e:
            logger.error(f"Error durante el scraping: {e}")
            break

    quotes_df = pd.DataFrame(quotes, columns=['quote', 'author', 'tags'])
    authors_df = pd.DataFrame(authors, columns=['name', 'born_date', 'born_location', 'description']).drop_duplicates()
    tags_df = pd.DataFrame(tags, columns=['tag']).drop_duplicates()

    # Crear el DataFrame quote_tag_df
    quote_tag_data = []
    for quote_id, quote_row in quotes_df.iterrows():
        for tag in quote_row['tags']:
            tag_id = tags_df.index[tags_df['tag'] == tag].tolist()[0]
            quote_tag_data.append((quote_id, tag_id))
    
    quote_tag_df = pd.DataFrame(quote_tag_data, columns=['quote_id', 'tag_id'])

    logger.info('Scraping completed successfully.')
    return quotes_df, authors_df, tags_df, quote_tag_df
