import logging
import os
from logging.handlers import RotatingFileHandler

# Asegúrate de que el directorio de logs existe
log_directory = 'data/logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configuración del logger
logger = logging.getLogger('webscraping')
logger.setLevel(logging.DEBUG)

# Ruta del archivo de log
log_file = os.path.join(log_directory, 'webscraping.log')

# Crea un manejador de archivo con rotación
handler = RotatingFileHandler(log_file, maxBytes=2000, backupCount=5)
handler.setLevel(logging.DEBUG)

# Crea un formateador y lo añade al manejador
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Añade el manejador al logger
logger.addHandler(handler)

# Configura el logger de la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
