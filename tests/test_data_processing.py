# Pruebas para el procesamiento de datos

import pytest
import pandas as pd
from src.data_processing import process_data
from src.db_setup import session, Quote, Tag

@pytest.fixture
def quotes_df():
    data = {
        'quote': ['Quote 1', 'Quote 2'],
        'author': ['Author 1', 'Author 2'],
        'author_born_date': ['Date 1', 'Date 2'],
        'author_born_location': ['Location 1', 'Location 2'],
        'author_description': ['Description 1', 'Description 2'],
        'tags': ["['tag1', 'tag2']", "['tag3', 'tag4']"]
    }
    return pd.DataFrame(data)

def test_process_data(quotes_df):
    process_data(quotes_df)

    quotes_in_db = session.query(Quote).all()
    tags_in_db = session.query(Tag).all()

    assert len(quotes_in_db) == 2
    assert len(tags_in_db) == 4

    quote1 = session.query(Quote).filter_by(text='Quote 1').one()
    tag1 = session.query(Tag).filter_by(name='tag1').one()

    assert tag1 in quote1.tags

    session.query(Quote).delete()
    session.query(Tag).delete()
    session.commit()
