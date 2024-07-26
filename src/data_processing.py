import pandas as pd
from db_setup import Author, Tag, Quote, session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from logging_config import logger

def process_data(quotes_df, authors_df):
    """
    Procesa los DataFrames de citas y autores para almacenarlos en la base de datos.
    """
    try:
        # Inserta autores en la base de datos en lotes
        author_objects = [Author(
            name=row['name'],
            born_date=row['born_date'],
            born_location=row['born_location'],
            description=row['description']
        ) for index, row in authors_df.iterrows()]

        session.bulk_save_objects(author_objects, return_defaults=True)
        session.commit()
        logger.info('Authors inserted successfully.')

        # Crea un diccionario para mapear los nombres de los autores a sus IDs
        author_id_map = {author.name: author.id for author in session.query(Author).all()}

        # Inserta etiquetas en la base de datos en lotes
        unique_tags = set(tag for tags_list in quotes_df['tags'] for tag in tags_list)
        tag_objects = [Tag(name=tag_name) for tag_name in unique_tags]

        session.bulk_save_objects(tag_objects, return_defaults=True)
        session.commit()
        logger.info('Tags inserted successfully.')

        # Crea un diccionario para mapear los nombres de las etiquetas a sus IDs
        tag_id_map = {tag.name: tag.id for tag in session.query(Tag).all()}

        # Inserta citas en la base de datos en lotes con las claves foráneas
        quote_objects = []
        for index, row in quotes_df.iterrows():
            for tag in row['tags']:
                quote_objects.append(Quote(
                    text=row['quote'],
                    author_id=author_id_map[row['author']],
                    tag_id=tag_id_map[tag]
                ))

        session.bulk_save_objects(quote_objects)
        session.commit()
        logger.info('Quotes inserted successfully.')
        print("Datos normalizados y guardados en la base de datos MySQL.")
        
        return quotes_df, authors_df

    except IntegrityError as e:
        session.rollback()
        logger.error(f"Error de integridad en la base de datos: {e}")
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error de SQLAlchemy: {e}")
    except Exception as e:
        session.rollback()
        logger.error(f"Error al procesar los datos: {e}")
    
    return None, None  # En caso de error, devolver None

