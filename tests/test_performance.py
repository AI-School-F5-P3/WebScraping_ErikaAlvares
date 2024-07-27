import pytest
import time
import sys
import os
import pandas as pd

# Agregar el directorio `src` al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scraping import scrape_quotes

def test_scraping_performance():
    start_time = time.time()
    quotes_df, authors_df, tags_df = scrape_quotes()
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time < 30  # Verifica que el scraping tome menos de 30 segundos

def test_processing_performance():
    from data_processing import process_data

    # Simula datos de entrada
    quotes_df = pd.DataFrame({
        'quote': ['Sample quote 1', 'Sample quote 2'],
        'author': ['Author 1', 'Author 2'],
        'tags': [['tag1', 'tag2'], ['tag2', 'tag3']]
    })
    authors_df = pd.DataFrame({
        'name': ['Author 1', 'Author 2'],
        'born_date': ['Date 1', 'Date 2'],
        'born_location': ['Location 1', 'Location 2'],
        'description': ['Description 1', 'Description 2']
    })
    tags_df = pd.DataFrame({
        'tag': ['tag1', 'tag2', 'tag3']
    })

    start_time = time.time()
    quotes_df, authors_df, tags_df, author_count, tag_count, quote_count = process_data(quotes_df, authors_df, tags_df)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time < 10  # Verifica que el procesamiento de datos tome menos de 10 segundos
