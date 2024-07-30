

# Proyecto Web Scraping y Dashboard con Streamlit

Este proyecto realiza web scraping en el sitio Quotes to Scrape para extraer citas, autores y etiquetas. Los datos son limpiados y normalizados antes de ser almacenados en una base de datos MySQL. Luego, se crean visualizaciones y filtros en una aplicación Streamlit.

Este proyecto ha sido desplegado en la nube de Streamlit y esta configurado para acceder los archivos .CSV desde mí repositorio de Github. Toda vez que actualicemos los CSVs en Github se actualizará la aplicación en la nube automáticamente.

Para acceder al proyecto en la nube, acceda a la dirección: https://proyectowebscrapingerikaalvares.streamlit.app/

## Estructura del Proyecto

```
PROYECTO_WEBSCRAPING_ERIKAALVARES/
│
├── app/
│   ├── __init__.py
│   ├── dashboard_authors.py
│   ├── dashboard_quotes.py
│   └── sidebar.py
│
├── data/
│   ├── authors.csv
│   ├── quote_tag.csv
│   ├── quotes.csv
│   └── tags.csv
│
├── venv/
│
├── .streamlit/
│   └── config.toml
│
├── .gitignore
├── main.py
└── requirements.txt
```

## Instalación

1. Clona el repositorio a tu máquina local.
   ```bash
   git clone https://github.com/AI-School-F5-P3/WebScraping_ErikaAlvares.git
   ```

2. Navega al directorio del proyecto.
   ```bash
   cd PROYECTO_WEBSCRAPING_ERIKAALVARES
   ```

3. Crea y activa un entorno virtual (opcional pero recomendado).
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Windows: venv\Scripts\activate
   ```

4. Instala las dependencias.
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

1. Ejecuta la aplicación Streamlit.
   ```bash
   streamlit run main.py
   ```

2. Abre tu navegador y navega a `http://localhost:8501` para ver la aplicación en ejecución.

## Descripción de Funcionalidades

### Página Home

En la página de inicio, se presenta una introducción sobre el proyecto y un botón para acceder al repositorio de GitHub.

### Página Quotes

Esta página muestra un dashboard con las siguientes funcionalidades:
- Filtros por autores y etiquetas.
- Visualización de KPIs (Total Quotes, Total Authors, Total Tags).
- Gráficos interactivos que muestran el número de citas por autor y por etiqueta.
- Tabla de los 10 autores principales y las 10 etiquetas principales.

### Página Authors

Esta página muestra un dashboard con las siguientes funcionalidades:
- Filtros por ubicación de nacimiento y por nombre de autor.
- Detalles descriptivos de los autores filtrados, incluyendo su nombre, fecha de nacimiento, lugar de nacimiento y una descripción.

## Librerías Utilizadas

### Streamlit

Streamlit es una librería de Python que permite crear aplicaciones web interactivas y visualizaciones de datos de manera sencilla y rápida. En este proyecto, se utiliza para crear el frontend de la aplicación y mostrar los datos de manera interactiva.

### pandas

Pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos. En este proyecto, se utiliza para manipular los datos obtenidos del web scraping y preparar los datos para su visualización en la aplicación Streamlit.

### plotly

Plotly es una librería de visualización de datos que permite crear gráficos interactivos y dinámicos. En este proyecto, se utiliza para crear gráficos de barras que muestran el número de citas por autor y por etiqueta.

### streamlit_option_menu

Streamlit Option Menu es una librería que permite crear menús de navegación personalizados en Streamlit. En este proyecto, se utiliza para crear el menú horizontal que permite navegar entre las diferentes páginas de la aplicación.

### st_aggrid

st_aggrid es una librería que integra AG Grid, un componente de grilla de datos avanzado para la web, con Streamlit. Aunque no se utiliza en el código final del proyecto, es una opción útil para manejar y visualizar grandes conjuntos de datos de manera interactiva en aplicaciones Streamlit.

## Datos

Los datos utilizados en este proyecto se obtienen del sitio Quotes to Scrape mediante web scraping. Los archivos CSV generados contienen información sobre citas, autores y etiquetas, y se almacenan en la carpeta `data` del proyecto:

- `authors.csv`: Contiene información sobre los autores.
- `quote_tag.csv`: Contiene la relación entre citas y etiquetas.
- `quotes.csv`: Contiene las citas extraídas.
- `tags.csv`: Contiene las etiquetas asociadas a las citas.

## Desarrollado por

Este proyecto fue desarrollado por [Erika Alvares](https://www.erikaalvares.es).

---


## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para discutir cualquier cambio.
¡Entra en mi web [https://www.erikaalvares.es](https://www.erikaalvares.es) y contacta conmigo!

## Licencia
Este proyecto está bajo la Licencia MIT.