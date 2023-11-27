import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_caso1(self):
        self.driver.get("http://localhost:3000/")
        self.driver.find_element(By.ID, ":r1:-tab-1").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("George Lucas")
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("Steven Spielberg")
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()



    def test_caso2(self):
        self.driver.get("http://localhost:3000/")
        self.driver.find_element(By.ID, ":r1:-tab-0").click()

        #Director 1 George Lucas -> Pelicula 1
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Star Wars")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de ciencia ficción, en la cual se vive una guerra de distintos mundos, incluye mitología y temas musicales.")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("1983")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        #Director 2 Steven Spielberg -> Pelicula 1
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("E.T")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de ciencia ficción, en la cual llega un extraterrestre a la Tierra")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("1982")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()


    def test_caso3(self):
        self.driver.get("http://localhost:3000/")
        self.driver.find_element(By.ID, ":r1:-tab-1").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("Christopher Nolan")
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        #Director 1 Cristopher Nolan -> Pelicula 1
        self.driver.find_element(By.ID, ":r1:-tab-0").click()
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Dunkerque")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de hechos reales, basada en la segunda Guerra Mundial")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("2017")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        #Director 1 Christopher Nolan -> Pelicula 2
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Interestelar")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de ciencia ficción, en la cual el protagonista viaja por distintops futuros.")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("2014")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()