import pandas as pd
from db_setup import Author, Tag, Quote, session

def process_data(quotes_df, authors_df):
    # Insertar autores en la tabla authors
    for index, row in authors_df.iterrows():
        author = Author(
            name=row['name'],
            born_date=row['born_date'],
            born_location=row['born_location'],
            description=row['description']
        )
        session.add(author)

    # Confirmar los cambios en la base de datos para obtener los IDs de los autores
    session.commit()

    # Crear un diccionario para mapear los nombres de los autores a sus IDs
    author_id_map = {author.name: author.id for author in session.query(Author).all()}

    # Insertar tags en la tabla tags
    unique_tags = set(tag for tags_list in quotes_df['tags'] for tag in tags_list)
    for tag_name in unique_tags:
        tag = Tag(name=tag_name)
        session.add(tag)

    # Confirmar los cambios en la base de datos para obtener los IDs de los tags
    session.commit()

    # Crear un diccionario para mapear los nombres de los tags a sus IDs
    tag_id_map = {tag.name: tag.id for tag in session.query(Tag).all()}

    # Insertar citas en la tabla quotes con las claves foráneas
    for index, row in quotes_df.iterrows():
        for tag in row['tags']:
            quote = Quote(
                text=row['quote'],
                author_id=author_id_map[row['author']],
                tag_id=tag_id_map[tag]
            )
            session.add(quote)

    # Confirmar los cambios en la base de datos
    session.commit()
    print("Datos normalizados y guardados en la base de datos MySQL.")
