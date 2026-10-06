from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options
import time



def test_carrito():
    #1 Cofiguramos Chrome
    
    options = Options()
    options.add_argument('--start-maximized') # Ventana grande
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5) # Espera implicita
    
    try:
        #2 Login
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        #3 Agregar la mochila al carrito
        #4 Buscamos el boton ADD TO CART
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary").click()
        #4 Verificar el numero en el badge del carrito
        # Guardamos el texto enseguida para que no se venza
        
        texto_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        
        
        assert texto_badge == "1" # tiene que decir 1
        
        #5 Ir al carrito
        driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        
        #6 Verificar que el nombre del producto este en el carrito
        
        nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert nombre.text == "Sauce Labs Backpack"
        print('Carrito ok', texto_badge)
    finally:
        #7 Cerramos todo
        driver.quit()        