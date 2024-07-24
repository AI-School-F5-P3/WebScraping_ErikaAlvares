import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def clean_text(text):
    return re.sub(r'[^\x00-\x7F]+', '', text).strip()

def scrape_quotes():
    quotes = []
    authors = []
    tags = []

    # Realiza el web scraping (ajusta la URL y el scraping según tu necesidad)
    url = 'http://quotes.toscrape.com/'
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for quote in soup.select('.quote'):
            text = clean_text(quote.select_one('.text').get_text())
            author_name = clean_text(quote.select_one('.author').get_text())
            tags_list = [clean_text(tag.get_text()) for tag in quote.select('.tag')]
            quote_page = quote.select_one('a')['href']
            author_url = f"http://quotes.toscrape.com{quote_page}"
            author_response = requests.get(author_url)
            author_soup = BeautifulSoup(author_response.text, 'html.parser')
            born_date = clean_text(author_soup.select_one('.author-born-date').get_text())
            born_location = clean_text(author_soup.select_one('.author-born-location').get_text())
            description = clean_text(author_soup.select_one('.author-description').get_text())

            quotes.append((text, author_name, tags_list))
            authors.append((author_name, born_date, born_location, description))

        next_page = soup.select_one('.next > a')
        url = f"http://quotes.toscrape.com{next_page['href']}" if next_page else None

    quotes_df = pd.DataFrame(quotes, columns=['quote', 'author', 'tags'])
    authors_df = pd.DataFrame(authors, columns=['name', 'born_date', 'born_location', 'description']).drop_duplicates()

    return quotes_df, authors_df
