import pytest
import time
from src.scraping import scrape_quotes
from src.data_processing import process_data

def test_scraping_performance():
    start_time = time.time()
    quotes_df, authors_df = scrape_quotes()
    end_time = time.time()
    assert (end_time - start_time) < 60  # El tiempo de scraping debería ser menos de 60 segundos

def test_processing_performance():
    quotes_df, authors_df = scrape_quotes()
    start_time = time.time()
    process_data(quotes_df, authors_df)
    end_time = time.time()
    assert (end_time - start_time) < 60  # El tiempo de procesamiento debería ser menos de 60 segundos
