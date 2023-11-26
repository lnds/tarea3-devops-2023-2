# Generated by Selenium IDE
import pytest
import time
import json
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestGATarea3DevOps():

  #Se especifica el driver de selenium IDE en Firefox
  def __init__(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_gATarea3DevOps(self):
  
    #Acceso a la página web (en este caso localhost)
    self.driver.get("http://localhost:3000/")
    self.driver.set_window_size(1936, 1048)
    print("Iniciando proceso de test")
    
    
    #Nos cambiamos a pestaña de directores
    self.driver.find_element(By.ID, ":r1:-tab-1").click()
    print("En directores")

    #Agregando director 1
    print("Agregando Director 1")
    #Hacemos click en agregar director
    self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Gerardo Alonso")
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    print("Agregado Director 1")
    
    #Agregando director 2
    print("Agregando Director 2")
    #Hacemos click en agregar director
    self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Rob Minkoff")
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    print("Agregado Director 2")
   
    #Nos cambiamos a pestaña de peliculas
    self.driver.find_element(By.ID, ":r1:-tab-0").click()
    print("En peliculas")
    
    #Agregando pelicula 1
    print("Agregando Pelicula 1")
    #Hacemos click en agregar pelicula
    self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("Devops en extasis")
    self.driver.find_element(By.ID, "description").send_keys("Un aprendizaje lento pero productivo sobre DevOps y su máximo villano enseñandolo")
    self.driver.find_element(By.ID, "year").click()
    self.driver.find_element(By.ID, "year").send_keys("2023")
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.ID, "director_id").click()
    dropdown = self.driver.find_element(By.ID, "director_id")
    dropdown.find_element(By.XPATH, "//option[. = 'Gerardo Alonso']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    print("Agregada Pelicula 1")
    
    
    #Agregando pelicula 2
    print("Agregando Pelicula 2")
    #Hacemos click en agregar pelicula
    self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("Lion King")
    self.driver.find_element(By.ID, "description").send_keys("A lion cub is betrayed by his uncle and try to find a new life away from its kingdom until unexpected things will made him return")
    self.driver.find_element(By.ID, "year").click()
    self.driver.find_element(By.ID, "year").send_keys("1994")
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.ID, "director_id").click()
    dropdown = self.driver.find_element(By.ID, "director_id")
    dropdown.find_element(By.XPATH, "//option[. = 'Rob Minkoff']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    print("Agregada Pelicula 2")
    
    #Agregando pelicula de Nolan 1
    print("Agregando Pelicula de Nolan 1")
    #Hacemos click en agregar pelicula
    self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("El origen")
    self.driver.find_element(By.ID, "description").send_keys("Una excelente pelicula, solo disfrutala")
    self.driver.find_element(By.ID, "year").click()
    self.driver.find_element(By.ID, "year").send_keys("2010")
    self.driver.find_element(By.ID, "director_id").click()
    dropdown = self.driver.find_element(By.ID, "director_id")
    dropdown.find_element(By.XPATH, "//option[. = 'Cristopher Nolan']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    print("Agregada Pelicula de Nolan 1")
    
    #Agregando pelicula de Nolan 2
    print("Agregando Pelicula de Nolan 2")
    #Hacemos click en agregar pelicula
    self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("Batman el caballero de la noche")
    self.driver.find_element(By.ID, "description").send_keys("Si quieres ver la maestria de un actor como joker, no lo dudes, esta es tu pelicula")
    self.driver.find_element(By.ID, "description").send_keys("Una excelente pelicula, solo disfrutala")
    self.driver.find_element(By.ID, "year").click()
    self.driver.find_element(By.ID, "year").send_keys("2012")
    self.driver.find_element(By.ID, "director_id").click()
    dropdown = self.driver.find_element(By.ID, "director_id")
    dropdown.find_element(By.XPATH, "//option[. = 'Cristopher Nolan']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    print("Agregada Pelicula de Nolan 2")
    
    print("Finalizando proceso de test")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()

    print("Prueba finalizada")
