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
    element = driver.find_element(By.ID, ":r1:-tab-1").click()
    boton = driver.find_element(By.XPATH, '//*[@id="add-director-btn"]/span')
    boton.click()
    input_text = driver.find_element(By.ID, "name").click()
    driver.find_element(By.ID, "name").send_keys(DIRECTOR_1)
    add_director = driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    new_boton = driver.find_element(By.XPATH, '//*[@id="add-director-btn"]/span')
    new_boton.click()
    input_text = driver.find_element(By.ID, "name")
    input_text.send_keys(DIRECTOR_2)
    driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    time.sleep(2)


finally:
    driver.quit()