# Documentación del proyecto

# erika_alvares_web_scraping
Proyecto de Web Scraping para una empresa fictícia llamada empresa XYZ Corp - Factoría F5.

# Web Scraping y Análisis de Citas

Este proyecto realiza web scraping, procesamiento y almacenamiento de datos de citas en una base de datos MySQL.

## Estructura de Carpetas

- `data/`: Archivos de datos (por ejemplo, CSVs).
- `notebooks/`: Notebooks de Jupyter.
- `src/`: Código fuente del proyecto.
- `tests/`: Pruebas del proyecto.
- `venv/`: Entorno virtual (ignorado por git).
- `.gitignore`: Archivos y carpetas a ignorar por git.
- `Dockerfile`: Configuración de Docker.
- `requirements.txt`: Dependencias del proyecto.
- `README.md`: Documentación del proyecto.

## Cómo ejecutar

1. Crear y activar un entorno virtual.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Ejecutar el script de procesamiento de datos con `python src/data_processing.py`.

## Configuración de Docker

Para construir y ejecutar el contenedor Docker:

```sh
docker build -t my-project .
docker run -p 8501:8501 my-project
