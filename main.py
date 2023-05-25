# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# from datetime import date
# import time
#
# driver = webdriver.Chrome('./chromedriver.exe')
#
# try:
#     driver.get("https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona")
#
#     count = 0  # Inicializar el contador de clics
#
#     while count < 200:  # Realizar un máximo de 200 clics
#         try:
#             elements = driver.find_elements(By.CLASS_NAME, "brick-helper-fontSize-body")
#             elements = [el.text for el in elements]
#             print(elements)
#
#             # Esperar hasta que aparezca el botón "Ver 12 más"
#             wait = WebDriverWait(driver, 10)
#             next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#nextPage")))
#
#             next_button.click()
#
#             # Esperar hasta que aparezca el botón para cerrar el modal de cookies
#             close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-first")))
#             close_button.click()
#
#             # Esperar a que se carguen los nuevos elementos antes de recorrerlos
#             wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "brick-helper-fontSize-body")))
#
#             # Actualizar la lista elements con los nuevos elementos
#             elements = driver.find_elements(By.CLASS_NAME, "brick-helper-fontSize-body")
#             elements = [el.text for el in elements]
#
#             time.sleep(15)
#
#             count += 1  # Incrementar el contador de clics
#
#         except:
#             break
#
# finally:
#     time.sleep(10000)
#     driver.close()

# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# from datetime import date
# import time
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
#
# # Navigate to Url
# driver.get("https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona")
#
# while True:
#     # Get all the elements available with tag name 'p'
#     elements = driver.find_elements(By.XPATH, "//div[@class='brick-layout-grid-flex__row row-less-padding']//div[@id='switchMap']")
#
#     for e in elements:
#         print(e.text)
#
#     # Buscar el botón "Ver 12 más" y hacer clic en él
#     try:
#         next_button = driver.find_element(By.CSS_SELECTOR, "a#nextPage")
#         if next_button.is_displayed():
#             next_button.click()
#
#             # Esperar hasta que aparezca el botón para cerrar el modal de cookies
#             wait = WebDriverWait(driver, 30)
#             close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-first")))
#             close_button.click()
#
#             # Esperar a que se carguen los nuevos elementos antes de continuar
#             wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='brick-layout-grid-flex__row row-less-padding']//div[@id='switchMap']")))
#         else:
#             break
#
#     except:
#         break
#
# time.sleep(10000)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import date
# import time
#
# driver = webdriver.Chrome()
#
# # Navigate to Url
# driver.get("https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona")
#
# while True:
#     # Get page source
#     html = driver.page_source
#
#     # Parse HTML with BeautifulSoup
#     soup = BeautifulSoup(html, 'html.parser')
#
#     # Find all the switchMap elements
#     switchmaps = soup.select("div.brick-layout-grid-flex__row.row-less-padding div#switchMap")
#
#     # Print the text of each switchMap element
#     for switchmap in switchmaps:
#         print(switchmap.text)
#
#     # Buscar el botón "Ver 12 más" y hacer clic en él
#     try:
#         next_button = driver.find_element(By.CSS_SELECTOR, "a#nextPage")
#         if next_button.is_displayed():
#             next_button.click()
#
#             # Esperar hasta que aparezca el botón para cerrar el modal de cookies
#             close_button = driver.find_element(By.CSS_SELECTOR, "button.btn-first")
#             close_button.click()
#
#             # Esperar a que se carguen los nuevos elementos antes de continuar
#             time.sleep(15)
#         else:
#             break
#
#     except:
#         break
#
# time.sleep(1000)
# driver.close()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# from datetime import date
# import time
#
#
# driver = webdriver.Chrome()
#
# # Navigate to Url
# driver.get("https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/manlleu/52615440")
#
# # Get all the elements available with tag name 'p'
# title = driver.find_elements(By.XPATH, "//h1[@class='title']")
# features = driver.find_elements(By.XPATH, "//div[@class='features']")
# price = driver.find_elements(By.XPATH, "//div[@class='price__current']")
# main_photo = driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//img")
# image_source = main_photo.get_attribute("src")
# image_sources = [image_source]
# elements = title + features + price + image_sources
#
# url_string = " ".join(image_sources)
# print(url_string, end=" ")
#
# for e in elements:
#     if isinstance(e, webdriver.remote.webelement.WebElement):
#         print(e.text)
#     else:
#         print(e)
#
# time.sleep(1000)
# driver.close()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# from datetime import date
# import time
#
# driver = webdriver.Chrome()
#
# # Navigate to Url
# url_list = ["https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/manlleu/52615440", "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/terrassa/51341143", "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/barcelona/37910931"]
# driver.get("https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/manlleu/52615440")
#
# # Get all the elements available with tag name 'p'
# title = driver.find_elements(By.XPATH, "//h1[@class='title']")
# features = driver.find_elements(By.XPATH, "//div[@class='features']")
# price = driver.find_elements(By.XPATH, "//div[@class='price__current']")
# main_photo = driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//img")
# image_source = main_photo.get_attribute("src")
#
# gallery = driver.find_element(By.CSS_SELECTOR, "div.gallery-grid-right.size-4.ng-star-inserted")
# image_elements = gallery.find_elements(By.CSS_SELECTOR, "div.container_img.ng-star-inserted img")
# image_sources = [element.get_attribute("src") for element in image_elements]
#
# elements = title + features + price + [image_source] + image_sources
#
# for e in elements:
#     if isinstance(e, webdriver.remote.webelement.WebElement):
#         print(e.text)
#     else:
#         print(e)
#
# time.sleep(1000)
# driver.close()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# from datetime import date
# import time
#
# driver = webdriver.Chrome()
#
# # Lista de URLs a extraer
# url_list = ["https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/manlleu/52615440",
#             "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/terrassa/51341143",
#             "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/barcelona/37910931"]
#
# # Lista para almacenar los datos extraídos de todas las páginas
# data = []
#
# # Recorrer cada URL de la lista
# for url in url_list:
#     # Navegar a la URL
#     driver.get(url)
#     time.sleep(10)
#
#     # Obtener los datos de la página
#     title = driver.find_elements(By.XPATH, "//h1[@class='title']")
#     features = driver.find_elements(By.XPATH, "//div[@class='features']")
#     price = driver.find_elements(By.XPATH, "//div[@class='price__current']")
#     main_photo = driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//img")
#     image_source = main_photo.get_attribute("src")
#
#     gallery = driver.find_element(By.CSS_SELECTOR, "div.gallery-grid-right.size-4.ng-star-inserted")
#     image_elements = gallery.find_elements(By.CSS_SELECTOR, "div.container_img.ng-star-inserted img")
#     image_sources = [element.get_attribute("src") for element in image_elements]
#
#     elements = title + features + price + [image_source] + image_sources
#
#     # Almacenar los datos en la lista
#     data.append({
#         "Title": title[0].text,
#         "Features": features[0].text,
#         "Price": price[0].text,
#         "Main Photo": image_source,
#         "Image Sources": image_sources
#     })
#
#     # Imprimir los datos en la consola
#     for e in elements:
#         if isinstance(e, webdriver.remote.webelement.WebElement):
#             print(e.text)
#         else:
#             print(e)
#
# # Cerrar el navegador
#
# driver.close()
#
#
#
# # Crear un DataFrame de pandas a partir de la lista de datos
# df = pd.DataFrame(data)
#
# # Imprimir el DataFrame en la consola
# print(df)



