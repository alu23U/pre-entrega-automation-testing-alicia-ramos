from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options
import time



def test_carrito():
    
    options = Options()
    options.add_argument('--start-maximized') #Ventana grande
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5) #Espera implicita
    
    try:
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        #agregar la mochila al carrito
        
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary").click()
        #Verificar el numero en el badge del carrito
        
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        
        assert badge.text == "1"
        
        # ir al carrito
        driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        
        # verificar el nombre del producto en el carrito
        
        nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert nombre.text == "Sauce Labs Backpack"
        print('Carrito ok', badge)
    finally:
        driver.quit()        