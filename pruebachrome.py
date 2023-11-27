from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Crear una sesión de Firefox
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Acceder a la aplicación web
driver.get("http://www.google.es")

# Localizar cuadro de texto
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# Indicar y confirmar término de búsqueda
search_field.send_keys("Término de búsqueda")
search_field.submit()

# Obtener la lista de resultados de la búsqueda y mostrarla
# mediante el método find_elements_by_class_name
lists= driver.find_elements_by_class_name("_Rm")

# Pasar por todos los elementos y reproducir el texto individual

i=0
for listitem in lists:
  print (listitem.get_attribute("innerHTML"))
  i=i+1
  if(i>10):
    break

# Cerrar la ventana del navegador
driver.quit()
