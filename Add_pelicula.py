from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://localhost:3000")

try:
    driver.find_element(By.ID, ":r1:-tab-0").click()

    add_movie_button = driver.find_element(By.CSS_SELECTOR, "#add-movie-btn > .flex")

    ActionChains(driver).move_to_element(add_movie_button).click().perform()
    ActionChains(driver).move_to_element(add_movie_button).release().perform()

    driver.find_element(By.ID, "title").send_keys("Pelicula 1")
    driver.find_element(By.ID, "description").send_keys("Descripcion 1")
    driver.find_element(By.ID, "year").send_keys("2001")
    director_dropdown = driver.find_element(By.ID, "director_id")
    Select(director_dropdown).select_by_visible_text("Director 1")

    add_movie_button = driver.find_element(By.CSS_SELECTOR, ".h-min > .flex")
    ActionChains(driver).move_to_element(add_movie_button).click().perform()
    ActionChains(driver).move_to_element(add_movie_button).release().perform()


    add_movie_button = driver.find_element(By.CSS_SELECTOR, "#add-movie-btn > .flex")

    ActionChains(driver).move_to_element(add_movie_button).click().perform()
    ActionChains(driver).move_to_element(add_movie_button).release().perform()

    driver.find_element(By.ID, "title").send_keys("Pelicula 2")
    driver.find_element(By.ID, "description").send_keys("Descripcion 2")
    driver.find_element(By.ID, "year").send_keys("2002")
    director_dropdown = driver.find_element(By.ID, "director_id")
    Select(director_dropdown).select_by_visible_text("Director 2")

    add_movie_button = driver.find_element(By.CSS_SELECTOR, ".h-min > .flex")
    ActionChains(driver).move_to_element(add_movie_button).click().perform()
    ActionChains(driver).move_to_element(add_movie_button).release().perform()


except Exception as e:
    print(f"Error: {str(e)}")

finally:
    driver.quit()
