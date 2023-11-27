import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestAgrega2Peliculas():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_agrega2Peliculas(self):
        self.driver.get("http://localhost:3000/")
        self.driver.set_window_size(1050, 708)

        # Agregar la primera película (Inception)
        self.agregar_pelicula("Inception", "Pelicula de suspenso", "2010", "Cristopher Nolan")

        # Agregar la segunda película (The Dark Knight)
        self.agregar_pelicula("The Dark Knight", "Película de acción", "2008", "Cristopher Nolan")

    def agregar_pelicula(self, title, description, year, director):
        # Hacer clic en el botón para agregar película
        self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()

        # Ingresar detalles de la película
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys(title)
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys(description)
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys(year)
        self.driver.find_element(By.ID, "director_id").click()

        # Seleccionar director desde el dropdown
        dropdown = self.driver.find_element(By.ID, "director_id")
        dropdown.find_element(By.XPATH, f"//option[. = '{director}']").click()

        # Confirmar la adición de la película
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

if __name__ == "__main__":
    pytest.main()
