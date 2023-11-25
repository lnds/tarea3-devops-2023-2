from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://localhost:3000")

try:
    driver.find_element(By.ID, ":r1:-tab-1").click()

    director_button = driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16")
    ActionChains(driver).move_to_element(director_button).click().perform()
    ActionChains(driver).move_to_element(director_button).perform()
    ActionChains(driver).move_to_element(director_button).release().perform()

    driver.find_element(By.ID, "name").click()
    driver.find_element(By.ID, "name").send_keys("Director 1")

    add_director_button = driver.find_element(By.CSS_SELECTOR, ".h-min > .flex")
    ActionChains(driver).move_to_element(add_director_button).click().perform()

    ActionChains(driver).move_to_element(director_button).click().perform()
    ActionChains(driver).move_to_element(director_button).perform()
    ActionChains(driver).move_to_element(director_button).release().perform()

    driver.find_element(By.ID, "name").click()
    driver.find_element(By.ID, "name").send_keys("Director 2")

    add_director_button = driver.find_element(By.CSS_SELECTOR, ".h-min > .flex")
    ActionChains(driver).move_to_element(add_director_button).click().perform()

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    driver.quit()

