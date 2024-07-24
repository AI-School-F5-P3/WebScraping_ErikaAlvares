from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Conexión con la BD (modificada)
password = "root"
user = "root"
hostname = "127.0.0.1"
port = 3306
database = "quotes"

# Crear la base de datos y la conexión (sin SSL)
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}",
    pool_size=10,
    max_overflow=20
)
Base = declarative_base()

# Definir las tablas
quote_tag_association = Table(
    'quote_tag', Base.metadata,
    Column('quote_id', Integer, ForeignKey('quotes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    text = Column(Text)  # Cambiar a Text para permitir textos largos
    author = Column(String(255))
    author_born_date = Column(String(255))
    author_born_location = Column(String(255))
    author_description = Column(Text)  # Cambiar a Text para permitir descripciones largas
    tags = relationship('Tag', secondary=quote_tag_association, back_populates='quotes')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    quotes = relationship('Quote', secondary=quote_tag_association, back_populates='tags')

# Crear las tablas en la base de datos
Base.metadata.drop_all(engine)  # Borrar las tablas existentes
Base.metadata.create_all(engine)  # Crear las tablas con la nueva estructura

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()
