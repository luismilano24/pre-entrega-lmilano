# conftest.py (¡Estructura Final Correcta!)

import sys
import os
import pytest
from selenium import webdriver
# Nota: Quitamos la importación fallida de aquí por ahora.

# 1. Bloque CRÍTICO: Debe ejecutarse PRIMERO
###############################################################
# os.path.dirname(__file__) es la ruta de la carpeta 'test'
# os.path.join(..., '..') sube un nivel a la carpeta 'preentrega-lmilano'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Insertar la ruta raíz en el PATH de Python
sys.path.insert(0, project_root)
###############################################################

# 2. Importación LOCAL: Ahora funcionará
from utils.login import login # <-- ¡Ahora el sys.path está listo!


# ------------------------------------------------------------------
# Fixtures (NO NECESITAN CAMBIOS)

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito") 
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
