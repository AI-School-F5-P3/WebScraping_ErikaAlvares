from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
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

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    born_date = Column(String(255))
    born_location = Column(String(255))
    description = Column(Text)

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    author_id = Column(Integer, ForeignKey('authors.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
    author = relationship('Author', back_populates='quotes')
    tag = relationship('Tag', back_populates='quotes')

Author.quotes = relationship('Quote', order_by=Quote.id, back_populates='author')
Tag.quotes = relationship('Quote', order_by=Quote.id, back_populates='tag')

# Crear las tablas en la base de datos
Base.metadata.drop_all(engine)  # Borrar las tablas existentes
Base.metadata.create_all(engine)  # Crear las tablas con la nueva estructura

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()
