import pytest
import pandas as pd
from db_setup import session, Author, Tag, Quote
from data_processing import process_data

@pytest.fixture
def sample_quotes_df():
    return pd.DataFrame({
        'quote': ['Sample quote 1', 'Sample quote 2'],
        'author': ['Author 1', 'Author 2'],
        'tags': [['tag1', 'tag2'], ['tag2', 'tag3']]
    })

@pytest.fixture
def sample_authors_df():
    return pd.DataFrame({
        'name': ['Author 1', 'Author 2'],
        'born_date': ['Date 1', 'Date 2'],
        'born_location': ['Location 1', 'Location 2'],
        'description': ['Description 1', 'Description 2']
    })

@pytest.fixture
def sample_tags_df():
    return pd.DataFrame({
        'tag': ['tag1', 'tag2', 'tag3']
    })

def test_process_data(sample_quotes_df, sample_authors_df, sample_tags_df):
    # Ejecuta el proceso de datos en los DataFrames de ejemplo
    quotes_df, authors_df, tags_df, author_count, tag_count, quote_count = process_data(sample_quotes_df, sample_authors_df, sample_tags_df)

    # Afirmaciones para verificar el procesamiento correcto de los datos
    assert quotes_df is not None
    assert authors_df is not None
    assert tags_df is not None
    assert author_count >= 0
    assert tag_count >= 0
    assert quote_count >= 0
