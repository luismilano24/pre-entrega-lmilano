import pytest

# Lista de archivos a prueba a ejecutar
test_files = [
    "test/test_inventario.py",
    "test/test_login.py",
    "test/car"
]

# argunmentos para ejecutar las pruebas archivos + reportes html
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)