# import mysql.connector
# from mysql.connector import errorcode
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
#
# config = {
#     'user': 'root',
#     'password': '',
#     'host': '127.0.0.1',
#     'database': 'hannan',
#     'port': '3306',
#     'raise_on_warnings': True
# }
#
# cnx = None
#
# try:
#     cnx = mysql.connector.connect(**config)
#     cursor = cnx.cursor()
#
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS `real_estate` (
#       `id` INT NOT NULL AUTO_INCREMENT,
#       `title` VARCHAR(255) NOT NULL,
#       `features` TEXT NOT NULL,
#       `price` VARCHAR(255) NOT NULL,
#       `main_photo` VARCHAR(255) NOT NULL,
#       PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
#     """
#
#     cursor.execute(create_table_query)
#
#     url_list = ["https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/manlleu/52615440",
#                 "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/terrassa/51341143",
#                 "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/barcelona/37910931",
#                 "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/vilanova-i-la-geltru/52717713",

#                 ]
#
#     for url in url_list:
#         driver = webdriver.Chrome()
#         driver.get(url)
#
#         time.sleep(5)
#
#         try:
#             accept_button = driver.find_element(By.XPATH, "//button[@id='accept-cookies']")
#             accept_button.click()
#         except:
#             pass
#
#         title = driver.find_elements(By.XPATH, "//h1[@class='title']")
#         features = driver.find_elements(By.XPATH, "//div[@class='features']")
#         price = driver.find_elements(By.XPATH, "//div[@class='price__current']")
#         main_photo = driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//img")
#         image_source = main_photo.get_attribute("src")
#
#         gallery = driver.find_element(By.CSS_SELECTOR, "div.gallery-grid-right.size-4.ng-star-inserted")
#         image_elements = gallery.find_elements(By.CSS_SELECTOR, "div.container_img.ng-star-inserted img")
#         image_sources = [element.get_attribute("src") for element in image_elements]
#
#         elements = title + features + price + [image_source] + image_sources
#
#         if title and features and price:
#             insert_query = """
#             INSERT INTO real_estate (title, features, price, main_photo)
#             VALUES (%s, %s, %s, %s)
#             """
#             cursor.execute(insert_query, (title[0].text, features[0].text, price[0].text, image_source))
#             cnx.commit()
#
#         for e in elements:
#             if isinstance(e, webdriver.remote.webelement.WebElement):
#                 print(e.text)
#             else:
#                 print(e)
#
#         driver.close()
#
#     cursor.close()
#
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
#
# finally:
#     if cnx is not None:
#         cnx.close()



# ULTIMO CODIGO FUNCIONAL

# import mysql.connector
# from mysql.connector import errorcode
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
#
# config = {
#     'user': 'root',
#     'password': '',
#     'host': '127.0.0.1',
#     'database': 'hannan',
#     'port': '3306',
#     'raise_on_warnings': True
# }
#
# cnx = None
#
# try:
#     cnx = mysql.connector.connect(**config)
#     cursor = cnx.cursor()
#
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS `real_estate` (
#       `id` INT NOT NULL AUTO_INCREMENT,
#       `title` VARCHAR(255) NOT NULL,
#       `features` TEXT NOT NULL,
#       `price` VARCHAR(255) NOT NULL,
#       `main_photo` VARCHAR(255) NOT NULL,
#       `url` VARCHAR(255) NOT NULL UNIQUE,
#       PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
#     """
#
#     cursor.execute(create_table_query)
#
#     url_list = ["https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/manlleu/52615440",
#                 "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/terrassa/51341143",
#                 "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/barcelona/37910931",
#                 "https://www.alisedainmobiliaria.com/comprar-vivienda/barcelona/vilanova-i-la-geltru/52717713"
#                 ]
#
#     for url in url_list:
#         driver = webdriver.Chrome()
#         driver.get(url)
#
#         time.sleep(5)
#
#         try:
#             accept_button = driver.find_element(By.XPATH, "//button[@id='accept-cookies']")
#             accept_button.click()
#         except:
#             pass
#
#         title = driver.find_elements(By.XPATH, "//h1[@class='title']")
#         features = driver.find_elements(By.XPATH, "//div[@class='features']")
#         price = driver.find_elements(By.XPATH, "//div[@class='price__current']")
#         main_photo = driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']//img")
#         image_source = main_photo.get_attribute("src")
#
#         gallery = driver.find_element(By.CSS_SELECTOR, "div.gallery-grid-right.size-4.ng-star-inserted")
#         image_elements = gallery.find_elements(By.CSS_SELECTOR, "div.container_img.ng-star-inserted img")
#         image_sources = [element.get_attribute("src") for element in image_elements]
#
#         elements = title + features + price + [image_source] + image_sources
#
#         if title and features and price:
#             select_query = "SELECT id FROM real_estate WHERE url = %s"
#             cursor.execute(select_query, (url,))
#             result = cursor.fetchone()
#
#             if result:
#                 update_query = """
#                 UPDATE real_estate
#                 SET title = %s, features = %s, price = %s, main_photo = %s
#                 WHERE id = %s
#                 """
#                 cursor.execute(update_query, (title[0].text, features[0].text, price[0].text, image_source, result[0]))
#                 cnx.commit()
#             else:
#                 insert_query = """
#                 INSERT INTO real_estate (title, features, price, main_photo, url)
#                 VALUES (%s, %s, %s, %s, %s)
#                 """
#                 cursor.execute(insert_query, (title[0].text, features[0].text, price[0].text, image_source, url))
#                 cnx.commit()
#
#         for e in elements:
#             if isinstance(e, webdriver.remote.webelement.WebElement):
#                 print(e.text)
#             else:
#                 print(e)
#
#         driver.close()
#
#     cursor.close()
#
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
#
# finally:
#     if cnx is not None:
#         cnx.close()
#
#

# import mysql.connector
# from mysql.connector import errorcode
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
#
#
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# title = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#
# elements = title
#
# for e in elements:
#     print(e.text)
#
# time.sleep(1000)
# driver.close()


# PROGRAMA FUNCIONAL

# import mysql.connector
# from mysql.connector import errorcode
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
#
#
#
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
# prices = []
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)  # Esperar a que se cargue el siguiente lote de propiedades
#         counter += 12  # Añadir 12 propiedades al contador
#     except:
#         break
#
#     # Raspar los títulos y precios de todas las propiedades
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     new_prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#     construccion = driver.find_elements(By.XPATH, "//span[@class='property-card-features__item-value']//b")
#
#     prices += new_prices
#     for i in range(len(titles)):
#       print(f"{titles[i].text} {prices[i].text}")
#     if counter % 50 == 0:
#       print(f"Counter: {counter}")





# import mysql.connector
# from mysql.connector import errorcode
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import openpyxl
# import re
#
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
#
#
#
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
# prices = []
# features = []
# data_dict = {"title": [], "price": [], "construccion": [], "hab": [], "banos": [], "image_source": []}
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(15)  # Esperar a que se cargue el siguiente lote de propiedades
#         counter += 12  # Añadir 12 propiedades al contador
#     except:
#         break
#
#
#     # Raspar los títulos y precios de todas las propiedades
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     new_prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#     main_photo = driver.find_element(By.XPATH, "//img[@class='itembox-img itembox-img__list']")
#     image_source = main_photo.get_attribute("src")
#
#     # añadir los datos al diccionario
#
#     for i in range(len(titles)):
#         construccion = driver.find_elements(By.XPATH, "//span[@class='property-card-features__item-value']//b")
#
#         # Calculate the index for each property's construccion, habitaciones, and banos
#         construccion_index = i * 3
#         habitaciones_index = i * 3 + 1
#         banos_index = i * 3 + 2
#
#         # Obtener el valor de metros cuadrados
#         metros_cuadrados = re.findall(r'\d+', construccion[construccion_index].text)[0]
#
#         # Obtener el número de habitaciones
#         habitaciones = re.findall(r'\d+', construccion[habitaciones_index].text)[0]
#
#         # Obtener el número de baños
#         banos = re.findall(r'\d+', construccion[banos_index].text)[0]
#
#         data_dict["title"].append(titles[i].text)
#         data_dict["price"].append(new_prices[i].text)
#         data_dict["construccion"].append(metros_cuadrados)
#         data_dict["hab"].append(habitaciones)
#         data_dict["banos"].append(banos)
#         data_dict["image_source"].append(image_source)
#
#     if counter % 21 == 0:
#         # crear un DataFrame a partir del diccionario
#         df = pd.DataFrame(data_dict)
#
#         # guardar los datos en un archivo Excel
#         filename = f'aliseda_propiedades_{counter}.xlsx'
#         df.to_excel(filename, index=False)
#
#         # imprimir un mensaje indicando que se ha guardado el archivo
#         print(f"Guardando {filename}...")
#
#         # resetear el diccionario
#         data_dict = {"title": [], "price": [], "construccion": [], "hab": [], "banos": [], "image_source": []}
#
#     print(f"{counter} propiedades raspadas")  # imprimir el número de propiedades raspadas
#
#
# df = pd.DataFrame(data_dict)  # crear el DataFrame final
# print(df)  # imprimir el DataFrame completo al final del proceso






# import mysql.connector
# from mysql.connector import errorcode
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import openpyxl
# import re
# import csv
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
# prices = []
# features = []
# data_dict = {"title": [], "price": [], "detalles": [], "image_source": []}
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(15)  # Esperar a que se cargue el siguiente lote de propiedades
#         counter += 12  # Añadir 12 propiedades al contador
#     except:
#         break
#
#
#     # Raspar los títulos y precios de todas las propiedades
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     new_prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#
#
#     # añadir los datos al diccionario
#
#     for i in range(len(titles)):
#         main_photo = driver.find_elements(By.XPATH, "//img[@class='itembox-img itembox-img__list']")[i]
#         image_source = main_photo.get_attribute("src")
#         construccion = driver.find_elements(By.XPATH, "//span[@class='property-card-features__item-value']//b")
#
#         # Crear un diccionario vacío para almacenar los detalles
#         detalles_dict = {"m2": "N/A", "hab": "N/A", "baños": "N/A"}
#
#         for j in range(i * 3, i * 3 + 3):
#             if j < len(construccion):
#                 number = re.findall(r'\d+', construccion[j].text)
#                 if number:
#                     # Asignar los valores según el índice
#                     if j % 3 == 0:
#                         detalles_dict["m2"] = number[0]
#                     elif j % 3 == 1:
#                         detalles_dict["hab"] = number[0]
#                     elif j % 3 == 2:
#                         detalles_dict["baños"] = number[0]
#
#         # Concatenar los valores de metros cuadrados, habitaciones y baños en una sola cadena
#         detalles = f"{detalles_dict['m2']} m², {detalles_dict['hab']} hab, {detalles_dict['baños']} baños"
#
#         data_dict["title"].append(titles[i].text)
#         data_dict["price"].append(new_prices[i].text)
#         data_dict["detalles"].append(detalles)
#         data_dict["image_source"].append(image_source)
#
#     # ... (mismo código posterior al bucle for)
#
#     if counter % 21 == 0:
#         # crear un DataFrame a partir del diccionario
#         df = pd.DataFrame(data_dict)
#
#         # guardar los datos en un archivo Excel
#         filename = f'aliseda_propiedades_{counter}.xlsx'
#         df.to_csv(filename, index=False)
#
#         # imprimir un mensaje indicando que se ha guardado el archivo
#         print(f"Guardando {filename}...")
#
#         # resetear el diccionario
#         data_dict = {"title": [], "price": [], "detalles": [], "image_source": []}
#
#     print(f"{counter} propiedades raspadas")  # imprimir el número de propiedades raspadas
#
#
# df = pd.DataFrame(data_dict)  # crear el DataFrame final
# print(df)  # imprimir el DataFrame completo al final del proceso












# import mysql.connector
# from mysql.connector import errorcode
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import openpyxl
# import re
# import csv
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
#
# prop_dict = {}
# def divide_features(features, n):
#     for i in range(0, len(features), n):
#         yield features[i:i + n]
#
#
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         break
#
#     # Encuentra los elementos del título y del precio
#
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#
#     # Encuentra todos los elementos <ul> que contengan las características
#     ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")
#
#     # Itera a través de los elementos <ul> y encuentra los elementos <li> dentro de ellos
#     grouped_features = []
#     for ul in ul_elements:
#         li_elements = ul.find_elements(By.XPATH, ".//li")
#         features = []
#         for li in li_elements:
#             b_element = li.find_element(By.XPATH, ".//b")
#             number = b_element.text
#             features.append(number)
#         grouped_features.append(features)
#
#     # Crea el diccionario para guardar los datos
#     prop_dict = {}
#
#     # Itera a través de los títulos, precios y características y guárdalos en el diccionario
#     for i in range(len(titles)):
#         prop_dict[titles[i].text] = {
#             "price": prices[i].text,
#             "features": grouped_features[i],
#         }
#
#     # Imprime los datos en orden desde el diccionario
#     for title, data in prop_dict.items():
#         print(title)
#         print(data["price"])
#         for feature in data["features"]:
#             print(feature)
#




# ULTIMO CODIGO FUNCIONAL

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el web driver
driver = webdriver.Chrome()
driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")

# Aceptar las cookies
cookies_accept_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
)
cookies_accept_btn.click()

# Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
counter = 0

while True:
    try:
        ver_mas_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nextPage"))
        )
        ver_mas_btn.click()
        time.sleep(18)
        counter += 12
    except:
        break

    # Encuentra los elementos del título y del precio
    titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
    prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")

    # Encuentra todos los elementos <ul> que contengan las características
    ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")

    # Itera a través de los elementos <ul> y encuentra los elementos <li> dentro de ellos
    grouped_features = []
    for ul in ul_elements:
        li_elements = ul.find_elements(By.XPATH, ".//li")
        features = []
        for li in li_elements:
            b_element = li.find_element(By.XPATH, ".//b")
            number = b_element.text
            features.append(number)
        grouped_features.append(features)

    # Crea una lista para almacenar los datos de las propiedades
    properties_data = []

    img_elements = driver.find_elements(By.CSS_SELECTOR,"img.itembox-img.itembox-img__list")

    # Itera a través de los títulos, precios y características y guárdalos en la lista
    for i in range(len(titles)):
        img_url = None
        for img in img_elements:
            if img.get_attribute("alt") == titles[i].text:
                img_url = img.get_attribute("src")
                break

        property_data = {
            "title": titles[i].text,
            "price": prices[i].text,
            "square_meters": grouped_features[i][0] if len(grouped_features[i]) > 0 else None,
            "bedrooms": grouped_features[i][1] if len(grouped_features[i]) > 1 else None,
            "bathrooms": grouped_features[i][2] if len(grouped_features[i]) > 2 else None,
            "img_urls": img_url
        }
        properties_data.append(property_data)

    # Crea un DataFrame con la lista de propiedades
    df = pd.DataFrame(properties_data)

    # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
    if counter % 24 == 0:
        file_counter = counter // 24
        df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")

