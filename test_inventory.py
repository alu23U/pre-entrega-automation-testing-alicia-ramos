from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_inventory():
    driver = webdriver.Chrome()
    try:
        # Entramos a la pagina 
        driver.get("https://www.saucedemo.com")
        # primero hacemos login porque para poder ver el inventario       
        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")
                
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()
        # Verificamos que el titulo de la pagina sea Swa Labs
        assert driver.title == "Swag Labs"
        # Buscamos cuantos productos hay en la lista
        #find_element trae todos los que tengan esa clase       
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        # Verificamos que al menos haya un producto cargado
        # Si la lista esta vacia, el test falla
        assert len(productos) > 0
        # Tomamos el primer producto de lista
        primer_producto = productos[0]
        # Dentro de ese primer producto buscaos su nombre nombre_producto = primer:producto.findelement(By.Class_NAME, "inventory_item_name").text
        nomre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text 
        # Dentro del mismo producto buscamos su precio 
        precio_producto = primer_producto.find_element(By.CLASS_NAME,"inventory_item_price").text
        # Verificamos que el nombre sea el esperado
        assert nomre_producto == "Sauce Labs Backpack"
        # Verificamos que el precio sea el esperado
        assert precio_producto == "$29.99"
        # Buscamos el menu hamburguesa (las tres rayitas)
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        # Verificamos que el menu se vea en la pantalla
        assert menu.is_displayed()
        # Buscamos el filtro para ordenar el producto de (A-Z, precio)
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        # Verificamos que el fitro tambie se visualize
        assert filtro.is_displayed()
    
    finally:
        # Siempre cerramos el navegador, aunque algo falle
        driver.quit()    
