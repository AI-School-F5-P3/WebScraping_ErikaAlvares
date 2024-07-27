# tests/test_integration.py
import pytest
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db_setup import Author, Tag, Quote, quote_tag_table, engine, Base
from src.scraping import scrape_quotes
from src.data_processing import process_data
import pandas as pd
import time

# Conexión con la BD (modificada)
password = "root"
user = "root"
hostname = "127.0.0.1"
port = 3306
database = "quotes"

# Ajusta la configuración de la base de datos
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}",
    pool_recycle=3600,
    pool_timeout=60, 
    pool_size=10, 
    max_overflow=20, 
    isolation_level="AUTOCOMMIT"
)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def clear_tables(session):
    """Limpia las tablas de la base de datos."""
    session.execute(quote_tag_table.delete())
    session.query(Quote).delete()
    session.query(Author).delete()
    session.query(Tag).delete()
    session.commit()

def insert_test_data(session):
    """Inserta datos de prueba en la base de datos."""
    authors_data = [
        {"name": "Author 1", "born_date": "Date 1", "born_location": "Location 1", "description": "Description 1"},
        {"name": "Author 2", "born_date": "Date 2", "born_location": "Location 2", "description": "Description 2"},
    ]
    tags_data = ["tag1", "tag2", "tag3"]
    quotes_data = [
        {"text": "Sample quote 1", "author_name": "Author 1", "tags": ["tag1", "tag2"]},
        {"text": "Sample quote 2", "author_name": "Author 2", "tags": ["tag2", "tag3"]},
    ]

    # Verifica y agrega autores si no existen
    authors = []
    for author_data in authors_data:
        author = session.query(Author).filter_by(name=author_data["name"]).first()
        if not author:
            author = Author(**author_data)
            session.add(author)
        authors.append(author)

    # Verifica y agrega tags si no existen
    tags = []
    for tag_name in tags_data:
        tag = session.query(Tag).filter_by(name=tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
            session.add(tag)
        tags.append(tag)

    # Verifica y agrega quotes si no existen
    for quote_data in quotes_data:
        author = session.query(Author).filter_by(name=quote_data["author_name"]).first()
        if author:
            quote = session.query(Quote).filter_by(text=quote_data["text"], author=author).first()
            if not quote:
                quote_tags = [session.query(Tag).filter_by(name=tag_name).first() for tag_name in quote_data["tags"]]
                quote = Quote(text=quote_data["text"], author=author, tags=quote_tags)
                session.add(quote)

    session.commit()

@pytest.fixture(scope='function')
def db_session():
    """Fixture para gestionar la sesión de la base de datos."""
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    session.close()
    transaction.rollback()
    connection.close()

def test_integration(db_session):
    """Prueba de integración para verificar la funcionalidad end-to-end."""
    clear_tables(db_session)
    insert_test_data(db_session)

    with db_session.no_autoflush:
        quotes = db_session.query(Quote).all()
        authors = db_session.query(Author).all()
        tags = db_session.query(Tag).all()

        quotes_data = [{'quote': quote.text, 'author': quote.author.name, 'tags': [tag.name for tag in quote.tags]} for quote in quotes]
        authors_data = [{'name': author.name, 'born_date': author.born_date, 'born_location': author.born_location, 'description': author.description} for author in authors]
        tags_data = [{'tag': tag.name} for tag in tags]

        quotes_df = pd.DataFrame(quotes_data)
        authors_df = pd.DataFrame(authors_data)
        tags_df = pd.DataFrame(tags_data)

        retries = 3
        for attempt in range(retries):
            try:
                quotes_df, authors_df, tags_df, author_count, tag_count, quote_count = process_data(quotes_df, authors_df, tags_df)
                break
            except OperationalError as e:
                db_session.rollback()
                print(f"OperationalError caught: {e}")
                if attempt < retries - 1:
                    print("Retrying...")
                    time.sleep(5)  # Esperar antes de reintentar
                else:
                    pytest.fail(f"Test failed due to OperationalError: {e}")

    # Agregar impresiones para depuración
    print(f"author_count: {author_count}")
    print(f"tag_count: {tag_count}")
    print(f"quote_count: {quote_count}")

    # Verifica que los DataFrames no estén 
