from selenium.webdriver.common.by import By
# No necesitamos importar 'webdriver' aquí.

def test_cart(login_in_driver):
    try:
        driver = login_in_driver
        
        # --- 1. CAPTURAR EL NOMBRE DEL PRODUCTO (Para la validación final) ---
        # El nombre del primer producto tiene la clase .inventory_item_name
        titulo_producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text

        # --- 2. AÑADIR AL CARRITO ---
        # SELECTOR CORREGIDO: .inventory_item button
        driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()

        # --- 3. VERIFICAR CONTADOR ---
        # SELECTOR CORREGIDO: shopping_cart_badge (usando By.CLASS_NAME, sin el punto)
        contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

        assert contador_carrito == "1", "❌ Error: El contador del carrito no es '1'."

        # --- 4. NAVEGAR AL CARRITO ---
        # SELECTOR CORREGIDO: shopping_cart_link (usando By.CLASS_NAME)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # --- 5. CAPTURAR TÍTULO EN EL CARRITO ---
        # SELECTOR CORREGIDO: .cart_item (la clase es 'cart', no 'card')
        titulo_productos_carritos = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
        
        # --- 6. ASERSION FINAL ---
        assert titulo_producto == titulo_productos_carritos, "❌ Error: El producto añadido no coincide con el producto en el carrito."

    except Exception as e:
        print(f"Error en test carrito: {e}")
        raise