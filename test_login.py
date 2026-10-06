from selenium import webdriver #Importa selenium para manejar el navegador
from selenium.webdriver.common.by import By #Importa By para buscar por ID,  XPATH, etc
import time #Para hacer pausas

def test_login_exitoso():
    #1. Creamos el navegador Chrome
    driver = webdriver.Chrome()
    try:
        #2. Abrimos la paginade Swag Labs
        driver.get("https://www.saucedemo.com")
        #3. Buscamos la caja de usuario y escribimos standar_user
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        #4. Buscamos la caja de contraseña y escribimos secret_sauce
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        #5.Hacemos click en el boton de login
        driver.find_element(By.ID, "login-button").click()
        #6. Esperamos 2 segundos a que cargue la pagina siguiente
        time.sleep(2)
        #7. Verificamos que realmente entramos al inventario
        # Si la url contine /inventory.html entonces el login funciono
        assert "/inventory.html" in driver.current_url
        print("Login OK")
    finally:
        #8. Siempre al final, cerramos el navegador
        driver.quit()