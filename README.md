```markdown

# Documentación del proyecto

## erika_alvares_web_scraping
Proyecto de Web Scraping para una empresa fictícia llamada empresa XYZ Corp - Factoría F5.

## Proyecto de Web Scraping y Normalización de Datos

Este proyecto realiza web scraping en el sitio [Quotes to Scrape](http://quotes.toscrape.com/) para extraer citas, autores y etiquetas. Los datos son limpiados y normalizados antes de ser almacenados en una base de datos MySQL.

## Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:

```plaintext
Proyecto_WebScraping_ErikaAlvares/
│
├── WebScraping_ErikaAlvares/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── db_setup.py
│   │   ├── scraping.py
│   │   └── data_processing.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_data_processing.py
│   ├── venv/
│   ├── .gitignore
│   └── README.md
│
└── requirements.txt

### Descripción de Carpetas y Archivos

#### `src/`
Esta carpeta contiene el código fuente principal del proyecto.

- `__init__.py`: Indica que esta carpeta debe ser tratada como un módulo de Python.
- `main.py`: Es el punto de entrada del proyecto. Coordina el flujo del scraping y el procesamiento de datos.
- `db_setup.py`: Configura la base de datos y define los modelos de datos (tablas) utilizando SQLAlchemy.
- `scraping.py`: Contiene el código para realizar el web scraping en el sitio de citas y generar DataFrames con los datos extraídos.
- `data_processing.py`: Contiene el código para normalizar los datos extraídos y almacenarlos en la base de datos MySQL.

#### `tests/`
Esta carpeta contiene las pruebas del proyecto.

- `__init__.py`: Indica que esta carpeta debe ser tratada como un módulo de Python.
- `test_data_processing.py`: Contiene pruebas unitarias para verificar el correcto funcionamiento de las funciones de procesamiento de datos.

#### `venv/`
Esta carpeta contiene el entorno virtual para el proyecto, que incluye todas las dependencias instaladas necesarias para ejecutar el código. No es necesario modificar nada dentro de esta carpeta.

#### `.gitignore`
Archivo que especifica qué archivos y directorios deben ser ignorados por Git. Incluye cosas como archivos compilados de Python, el entorno virtual y archivos de configuración específicos del entorno.

#### `README.md`
Este archivo. Contiene la documentación del proyecto, incluyendo la descripción, instalación, configuración y ejecución.

#### `requirements.txt`
Archivo que lista todas las dependencias del proyecto. Estas dependencias pueden ser instaladas utilizando `pip install -r requirements.txt`.

## Instalación y Configuración

### Requisitos

- Python 3.x
- MySQL
- Virtualenv

### Instalación

1. Clonar el repositorio:

    ```sh
    git clone https://github.com/AI-School-F5-P3/WebScraping_ErikaAlvares.git
    cd WebScraping_ErikaAlvares
    ```

2. Crear y activar un entorno virtual:

    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # En Windows
    source venv/bin/activate  # En macOS y Linux
    ```

3. Instalar las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

### Configuración de la Base de Datos

1. Crear una base de datos en MySQL:

    ```sql
    CREATE DATABASE quotes;
    ```

2. Configurar la conexión a la base de datos en `db_setup.py`:

    ```python
    # Conexión con la BD (modificada)
    password = "root"
    user = "root"
    hostname = "127.0.0.1"
    port = 3306
    database = "quotes"
    ```

## Ejecución del Proyecto

1. Ejecutar el script principal para realizar el scraping, procesar los datos y almacenarlos en la base de datos:

    ```sh
    python src/main.py
    ```

## Descripción de los Archivos

- `src/main.py`: Punto de entrada del proyecto. Coordina el scraping y el procesamiento de datos.
- `src/db_setup.py`: Configura la base de datos y define los modelos de datos.
- `src/scraping.py`: Realiza el web scraping y genera DataFrames con los datos extraídos.
- `src/data_processing.py`: Normaliza los datos y los almacena en la base de datos.

## Estructura de la Base de Datos

- **authors**: Almacena los datos de los autores.
- **tags**: Almacena las etiquetas de las citas.
- **quotes**: Almacena las citas con claves foráneas a las tablas `authors` y `tags`.

## Ejemplo de la Estructura de las Tablas

### authors

| id  | name              | born_date   | born_location  | description                  |
| --- | ----------------- | ----------- | -------------- | ---------------------------- |
| 1   | Albert Einstein   | 14-03-1879  | Ulm, Germany   | Físico teórico               |
| 2   | Marilyn Monroe    | 01-06-1926  | The United States | Actriz, modelo y cantante  |

### tags

| id  | name              |
| --- | ----------------- |
| 1   | life              |
| 2   | love              |

### quotes

| id  | text                                            | author_id | tag_id |
| --- | ----------------------------------------------- | --------- | ------ |
| 1   | "La vida es lo que haces de ella..."            | 2         | 1      |
| 2   | "El amor es una fuerza más formidable..."       | 1         | 2      |

## Pruebas

Para ejecutar las pruebas, utiliza `pytest`. Las pruebas se encuentran en la carpeta `tests`.

```sh
pytest tests/
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para discutir cualquier cambio.

## Licencia

Este proyecto está bajo la Licencia MIT.
```

## Configuración de Docker

Para construir y ejecutar el contenedor Docker:

```sh
docker build -t my-project .
docker run -p 8501:8501 my-project

