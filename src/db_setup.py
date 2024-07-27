# src/db_setup.py
from sqlalchemy import create_engine, Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from logging_config import logger

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)  # Agrega longitud a VARCHAR
    born_date = Column(String(255))  # Agrega longitud a VARCHAR
    born_location = Column(String(255))  # Agrega longitud a VARCHAR
    description = Column(Text)  # Cambia a TEXT para permitir descripciones largas
    quotes = relationship("Quote", back_populates="author")

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)  # Agrega longitud a VARCHAR
    quotes = relationship("Quote", secondary="quote_tag", back_populates="tags")

quote_tag_table = Table('quote_tag', Base.metadata,
    Column('quote_id', Integer, ForeignKey('quotes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    text = Column(Text)  # Cambia a TEXT para permitir textos largos
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="quotes")
    tags = relationship("Tag", secondary=quote_tag_table, back_populates="quotes")


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
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
