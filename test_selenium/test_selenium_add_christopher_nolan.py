from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
LOCAL_PATH = 'http://127.0.0.1:3000'
DIRECTOR_1 = "Alejandro Gómez Monteverde"
DIRECTOR_2 = "Wes Craven"
try:
    driver.get(LOCAL_PATH)
    time.sleep(1)
    driver.maximize_window()
    boton = driver.find_element(By.XPATH, '//*[@id="add-movie-btn"]/span')
    boton.click()
    #primera asignacion
    driver.find_element(By.ID, "title").click()
    driver.find_element(By.ID, "title").send_keys("Shrek 3")
    driver.find_element(By.ID, "description").send_keys("Pelicula de monos")
    driver.find_element(By.ID, "year").click()
    driver.find_element(By.ID, "year").send_keys("2006")
    driver.find_element(By.ID, "director_id").click()
    director_list = driver.find_element(By.ID, "director_id")
    director_list.find_element(By.XPATH, "//option[. = 'Cristopher Nolan']").click()
    driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    time.sleep(1)
    #segunda asignacion
    boton = driver.find_element(By.XPATH, '//*[@id="add-movie-btn"]/span')
    boton.click()
    driver.find_element(By.ID, "title").click()
    driver.find_element(By.ID, "title").send_keys("Shrek 4")
    driver.find_element(By.ID, "description").send_keys("Pelicula de monos")
    driver.find_element(By.ID, "year").click()
    driver.find_element(By.ID, "year").send_keys("2006")
    driver.find_element(By.ID, "director_id").click()
    director_list = driver.find_element(By.ID, "director_id")
    director_list.find_element(By.XPATH, "//option[. = 'Cristopher Nolan']").click()
    driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    time.sleep(2)


finally:
    driver.quit()