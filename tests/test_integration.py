import pytest
from src.db_setup import session, Author, Tag, Quote
from src.scraping import scrape_quotes
from src.data_processing import process_data

@pytest.fixture(scope='module')
def setup_database():
    quotes_df, authors_df = scrape_quotes()
    process_data(quotes_df, authors_df)
    yield
    session.query(Quote).delete()
    session.query(Tag).delete()
    session.query(Author).delete()
    session.commit()

def test_database_integration(setup_database):
    authors = session.query(Author).all()
    quotes = session.query(Quote).all()
    tags = session.query(Tag).all()
    
    assert len(authors) > 0
    assert len(quotes) > 0
    assert len(tags) > 0

  
