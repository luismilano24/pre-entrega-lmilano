import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

import pathlib 
from datetime import datetime
import time

target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox") # github
    options.add_argument("--disable-gpu") # github
    options.add_argument("--window-size=1920,1080") # github
    options.add_argument("--headless=new") # github

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}

# conftest.py

import pytest
from datetime import datetime # ¡Asegúrate de importar esto!
import time # ¡Asegúrate de importar esto!
from pathlib import Path # ¡Necesario para 'target'!

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    
    # 2. DEFINE la variable 'report' a partir del resultado
    report = outcome.get_result()

    # 3. Solo procede si el test falló (FAILED) durante setup o call
    if report.when in ("setup", "call") and report.failed:
        
        # 4. Obtener la fixture 'driver' (Asume que está definida)
        driver = item.funcargs.get("driver", None) 

        if driver:            
            # Definir la carpeta target (ejemplo: guardar en reports/screenshots)
            target = Path(item.config.rootdir) / "reports" / "screenshots"
            target.mkdir(parents=True, exist_ok=True)
            
     
            nombre_base_del_test = item.function.__name__ 
            
            timestamp_unix = int(time.time()) 
            
   
            file_name = target / f"{report.when}_{nombre_base_del_test}_{timestamp_unix}.png"
            
            driver.save_screenshot(str(file_name))
        