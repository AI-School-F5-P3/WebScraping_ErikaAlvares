
import logging
from logging.handlers import RotatingFileHandler

# Configurar el logger
logger = logging.getLogger('webscraping')
logger.setLevel(logging.DEBUG)

# Crear un manejador que escribe los logs en un archivo (con rotación)
handler = RotatingFileHandler('webscraping.log', maxBytes=2000, backupCount=5)
handler.setLevel(logging.DEBUG)

# Crear un formateador y agregarlo al manejador
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Agregar el manejador al logger
logger.addHandler(handler)
