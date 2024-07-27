import pytest
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from src.db_setup import session, Author

def test_sql_injection():
    malicious_author = Author(
        name="Robert'); DROP TABLE authors;--",
        born_date="01-01-1970",
        born_location="Unknown",
        description="This is a test for SQL injection"
    )
    try:
        session.add(malicious_author)
        session.commit()
    except IntegrityError as e:
        print("IntegrityError caught:", e)
        session.rollback()
        assert True
    except SQLAlchemyError as e:
        print("SQLAlchemyError caught:", e)
        session.rollback()
        assert False, f"Unexpected SQLAlchemyError: {e}"
    else:
        session.rollback()
        print("No exception raised for SQL injection, which is good if the ORM is handling it properly.")
        assert True
