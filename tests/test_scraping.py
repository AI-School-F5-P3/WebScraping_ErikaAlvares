import pytest
import sys
import os

# Agregar el directorio `src` al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scraping import clean_text, scrape_quotes

def test_clean_text():
    assert clean_text('Hello, World!') == 'Hello, World!'
    assert clean_text('Hello,\nWorld!') == 'Hello, World!'
    assert clean_text('Hello,\tWorld!') == 'Hello, World!'
    assert clean_text('Hello,  World!') == 'Hello, World!'

# @pytest.mark.skip(reason="Requiere conexión a internet y puede ser inestable")
def test_scrape_quotes():
    quotes_df, authors_df = scrape_quotes()
    assert not quotes_df.empty
    assert not authors_df.empty
    assert 'quote' in quotes_df.columns
    assert 'author' in quotes_df.columns
    assert 'tags' in quotes_df.columns
    assert 'name' in authors_df.columns
    assert 'born_date' in authors_df.columns
    assert 'born_location' in authors_df.columns
    assert 'description' in authors_df.columns
