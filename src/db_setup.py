# Este archivo contiene la configuración de la base de datos y las definiciones de los modelos. 

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
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
    text = Column(String)
    author = Column(String)
    author_born_date = Column(String)
    author_born_location = Column(String)
    author_description = Column(String)
    tags = relationship('Tag', secondary=quote_tag_association, back_populates='quotes')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    quotes = relationship('Quote', secondary=quote_tag_association, back_populates='tags')

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()
