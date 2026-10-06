# Preentregaauto Automatizacion QA - Selenium y Pytest
Proyecto de automatizacion de pruebas para https://www.saucedemo.com usando Selenium y Pytest

## Tegnologias utilidas
-Python
-Selenium 4.x
-Pytest 9.x
-Pytest-html (para reporte)
-Git
-Github

## Estructura del proyecto/
preentregaauto/
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt
├── test_login.py
├── test_inventory.py
├── test_carrito.py
├── informes/
└── reports/
    └── reporte.html

## instalacion
 ```
 pip install -r requirements.txt
```
## Ejecutar las pruebas 
```
 pytest -v --html=reporte.html --self-contained-html
```
## Casos de prueba
1- test_login.py - login exitoso con standar_user
2- test_inventory.py - Verifica 6 productos
3- test:carrito.py - Agrega 1 producto al carrito y verifica badge
