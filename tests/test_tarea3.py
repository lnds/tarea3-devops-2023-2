import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import time


class TestAppDynamicsJob:
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.url_base = "http://localhost:3000/"
        self.verification_errors = []
        self.accept_next_alert = True
    # Creamos funcion para hacer click, clear y sendkey a un elemento
    def perform_click_clear_sendkeys(self, locator, identifier, value):
        element = self.driver.find_element(locator, identifier)
        element.click()
        element.clear()
        element.send_keys(value)
    # Definimos como variables algunos xpath usados en el codigo
    BUTTON_ADD_DIRECTOR = "//div[@id=':r8:']/div/div[3]/button/span"
    BUTTON_ADD_MOVIE = "//div[@id=':r4:']/div/div[3]/button/span"

    def test_app_dynamics_job(self, setup):
        driver = self.driver
        driver.get(self.url_base)
        driver.implicitly_wait(10)
        # Hacemos click en la pestaña Directors
        driver.find_element(By.ID, ":r1:-tab-1").click()
        # Agregamos el primer director
        driver.find_element(By.ID, "add-director-btn").click()
        self.perform_click_clear_sendkeys(By.ID, "name", "Quentin Tarantino")
        driver.find_element(By.XPATH, self.BUTTON_ADD_DIRECTOR).click()
        # Agregamos el segundo director
        driver.find_element(By.ID, "add-director-btn").click()
        self.perform_click_clear_sendkeys(By.ID, "name", "Martin Scorsese")
        driver.find_element(By.XPATH, self.BUTTON_ADD_DIRECTOR).click()
        # Hacemos click en la pestaña Movies
        driver.find_element(By.ID, ":r1:-tab-0").click()
        # Agregamos la primera pelicula
        driver.find_element(By.ID, "add-movie-btn").click()
        self.perform_click_clear_sendkeys(By.ID, "title", "Malditos bastardos")
        self.perform_click_clear_sendkeys(By.ID, "description", "Soldados judíos y aliados planean venganza brutal contra nazis durante la Segunda Guerra Mundial.")
        self.perform_click_clear_sendkeys(By.ID, "year", "2009")
        driver.find_element(By.ID, "director_id").click()
        Select(driver.find_element(By.ID, "director_id")).select_by_visible_text("Quentin Tarantino")
        driver.find_element(By.XPATH, self.BUTTON_ADD_MOVIE).click()
        # Hacemos click en la pestaña Movies
        driver.find_element(By.ID, ":r1:-tab-0").click()
        # Agregamos la segunda pelicula
        driver.find_element(By.ID, "add-movie-btn").click()
        self.perform_click_clear_sendkeys(By.ID, "title", "El lobo de Wall Street")
        self.perform_click_clear_sendkeys(By.ID, "description", "Viaje vertiginoso de excesos financieros, ambición desbordante y caída inevitable.")
        self.perform_click_clear_sendkeys(By.ID, "year", "2013")
        driver.find_element(By.ID, "director_id").click()
        Select(driver.find_element(By.ID, "director_id")).select_by_visible_text("Martin Scorsese")
        driver.find_element(By.XPATH, self.BUTTON_ADD_MOVIE).click()
        # Hacemos click en la pestaña Movies
        driver.find_element(By.ID, ":r1:-tab-0").click()
        # Agregamos la tercera pelicula
        driver.find_element(By.ID, "add-movie-btn").click()
        self.perform_click_clear_sendkeys(By.ID, "title", "The Prestige")
        self.perform_click_clear_sendkeys(By.ID, "description", "Rivalidad feroz entre ilusionistas lleva a engaños mortales en el mundo del prestigio mágico.")
        self.perform_click_clear_sendkeys(By.ID, "year", "2006")
        driver.find_element(By.ID, "director_id").click()
        Select(driver.find_element(By.ID, "director_id")).select_by_visible_text("Cristopher Nolan")
        driver.find_element(By.XPATH, self.BUTTON_ADD_MOVIE).click()
        # Hacemos click en la pestaña Movies
        driver.find_element(By.ID, ":r1:-tab-0").click()
        # Agregamos la cuarta pelicula
        driver.find_element(By.ID, "add-movie-btn").click()
        self.perform_click_clear_sendkeys(By.ID, "title", "Memento")
        self.perform_click_clear_sendkeys(By.ID, "description", "Leonard busca venganza en un thriller psicológico donde la memoria es su laberinto traicionero.")
        self.perform_click_clear_sendkeys(By.ID, "year", "2000")
        driver.find_element(By.ID, "director_id").click()
        Select(driver.find_element(By.ID, "director_id")).select_by_visible_text("Cristopher Nolan")
        driver.find_element(By.XPATH, self.BUTTON_ADD_MOVIE).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def teardown_method(self):
        assert self.verification_errors == []
        self.driver.quit()
