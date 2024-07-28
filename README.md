# Documentación del Proyecto


## Proyecto de Web Scraping - FRONT-END

Dando secuencia al desarrollo del proyecto con web scrapping y atendendo a los requisitos de nivel medio desarrollaré este proyecto en la rama `frontend_streamlit` para que no se mezcle con los demás proyectos de niveles esencial, medio y avanzado.

## Nivel Experto
Para el nivel experto se pide:
- Dockerización del proyecto para asegurar un entorno de ejecución consistente.
- Implementación de un frontend básico para visualizar los datos extraídos. 
- Despliegue de la aplicación en un servidor web accesible públicamente. 
- Utilizar otras webs de frases para aumentar la cantidad de frases scrapeadas.


## Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:


### Descripción de Carpetas y Archivos


## Instalación y Configuración

### Requisitos

- Python 3.x
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

1. Configurar la conexión a la base de datos en `Github`:

    
## Ejecución del Proyecto


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
