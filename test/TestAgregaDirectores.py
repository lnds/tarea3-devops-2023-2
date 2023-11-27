import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAgregaDirectores():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_agregaDirectores(self):
        self.driver.get("http://localhost:3000/")
        self.driver.set_window_size(1050, 708)

        # Click en el primer tab
        self.driver.find_element(By.ID, ":r1:-tab-1").click()

        # Click en el botón para agregar director
        self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn path").click()

        # Ingresar el nombre "Lana y Lili Wachowski"
        name_input = self.driver.find_element(By.ID, "name")
        name_input.click()
        name_input.send_keys("Lana y Lili Wachowski")

        # Confirmar la adición del director
        self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()

        # Repetir el proceso para el segundo director
        name_input = self.driver.find_element(By.ID, "name")
        name_input.click()
        name_input.send_keys("Andrew Adamson y Vicky Jenson")

        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

if __name__ == "__main__":
    pytest.main()
