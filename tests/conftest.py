# tests/conftest.py
import sys
import os

# Agregar el directorio src a la ruta de importación
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