# Cierra el driver de Selenium
driver.quit()





#PENULTIMO CODIGO FUNCIONAL

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
#
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         break
#
#     # Encuentra los elementos del título y del precio
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#
#     # Encuentra todos los elementos <ul> que contengan las características
#     ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")
#
#     img_elements = driver.find_elements(By.CSS_SELECTOR, "img.itembox-img.itembox-img__list")
#
#     # Itera a través de los elementos <ul> y encuentra los elementos <li> dentro de ellos
#     grouped_features = []
#     for ul in ul_elements:
#         li_elements = ul.find_elements(By.XPATH, ".//li")
#         features = []
#         for li in li_elements:
#             b_element = li.find_element(By.XPATH, ".//b")
#             number = b_element.text
#             features.append(number)
#         img_url = img_elements[len(grouped_features)].get_attribute("src")
#         features.append(img_url)
#         grouped_features.append(features)
#
#     # Crea una lista para almacenar los datos de las propiedades
#     properties_data = []
#
#     # Itera a través de los títulos, precios y características y guárdalos en la lista
#     for i in range(len(titles)):
#         property_data = {
#             "title": titles[i].text,
#             "price": prices[i].text,
#             "square_meters": grouped_features[i][0] if len(grouped_features[i]) > 0 else None,
#             "bedrooms": grouped_features[i][1] if len(grouped_features[i]) > 1 else None,
#             "bathrooms": grouped_features[i][2] if len(grouped_features[i]) > 2 else None,
#             "img_url": grouped_features[i][3] if len(grouped_features[i]) > 3 else None
#         }
#         properties_data.append(property_data)
#
#     # Crea un DataFrame con la lista de propiedades
#     df = pd.DataFrame(properties_data, columns=["title", "price", "square_meters", "bedrooms", "bathrooms", "img_url"])
#
#     # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
#     if counter % 24 == 0:
#         file_counter = counter // 24
#         df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Cierra el driver de Selenium
# driver.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
#
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         break
#
#     # Encuentra los elementos del título y del precio
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#
#     # Encuentra todos los elementos <ul> que contengan las características
#     ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")
#
#     # Encuentra todos los elementos de imagen
#     img_elements = driver.find_elements(By.CSS_SELECTOR, "img.itembox-img.itembox-img__list")
#
#     # Almacenar las URL de las imágenes en una lista separada para cada propiedad
#     img_urls = []
#     grouped_features = []
#
#     for i in range(len(titles)):
#         # Encuentra el número de imágenes para la propiedad actual
#         num_imgs = len(driver.find_elements(By.XPATH,
#                                             f"(//img[@class='itembox-img itembox-img__list'])[{i + 1}]/ancestor::div[@class='itembox']/preceding-sibling::div[1]//img"))
#
#         # Agrega las URL de imagen a una lista separada para esta propiedad
#         img_urls.append([img.get_attribute("src") for img in img_elements[:num_imgs]])
#
#         # Elimina las URL de imagen que ya hemos agregado
#         img_elements = img_elements[num_imgs:]
#
#     # Crea una lista para almacenar los datos de las propiedades
#     properties_data = []
#
#     # Itera a través de los títulos, precios y características y guárdalos en la lista
#     for i in range(len(titles)):
#         property_data = {
#             "title": titles[i].text,
#             "price": prices[i].text,
#             "square_meters": grouped_features[i][0] if len(grouped_features[i]) > 0 else None,
#             "bedrooms": grouped_features[i][1] if len(grouped_features[i]) > 1 else None,
#             "bathrooms": grouped_features[i][2] if len(grouped_features[i]) > 2 else None,
#             "img_urls": img_urls[i]  # Agrega la lista de URL de imagen correspondiente
#         }
#         properties_data.append(property_data)
#
#     # Crea un DataFrame con la lista de propiedades
#     df = pd.DataFrame(properties_data, columns=["title", "price", "square_meters", "bedrooms", "bathrooms", "img_urls"])
#
#     # Usa la función explode() para crear una fila separada para cada URL de imagen
#     df = df.explode("img_urls")
#
#     # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
#     if counter % 24 == 0:
#         file_counter = counter // 24
#         df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Cierra el driver de Selenium
# driver.quit()





