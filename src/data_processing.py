import pandas as pd
from db_setup import Quote, Tag, session

def process_data(quotes_df):
    # Crear una lista de tuplas (quote, tag)
    quote_tags = []
    for index, row in quotes_df.iterrows():
        for tag in row['tags']:
            quote_tags.append((row['quote'], tag))

    # Crear un DataFrame a partir de la lista de tuplas
    quote_tags_df = pd.DataFrame(quote_tags, columns=['quote', 'tag'])

    # Insertar los datos en las tablas
    for index, row in quotes_df.iterrows():
        quote = Quote(
            text=row['quote'],
            author=row['author'],
            author_born_date=row['author_born_date'],
            author_born_location=row['author_born_location'],
            author_description=row['author_description']
        )
        session.add(quote)

    for tag_name in quote_tags_df['tag'].unique():
        tag = Tag(name=tag_name)
        session.add(tag)

    # Asociar las citas con las etiquetas
    for index, row in quote_tags_df.iterrows():
        quote = session.query(Quote).filter_by(text=row['quote']).first()
        tag = session.query(Tag).filter_by(name=row['tag']).first()
        quote.tags.append(tag)

    # Confirmar los cambios en la base de datos
    session.commit()
    print("Datos normalizados y guardados en la base de datos MySQL.")
