import pytest
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from src.db_setup import session, Author, engine

def test_sql_injection():
    malicious_query = "INSERT INTO authors (name, born_date, born_location, description) VALUES ('Robert\'); DROP TABLE authors;--', '01-01-1970', 'Unknown', 'This is a test for SQL injection')"
    try:
        with engine.connect() as connection:
            connection.execute(malicious_query)
    except SQLAlchemyError as e:
        print("SQLAlchemyError caught:", e)
        assert True, "SQLAlchemyError caught as expected"
    else:
        assert False, "No exception raised for SQL injection"