#CODIGO CON UNA SOLA IMAGEN


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_updated*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
#
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         break
#
#     # Encuentra los elementos del título y del precio
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#
#     # Encuentra todos los elementos <ul> que contengan las características
#     ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")
#
#     # Itera a través de los elementos <ul> y encuentra los elementos <li> dentro de ellos
#     grouped_features = []
#     for ul in ul_elements:
#         li_elements = ul.find_elements(By.XPATH, ".//li")
#         features = []
#         for li in li_elements:
#             b_element = li.find_element(By.XPATH, ".//b")
#             number = b_element.text
#             features.append(number)
#         grouped_features.append(features)
#
#     # Crea una lista para almacenar las URL de las imágenes de la primera imagen de cada propiedad
#     img_urls = []
#     property_containers = driver.find_elements(By.XPATH, "//div[@class='property-card__container']")
#
#     # Accede a la primera imagen de cada propiedad
#     for container in property_containers:
#         img_element = container.find_element(By.XPATH, ".//img[@class='itembox-img itembox-img__list']")
#         img_url = img_element.get_attribute("src")
#         img_urls.append(img_url)
#
#     # ... (código posterior)
#
#     # Itera a través de los títulos, precios y características y guárdalos en la lista
#     properties_data = []
#     for i in range(len(titles)):
#         property_data = {
#             "title": titles[i].text,
#             "price": prices[i].text,
#             "square_meters": grouped_features[i][0] if len(grouped_features[i]) > 0 else None,
#             "bedrooms": grouped_features[i][1] if len(grouped_features[i]) > 1 else None,
#             "bathrooms": grouped_features[i][2] if len(grouped_features[i]) > 2 else None,
#             "img_url": img_urls[i]  # Agrega la URL de la imagen de la propiedad actual
#         }
#         properties_data.append(property_data)
#
#     # Crea un DataFrame con la lista de propiedades
#     df = pd.DataFrame(properties_data)
#
#     # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
#     if counter % 24 == 0:
#         file_counter = counter // 24
#         df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Cierra el driver de Selenium
# driver.quit()



