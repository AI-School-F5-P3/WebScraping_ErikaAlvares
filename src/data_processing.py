# src/data_processing.py
import logging
from logging_config import logger
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # Asegúrate de importar SQLAlchemyError
from db_setup import session, Author, Tag, Quote

logger = logging.getLogger('webscraping')

def process_data(quotes_df, authors_df, tags_df):
    try:
        author_count = 0
        tag_count = 0
        quote_count = 0

        for index, row in authors_df.iterrows():
            author = session.query(Author).filter_by(name=row['name']).first()
            if not author:
                author = Author(
                    name=row['name'],
                    born_date=row['born_date'],
                    born_location=row['born_location'],
                    description=row['description']
                )
                session.add(author)
                author_count += 1

        session.commit()

        for index, row in tags_df.iterrows():
            tag = session.query(Tag).filter_by(name=row['tag']).first()
            if not tag:
                tag = Tag(name=row['tag'])
                session.add(tag)
                tag_count += 1

        session.commit()

        for index, row in quotes_df.iterrows():
            author = session.query(Author).filter_by(name=row['author']).first()
            quote = session.query(Quote).filter_by(text=row['quote']).first()
            if not quote:
                quote = Quote(
                    text=row['quote'],
                    author=author
                )
                session.add(quote)
                quote_count += 1

                for tag_name in row['tags']:
                    tag = session.query(Tag).filter_by(name=tag_name).first()
                    quote.tags.append(tag)

        session.commit()

        logger.info(f"Total Authors: {author_count + session.query(Author).count()}, Imported: {author_count}, Existing: {session.query(Author).count() - author_count}")
        logger.info(f"Total Tags: {tag_count + session.query(Tag).count()}, Imported: {tag_count}, Existing: {session.query(Tag).count() - tag_count}")
        logger.info(f"Total Quotes: {quote_count + session.query(Quote).count()}, Imported: {quote_count}, Existing: {session.query(Quote).count() - quote_count}")

        return quotes_df, authors_df, tags_df, author_count, tag_count, quote_count
    except IntegrityError as e:
        logger.error(f"Error de integridad al procesar los datos: {e}")
        session.rollback()
        return None, None, None, 0, 0, 0
    except SQLAlchemyError as e:  # Asegúrate de que esta línea esté correcta
        logger.error(f"Error en el proceso principal: {e}")
        session.rollback()
        return None, None, None, 0, 0, 0
