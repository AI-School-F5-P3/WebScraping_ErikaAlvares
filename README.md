# Documentación del Proyecto

## WebScraping_ErikaAlvares
Proyecto desarrollado para una empresa ficticia llamada empresa XYZ Corp.

## Proyecto de Web Scraping y Normalización de Datos

Este proyecto realiza web scraping en el sitio [Quotes to Scrape](http://quotes.toscrape.com/) para extraer citas, autores y etiquetas. Los datos son limpiados y normalizados antes de ser almacenados en una base de datos MySQL.

## Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:

```plaintext
Proyecto_WebScraping_ErikaAlvares/
│
├── WebScraping_ErikaAlvares/
│   ├── data/
│   │   ├── authors.csv
│   │   ├── quotes.csv
│   │   └── tags.csv
│   ├── notebooks/
│   │   └── web_scraping_quotes.ipynb
│   ├── src/
│   │   ├── __init__.py
│   │   ├── data_processing.py
│   │   ├── db_setup.py
│   │   ├── logging_config.py
│   │   ├── main.py
│   │   ├── scraping.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_data_processing.py
│   │   ├── test_integration.py
│   │   ├── test_performance.py
│   │   ├── test_scraping.py
│   │   └── test_security.py
│   ├── .gitignore
│   ├── README.md
│   ├── requirements.txt
│   └── webscraping.log
└── venv
```

### Descripción de Carpetas y Archivos

#### `venv/`
Esta carpeta contiene el entorno virtual para el proyecto, que incluye todas las dependencias instaladas necesarias para ejecutar el código. No es necesario modificar nada dentro de esta carpeta. 
La he creado y nombrado `venv/` a la hora de crear mi entorno virtual y no la subiré a mi repositório en Github pero es una buena práctica trabajar con entornos virtuales desde tu máquina local.

#### `src/`
Esta carpeta contiene el código fuente principal del proyecto.

- `__init__.py`: Indica que esta carpeta debe ser tratada como un módulo de Python.
- `main.py`: Es el punto de entrada del proyecto. Coordina el flujo del scraping, procesamiento de datos y almacenamiento en la base de datos.
- `db_setup.py`: Configura la base de datos y define los modelos de datos (tablas) utilizando SQLAlchemy.
- `scraping.py`: Contiene el código para realizar el web scraping en el sitio de citas y generar DataFrames con los datos extraídos.
- `data_processing.py`: Contiene el código para normalizar los datos extraídos y almacenarlos en la base de datos MySQL.
- `logging_config.py`: Configura el sistema de logs para registrar la ejecución del proceso.

#### `tests/`
Esta carpeta contiene las pruebas del proyecto.

- `__init__.py`: Indica que esta carpeta debe ser tratada como un módulo de Python.
- `test_scraping.py`: Contiene pruebas unitarias para verificar el correcto funcionamiento de las funciones de scraping.
- `test_data_processing.py`: Contiene pruebas unitarias para verificar el correcto funcionamiento de las funciones de procesamiento de datos.
- `test_integration.py`: Contiene pruebas para verificar la integración de diferentes partes del sistema.
- `test_performance.py`: Contiene pruebas para medir el rendimiento de las funciones.
- `test_security.py`: Contiene pruebas para verificar la seguridad del sistema, como la prevención de inyecciones SQL.

#### `data/`
Esta carpeta contiene los archivos CSV generados después del procesamiento de datos.

#### `.gitignore`
Archivo que especifica qué archivos y directorios deben ser ignorados por Git. Incluye cosas como archivos compilados de Python, el entorno virtual, archivos de configuración específicos del entorno y archivos de log.

#### `README.md`
Este archivo contiene la documentación del proyecto, incluyendo la descripción, instalación, configuración y ejecución.

#### `requirements.txt`
Archivo que lista todas las dependencias del proyecto. Estas dependencias pueden ser instaladas utilizando `pip install -r requirements.txt`.

## Instalación y Configuración

### Requisitos

- Python 3.x
- MySQL
- Módulo venv de Python

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

2. Ejemplo de Salida Esperada desde la CONSOLA

```plaintext
Título: PROCESO DE WEB SCRAPING
El proceso de Web Scraping acaba de empezar – 2024-07-26 17:07:41
El proceso de Web Scraping acaba de finalizar – 2024-07-26 17:08:05
Resumen Proceso de Web Scraping
Han sido scrapeado(s) 100 registro(s) al total

El proceso de Limpieza de los datos acaba de empezar – 2024-07-26 17:08:05
Datos normalizados y guardados en la base de datos MySQL.
El proceso de Limpieza acaba de finalizar – 2024-07-26 17:08:05
Han sido limpiado(s) 100 registro(s) al total
Han sido separado(s) lo(s) dato(s) de cita(s) en un dataframe 'Quotes'
Han sido separado(s) lo(s) dato(s) de autor(es) en un dataframe 'Authors'
Han sido separado(s) lo(s) dato(s) de etiqueta(s) en un dataframe 'Tags'
Al total han sido importados:
- 100 Quotes
- 50 Authors
- 6 Tags
¿Deseas generar un archivo .csv para Quotes, Authors y Tags? (S/N): S
Los archivos CSV han sido generados en la carpeta 'data'.

```

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

## Sistema de Logging

El sistema de logging está configurado para registrar la ejecución del proceso en un archivo `webscraping.log`. Los logs se rotan después de alcanzar un tamaño máximo de 2000 bytes, con hasta 5 archivos de respaldo. El archivo `.gitignore` está configurado para excluir estos archivos de log.

## Pruebas

### Tipos de Pruebas Realizadas

#### `test_scraping.py`
- **Objetivo**: Verificar el correcto funcionamiento de las funciones de scraping.
- **Pruebas realizadas**: 
  - `test_clean_text()`: Verifica la limpieza del texto eliminado caracteres innecesarios.
  - `test_scrape_quotes()`: Verifica que la función de scraping devuelve datos no vacíos y con las columnas esperadas.

#### `test_data_processing.py`
- **Objetivo**: Verificar el correcto funcionamiento de las funciones de procesamiento de datos.
- **Pruebas

 realizadas**:
  - `test_process_data()`: Verifica que los datos se procesan y almacenan correctamente en la base de datos.

#### `test_integration.py`
- **Objetivo**: Verificar la integración de diferentes partes del sistema.
- **Pruebas realizadas**:
  - `test_integration()`: Verifica que las distintas partes del sistema funcionan correctamente juntas.

#### `test_performance.py`
- **Objetivo**: Medir el rendimiento de las funciones.
- **Pruebas realizadas**:
  - `test_performance()`: Verifica que las funciones se ejecutan en un tiempo aceptable.

#### `test_security.py`
- **Objetivo**: Verificar la seguridad del sistema, como la prevención de inyecciones SQL.
- **Pruebas realizadas**:
  - `test_sql_injection()`: Verifica que el sistema es resistente a inyecciones SQL.

### Ejecución de Pruebas

Para ejecutar las pruebas, utiliza `pytest`. Las pruebas se encuentran en la carpeta `tests`.

```sh
pytest tests/
```

### Interpretación de los Resultados de las Pruebas

Cuando ejecutas las pruebas, verás algo como esto:

```plaintext
========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.12.4, pytest-8.3.1, pluggy-1.5.0
rootdir: C:\Users\erika\Documents\github\Proyecto_WebScraping_ErikaAlvares\WebScraping_ErikaAlvares
plugins: mock-3.14.0
collected 7 items

test_data_processing.py .                                                                                                                                           [ 14%]
test_integration.py .                                                                                                                                               [ 28%]
test_performance.py ..                                                                                                                                              [ 57%]
test_scraping.py ..                                                                                                                                                 [ 85%]
test_security.py .                                                                                                                                                  [100%]

===================================================================== 7 passed in 100.82s (0:01:40) ======================================================================
```

- Los números entre corchetes (`[14%]`, `[28%]`, etc.) indican el progreso de la ejecución de los tests, no el porcentaje de éxito. Cada número indica el porcentaje de tests que se han ejecutado en relación con el total.
- El hecho de que todos los tests hayan pasado (`7 passed`) confirma que no hubo fallos en ninguno de los tests.

## Archivo .gitignore

El archivo `.gitignore` contiene las siguientes entradas para asegurar que los archivos y directorios innecesarios no se incluyan en el repositorio:

```plaintext
# Ignorar archivos de log generados por logging_config.py
webscraping.log
webscraping.log.*
```

# Ignorar entorno virtual
```
venv/
```

# Ignorar archivos de caché de Python
```
__pycache__/
*.pyc
```

# Ignorar archivos de datos y de log generados
```
data/*.csv

webscraping.log
webscraping.log.*
```

## Configuración de Docker

Para construir y ejecutar el contenedor Docker:

```sh
docker build -t my-project .
docker run -p 8501:8501 my-project
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para discutir cualquier cambio.
¡Entra en mi web [https://www.erikaalvares.es](https://www.erikaalvares.es) y contacta conmigo!

## Licencia
Este proyecto está bajo la Licencia MIT.