#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
#
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         break
#
#     # Encuentra los elementos del título y del precio
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#
#     # Encuentra todos los elementos <ul> que contengan las características
#     ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")
#
#     # Itera a través de los elementos <ul> y encuentra los elementos <li> dentro de ellos
#     grouped_features = []
#     for ul in ul_elements:
#         li_elements = ul.find_elements(By.XPATH, ".//li")
#         features = []
#         for li in li_elements:
#             b_element = li.find_element(By.XPATH, ".//b")
#             number = b_element.text
#             features.append(number)
#         grouped_features.append(features)
#
#     # Crea una lista para almacenar los datos de las propiedades
#     properties_data = []
#
#     # Itera a través de los títulos, precios y características y guárdalos en la lista
#     for i in range(len(titles)):
#         img_element = driver.find_elements(By.CSS_SELECTOR,"img.itembox-img.itembox-img__list")[i]
#         img_url = img_element.get_attribute("src")
#
#         property_data = {
#             "title": titles[i].text,
#             "price": prices[i].text,
#             "square_meters": grouped_features[i][0] if len(grouped_features[i]) > 0 else None,
#             "bedrooms": grouped_features[i][1] if len(grouped_features[i]) > 1 else None,
#             "bathrooms": grouped_features[i][2] if len(grouped_features[i]) > 2 else None,
#             "img_url": img_url
#         }
#         properties_data.append(property_data)
#
#     # Crea un DataFrame con la lista de propiedades
#     df = pd.DataFrame(properties_data)
#
#     # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
#     if counter % 24 == 0:
#         file_counter = counter // 24
#
#
#         df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Cierra el driver de Selenium
# driver.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
#
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         break
#
#     # Encuentra los elementos del título y del precio
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#
#     # Encuentra todos los elementos <ul> que contengan las características
#     ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")
#
#     # Itera a través de los elementos <ul> y encuentra los elementos <li> dentro de ellos
#     grouped_features = []
#     for ul in ul_elements:
#         li_elements = ul.find_elements(By.XPATH, ".//li")
#         features = []
#         for li in li_elements:
#             b_element = li.find_element(By.XPATH, ".//b")
#             number = b_element.text
#             features.append(number)
#         grouped_features.append(features)
#
#     # Crea una lista para almacenar los datos de las propiedades
#     properties_data = []
#
#     # Encuentra las URL de las imágenes
#     img_elements = driver.find_elements(By.XPATH, '//img[@class= "itembox-img itembox-img__list"]')
#
#
#     # Itera a través de los títulos, precios y características y guárdalos en la lista
#     for i in range(len(titles)):
#         img_src = img_elements[i].get_attribute("src")
#         print(img_src)
#         # Encuentra los detalles de la propiedad actual
#         property_data = {
#             "title": titles[i].text,
#             "price": prices[i].text,
#             "square_meters": grouped_features[i][0] if len(grouped_features[i]) > 0 else None,
#             "bedrooms": grouped_features[i][1] if len(grouped_features[i]) > 1 else None,
#             "bathrooms": grouped_features[i][2] if len(grouped_features[i]) > 2 else None,
#             "img_url": img_src
#         }
#         properties_data.append(property_data)
#
#         # Crea un DataFrame con la lista de propiedades
#     df = pd.DataFrame(properties_data)
#
#     # Guarda el DataFrame en un archivo de Excel cada 24 propiedades
#     if counter % 24 == 0:
#         file_counter = counter // 24
#
#         df.to_excel(f"properties_data_{file_counter}.xlsx", index=False, engine="openpyxl")
#
# # Cierra el driver de Selenium
# driver.quit()



