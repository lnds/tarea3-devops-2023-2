const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')

describe('tarea3', function() {
  this.timeout(30000)
  let driver
  let vars
  beforeEach(async function() {
    driver = await new Builder().forBrowser('chrome').build()
    vars = {}
  })
  afterEach(async function() {
    await driver.quit();
  })
  it('tarea3', async function() {
    await driver.get("http://localhost:3000/")
    await driver.manage().window().setRect({ width: 1050, height: 708 })
    await driver.findElement(By.id(":r1:-tab-1")).click()
    await driver.findElement(By.css("#add-director-btn path")).click()
    {
      const element = await driver.findElement(By.css("#add-director-btn path"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    {
      const element = await driver.findElement(By.CSS_SELECTOR, "body")
      await driver.actions({ bridge: true }).moveToElement(element, 0, 0).perform()
    }
    await driver.findElement(By.id("name")).click()
    await driver.findElement(By.id("name")).sendKeys("Steven Spielberg")
    await driver.findElement(By.css(".h-min > .flex")).click()
    await driver.findElement(By.css("#add-director-btn .w-16")).click()
    {
      const element = await driver.findElement(By.css("#add-director-btn .w-16"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    {
      const element = await driver.findElement(By.CSS_SELECTOR, "body")
      await driver.actions({ bridge: true }).moveToElement(element, 0, 0).perform()
    }
    await driver.findElement(By.id("name")).click()
    await driver.findElement(By.id("name")).sendKeys("James Cameron")
    await driver.findElement(By.css(".h-min > .flex")).click()
    await driver.findElement(By.id(":r1:-tab-0")).click()
    await driver.findElement(By.css("#add-movie-btn .w-16")).click()
    {
      const element = await driver.findElement(By.css("#add-movie-btn .w-16"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    {
      const element = await driver.findElement(By.CSS_SELECTOR, "body")
      await driver.actions({ bridge: true }).moveToElement(element, 0, 0).perform()
    }
    await driver.findElement(By.id("title")).click()
    await driver.findElement(By.id("title")).sendKeys("La lista de Schindler")
    await driver.findElement(By.id("description")).click()
    await driver.findElement(By.id("description")).sendKeys("cuenta la historia real del empresario alemán Oskar Schindler quien salvó a más de 1000 judíos durante la segunda guerra mundial.")
    await driver.findElement(By.id("year")).click()
    await driver.findElement(By.id("year")).sendKeys("1994")
    await driver.findElement(By.id("director_id")).click()
    {
      const dropdown = await driver.findElement(By.id("director_id"))
      await dropdown.findElement(By.xpath("//option[. = 'Steven Spielberg']")).click()
    }
    await driver.findElement(By.css(".h-min > .flex")).click()
    await driver.findElement(By.css("#add-movie-btn .w-16")).click()
    {
      const element = await driver.findElement(By.css("#add-movie-btn .w-16"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    {
      const element = await driver.findElement(By.CSS_SELECTOR, "body")
      await driver.actions({ bridge: true }).moveToElement(element, 0, 0).perform()
    }
    await driver.findElement(By.id("title")).click()
    await driver.findElement(By.id("title")).sendKeys("Aliens")
    await driver.findElement(By.id("description")).click()
    await driver.findElement(By.id("description")).sendKeys("La saga de Alien es una saga cinematográfica de ciencia ficción y terror que relata la historia de la teniente Ellen Ripley (protagonizada por Sigourney Weaver) y su lucha contra una forma de vida alienígena, conocida simplemente como «el alien» o xenomorfo. \\n")
    await driver.findElement(By.id("year")).click()
    await driver.findElement(By.id("year")).sendKeys("1979")
    await driver.findElement(By.id("director_id")).click()
    {
      const dropdown = await driver.findElement(By.id("director_id"))
      await dropdown.findElement(By.xpath("//option[. = 'James Cameron']")).click()
    }
    await driver.findElement(By.css(".h-min > .flex")).click()
    await driver.findElement(By.css("#add-movie-btn > .flex")).click()
    {
      const element = await driver.findElement(By.css("#add-movie-btn > .flex"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    {
      const element = await driver.findElement(By.CSS_SELECTOR, "body")
      await driver.actions({ bridge: true }).moveToElement(element, 0, 0).perform()
    }
    await driver.findElement(By.id("title")).click()
    await driver.findElement(By.id("title")).sendKeys("Inception")
    await driver.findElement(By.id("description")).click()
    await driver.findElement(By.id("description")).sendKeys("Dom Cobb (Leonardo DiCaprio) es un ladrón, prófugo de la justicia estadounidense por el supuesto asesinato de su esposa, especializado en infiltrarse en los sueños para robar ideas, claves de bancos, etc. mientras sus víctimas duermen.\\nDirector: Cristopher Nolan")
    await driver.findElement(By.id("year")).click()
    await driver.findElement(By.id("year")).sendKeys("2010")
    await driver.findElement(By.id("director_id")).click()
    {
      const dropdown = await driver.findElement(By.id("director_id"))
      await dropdown.findElement(By.xpath("//option[. = 'Cristopher Nolan']")).click()
    }
    await driver.findElement(By.css(".h-min > .flex")).click()
    await driver.findElement(By.css("#add-movie-btn path")).click()
    {
      const element = await driver.findElement(By.css("#add-movie-btn path"))
      await driver.actions({ bridge: true }).moveToElement(element).perform()
    }
    {
      const element = await driver.findElement(By.CSS_SELECTOR, "body")
      await driver.actions({ bridge: true }).moveToElement(element, 0, 0).perform()
    }
    await driver.findElement(By.id("title")).click()
    await driver.findElement(By.id("title")).sendKeys("Interstellar")
    await driver.findElement(By.id("description")).click()
    await driver.findElement(By.id("description")).sendKeys("Interstellar (conocida como Interestelar en Hispanoamérica) es una película épica de drama y ciencia ficción británico-estadounidense y canadiense de 2014, dirigida por Christopher Nolan y protagonizada por Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine y Matt Damon. Ambientada en un futuro distópico donde la humanidad está luchando por sobrevivir, ya que la Tierra se está volviendo inhabitable por el polvo que está arrasando con todo, cuenta la historia de un grupo de astronautas que viajan a través de un agujero de gusano cerca de Saturno en busca de un nuevo hogar para la humanidad.")
    await driver.findElement(By.id("year")).click()
    await driver.findElement(By.id("year")).sendKeys("2014")
    await driver.findElement(By.id("director_id")).click()
    {
      const dropdown = await driver.findElement(By.id("director_id"))
      await dropdown.findElement(By.xpath("//option[. = 'Cristopher Nolan']")).click()
    }
    await driver.findElement(By.css(".h-min > .flex")).click()
  })
})
