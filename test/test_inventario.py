from selenium.webdriver.common.by import By


# 'login_in_driver' Se ingresa al login.
def test_inventario(login_in_driver):
  
    # 1. llamada al login_in)
    driver = login_in_driver
    
    # 2. Validación de Título
    assert driver.title == "Swag Labs"
    print("Validacion de titulo")

    # 3. Validación de Productos 
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    # 4. Aserción de Presencia
    assert len(products) > 0, "No hay productos visibles en la pagina."
    print(f"Validación de Productos: Correcta. Se encontraron {len(products)} productos. ✅")

    # Opcional: Validar el primer producto para completar el ejercicio anterior
    primer_producto = products[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer Producto: Nombre={nombre}, Precio={precio}")
