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
        self.driver.find_element(By.ID, "name").send_keys("Martin Scorsese")
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("David Lynch")
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

    def test_caso2(self):
        self.driver.get("http://localhost:3000/")
        self.driver.find_element(By.ID, ":r1:-tab-0").click()

        #Director 1 Cristopher Nolan -> Pelicual 1
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Memento")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de suspenso psicológico protagonizada por Guy Pearce como Leonard Shelby, un hombre que sufre de amnesia anterógrada y está decidido a encontrar al hombre que violó y asesinó a su esposa. La película utiliza un formato de narración no lineal para explorar temas como la memoria, la identidad y la venganza.")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("2000")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        #Director 2 Greta Gerwig -> Pelicual 1
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Lady Bird")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de coming-of-age escrita y dirigida por Greta Gerwig en su debut como directora. La película está protagonizada por Saoirse Ronan como Christine, una joven que lucha por encontrar su lugar en el mundo. La película se desarrolla en Sacramento, California, y explora temas como la familia, la amistad, el amor y la identidad.")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("2017")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        #Director 3 Martin Scorsese -> Pelicual 1
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Taxi Driver")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película dramática neo-noir escrita y dirigida por Martin Scorsese. La película está protagonizada por Robert De Niro como Travis Bickle, un taxista de Nueva York que se siente alienado de la sociedad. La película explora temas como la violencia, la soledad, la paranoia y la locura.")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("1976")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        #Director 4 David Lynch -> Pelicual 1        
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Mulholland Drive")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de suspenso psicológico escrita y dirigida por David Lynch. La película está protagonizada por Naomi Watts como Betty Elms, una aspirante a actriz que llega a Los Ángeles, y Laura Harring como Rita, una mujer amnésica que se encuentra con Betty. La película explora temas como la identidad, la realidad y la memoria.")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("2001")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(5)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

    def test_caso3(self):
        self.driver.get("http://localhost:3000/")
        self.driver.find_element(By.ID, ":r1:-tab-0").click()

        #Director 1 Cristopher Nolan -> Pelicual 1
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("El caballero oscuro")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de superhéroes basada en el personaje de DC Comics Batman. La película está protagonizada por Christian Bale como Bruce Wayne/Batman, Heath Ledger como el Joker y Michael Caine como Alfred Pennyworth. La película es una de las películas de superhéroes más aclamadas por la crítica y comercialmente exitosas de todos los tiempos.")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("2008")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

        #Director 1 Cristopher Nolan -> Pelicual 2
        self.driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/div[2]/div[1]/button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Origen")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Es una película de ciencia ficción protagonizada por Leonardo DiCaprio como Dom Cobb, un ladrón que roba secretos corporativos implantándolos en los sueños de las personas. La película explora temas como la realidad, el sueño y la mente.")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("2010")
        self.driver.find_element(By.ID, "director_id").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