# #GUARDAR EN MONGO DB
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pymongo import MongoClient
# from pymongo.mongo_client import MongoClient
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
#
# # Create a connection to the MongoDB server
# uri = "mongodb+srv://arquidev:<hector20759364>@cluster0.ueqz4.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(uri)
# db = client['properties_db']
# collection = db['properties_data']
#
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
#
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         break
#
#     # Encuentra los elementos del título y del precio
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#
#     # Encuentra todos los elementos <ul> que contengan las características
#     ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")
#
#     # Itera a través de los elementos <ul> y encuentra los elementos <li> dentro de ellos
#     grouped_features = []
#     for ul in ul_elements:
#         li_elements = ul.find_elements(By.XPATH, ".//li")
#         features = []
#         for li in li_elements:
#             b_element = li.find_element(By.XPATH, ".//b")
#             number = b_element.text
#             features.append(number)
#         grouped_features.append(features)
#
#     # Crea una lista para almacenar los datos de las propiedades
#     properties_data = []
#
#     # Encuentra las URL de las imágenes
#     img_elements = driver.find_elements(By.XPATH, '//img[@class= "itembox-img itembox-img__list"]')
#
#
#     # Itera a través de los títulos, precios y características y guárdalos en la lista
#     for i in range(len(titles)):
#         img_src = img_elements[i].get_attribute("src")
#         print(img_src)
#         # Encuentra los detalles de la propiedad actual
#         property_data = {
#             "title": titles[i].text,
#             "price": prices[i].text,
#             "square_meters": grouped_features[i][0] if len(grouped_features[i]) > 0 else None,
#             "bedrooms": grouped_features[i][1] if len(grouped_features[i]) > 1 else None,
#             "bathrooms": grouped_features[i][2] if len(grouped_features[i]) > 2 else None,
#             "img_url": img_src
#         }
#         properties_data.append(property_data)
#
#         # Save the extracted data to MongoDB
#         for property_data in properties_data:
#             collection.insert_one(property_data)
#
# # Cierra el driver de Selenium
# driver.quit()
#
#
#


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import firestore
#
# # Configurar el web driver
# driver = webdriver.Chrome()
# driver.get("https://www.alisedainmobiliaria.com/compra-con-un-clic?_gl=1*1yg083r*_up*MQ..*_ga*MzM3Mjc2Nzg0LjE2ODQ0MTgyMTQ.*_ga_4LDRN41J8T*MTY4NDQxODIxMy4xLjEuMTY4NDQxODIxOS4wLjAuMA..")
#
# # Aceptar las cookies
# cookies_accept_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "btn-first"))
# )
# cookies_accept_btn.click()
#
# # Recorrer todos los botones "Ver 12 más" y hacer clic en ellos
# counter = 0
# while True:
#     try:
#         ver_mas_btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "nextPage"))
#         )
#         ver_mas_btn.click()
#         time.sleep(18)
#         counter += 12
#     except:
#         break
#
#     # Inicializar la aplicación Firebase
#
#
#     firebaseConfig = {
#       'apiKey': "AIzaSyBAiuV3N0BnTqHO28JX_VF0lp1WG3iCYXQ",
#       'authDomain': "databaselanding.firebaseapp.com",
#       'projectId': "databaselanding",
#       'storageBucket': "databaselanding.appspot.com",
#       'messagingSenderId': "1047531959700",
#       'appId': "1:1047531959700:web:d1914bc57b5866d6138b81",
#       'measurementId': "G-C5Y75236KE"
#     }
#
#
#     firebase_admin.initialize_app(firebaseConfig, {
#         'projectId': 'databaselanding'
#     })
#
#     # Obtener una referencia a la base de datos Firebase Realtime
#     db = firestore.client()
#
#     # Extraer y guardar los datos de las propiedades en Firebase
#     titles = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-body brick-helper-fontWeight-500']")
#     prices = driver.find_elements(By.XPATH, "//span[@class='brick-helper-fontSize-type brick-helper-fontWeight-700']")
#     ul_elements = driver.find_elements(By.XPATH, "//ul[@class='property-card-features no-attribute ng-star-inserted']")
#     img_elements = driver.find_elements(By.XPATH, '//img[@class= "itembox-img itembox-img__list"]')
#
#     grouped_features = []
#     for ul in ul_elements:
#         li_elements = ul.find_elements(By.XPATH, ".//li")
#         features = []
#         for li in li_elements:
#             b_element = li.find_element(By.XPATH, ".//b")
#             number = b_element.text
#             features.append(number)
#         grouped_features.append(features)
#
#     properties_data = []
#     count = 0
#     for i in range(len(titles)):
#         img_src = img_elements[i].get_attribute("src")
#         property_data = {
#             "title": titles[i].text,
#             "price": prices[i].text,
#             "square_meters": grouped_features[i][0] if len(grouped_features[i]) > 0 else None,
#             "bedrooms": grouped_features[i][1] if len(grouped_features[i]) > 1 else None,
#             "bathrooms": grouped_features[i][2] if len(grouped_features[i]) > 2 else None,
#             "img_url": img_src
#         }
#         properties_data.append(property_data)
#         count += 1
#         # Si se han extraído 24 propiedades, guardarlas en Firebase
#         if count == 24:
#             # Agregar los datos a la colección 'propiedades'
#             db.collection('propiedades').add(property_data)
#             properties_data = []
#             count = 0
#
#     # Guardar las propiedades restantes en Firebase
#     if properties_data:
#         db.collection('propiedades').add(property_data)
# # Cerrar el driver de Selenium
# driver.quit()
