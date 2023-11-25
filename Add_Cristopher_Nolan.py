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

    driver.find_element(By.ID, "title").send_keys("Following")
    driver.find_element(By.ID, "description").send_keys("Following es el primer largometraje del cineasta Christopher Nolan rodado íntegramente en blanco y negro. Esta película con la que Nolan debutó tuvo tan sólo un presupuesto de 6.000 dólares y fue rodada en 16 milímetros. De 69 minutos de duración.")
    driver.find_element(By.ID, "year").send_keys("1998")
    director_dropdown = driver.find_element(By.ID, "director_id")
    Select(director_dropdown).select_by_visible_text("Cristopher Nolan")

    add_movie_button = driver.find_element(By.CSS_SELECTOR, ".h-min > .flex")
    ActionChains(driver).move_to_element(add_movie_button).click().perform()
    ActionChains(driver).move_to_element(add_movie_button).release().perform()


    add_movie_button = driver.find_element(By.CSS_SELECTOR, "#add-movie-btn > .flex")

    ActionChains(driver).move_to_element(add_movie_button).click().perform()
    ActionChains(driver).move_to_element(add_movie_button).release().perform()

    driver.find_element(By.ID, "title").send_keys("The Prestige")
    driver.find_element(By.ID, "description").send_keys("The Prestige, titulada El truco final (el prestigio) en España y El gran truco en Hispanoamérica, es una película de 2006 dirigida por Christopher Nolan y protagonizada por Christian Bale y Hugh Jackman, basada en el libro homónimo de Christopher Priest. Producida por la Warner Bros. Pictures, se estrenó en 2006 y estuvo nominada a dos Óscar de la Academia de ese año (fotografía y dirección artística). La historia sigue a Robert Angier y Alfred Borden, magos teatrales rivales en Londres a finales del siglo xix. Obsesionados con la creación de la mejor ilusión, se involucran en la competencia de superioridad con resultados trágicos.")
    driver.find_element(By.ID, "year").send_keys("2006")
    director_dropdown = driver.find_element(By.ID, "director_id")
    Select(director_dropdown).select_by_visible_text("Cristopher Nolan")

    add_movie_button = driver.find_element(By.CSS_SELECTOR, ".h-min > .flex")
    ActionChains(driver).move_to_element(add_movie_button).click().perform()
    ActionChains(driver).move_to_element(add_movie_button).release().perform()


except Exception as e:
    print(f"Error: {str(e)}")

finally:
    driver.quit()
