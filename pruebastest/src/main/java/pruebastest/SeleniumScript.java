package pruebastest;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;

public class SeleniumScript {
    public static void main(String[] args) {
        // Configura la propiedad del sistema para el controlador de Chrome
       System.setProperty("webdriver.gecko.driver", "ruta/al/geckodriver.exe");

        // Inicializa el WebDriver
        WebDriver driver = new FirefoxDriver();

        driver.get("http://localhost:3000/");
        // 2 | setWindowSize | 1936x1096 | 
        driver.manage().window().setSize(new Dimension(1936, 1096));
        // 3 | click | id=:r1:-tab-1 | 
        driver.findElement(By.id(":r1:-tab-1")).click();
        // 4 | click | css=#add-director-btn path | 
        driver.findElement(By.cssSelector("#add-director-btn")).click();
        // 5 | click | id=name | 
        driver.findElement(By.id("name")).click();
        // 6 | type | id=name |  James Cameron
        driver.findElement(By.id("name")).sendKeys(" James Cameron");
        // 7 | click | css=.h-min > .flex | 
        driver.findElement(By.cssSelector(".h-min > .flex")).click();
        // 8 | click | css=#add-director-btn .w-16 | 
        driver.findElement(By.cssSelector("#add-director-btn .w-16")).click();
        // 9 | mouseOver | css=#add-director-btn .w-16 | 
        {
          WebElement element = driver.findElement(By.cssSelector("#add-director-btn .w-16"));
          Actions builder = new Actions(driver);
          builder.moveToElement(element).perform();
        }
        // 10 | mouseOut | css=#add-director-btn .w-16 | 
        {
          WebElement element = driver.findElement(By.tagName("body"));
          Actions builder = new Actions(driver);
          builder.moveToElement(element, 0, 0).perform();
        }
        // 11 | click | id=name | 
        driver.findElement(By.id("name")).click();
        // 12 | type | id=name | Steven Spielberg
        driver.findElement(By.id("name")).sendKeys("Steven Spielberg");
        // 13 | click | css=.h-min > .flex | 
        driver.findElement(By.cssSelector(".h-min > .flex")).click();
        
        //test nuevas peliculas a nuevos directores***************************
        
        driver.findElement(By.id(":r1:-tab-0")).click();
        
        driver.findElement(By.cssSelector("#add-movie-btn")).click();
        // 4 | mouseOver | css=#add-movie-btn path | 
        {
          WebElement element = driver.findElement(By.cssSelector("#add-movie-btn"));
          Actions builder = new Actions(driver);
          builder.moveToElement(element).perform();
        }
        // 5 | mouseOut | css=#add-movie-btn path | 
        {
          WebElement element = driver.findElement(By.tagName("body"));
          Actions builder = new Actions(driver);
          builder.moveToElement(element, 0, 0).perform();
        }
        // 6 | click | id=title | 
        driver.findElement(By.id("title")).click();
        // 7 | type | id=title | Terminator
        driver.findElement(By.id("title")).sendKeys("Terminator");
        // 8 | click | id=description | 
        driver.findElement(By.id("description")).click();
        // 9 | type | id=description | Ciencia Ficción
        driver.findElement(By.id("description")).sendKeys("Ciencia Ficción");
        // 10 | click | id=year | 
        driver.findElement(By.id("year")).click();
        // 11 | type | id=year | 1987
        driver.findElement(By.id("year")).sendKeys("1987");
        // 12 | click | id=director_id | 
        driver.findElement(By.id("director_id")).click();
        // 13 | select | id=director_id | label=James Cameron
        {
          WebElement dropdown = driver.findElement(By.id("director_id"));
          dropdown.findElement(By.xpath("//option[. = 'James Cameron']")).click();
        }
        // 14 | click | css=.h-min > .flex | 
        driver.findElement(By.cssSelector(".h-min > .flex")).click();
        // 15 | click | css=#add-movie-btn path | 
        driver.findElement(By.cssSelector("#add-movie-btn")).click();
        // 16 | mouseOver | css=#add-movie-btn path | 
        {
          WebElement element = driver.findElement(By.cssSelector("#add-movie-btn"));
          Actions builder = new Actions(driver);
          builder.moveToElement(element).perform();
        }
        // 17 | mouseOut | css=#add-movie-btn path | 
        {
          WebElement element = driver.findElement(By.tagName("body"));
          Actions builder = new Actions(driver);
          builder.moveToElement(element, 0, 0).perform();
        }
        // 18 | click | id=title | 
        driver.findElement(By.id("title")).click();
        // 19 | type | id=title | Jurassic Park
        driver.findElement(By.id("title")).sendKeys("Jurassic Park");
        // 20 | click | id=description | 
        driver.findElement(By.id("description")).click();
        // 21 | type | id=description | Todo Espectador
        driver.findElement(By.id("description")).sendKeys("Todo Espectador");
        // 22 | click | id=year | 
        driver.findElement(By.id("year")).click();
        // 23 | type | id=year | 1993
        driver.findElement(By.id("year")).sendKeys("1993");
        // 24 | click | id=director_id | 
        driver.findElement(By.id("director_id")).click();
        // 25 | select | id=director_id | label=Steven Spielberg
        {
          WebElement dropdown = driver.findElement(By.id("director_id"));
          dropdown.findElement(By.xpath("//option[. = 'Steven Spielberg']")).click();
        }
        // 26 | click | css=.h-min > .flex | 
        driver.findElement(By.cssSelector(".h-min > .flex")).click();
        
        
      //test nuevas peliculas a Crittopher Nolan***************************
        
        driver.findElement(By.cssSelector("#add-movie-btn ")).click();
        // 4 | mouseOver | css=#add-movie-btn path | 
        {
          WebElement element = driver.findElement(By.cssSelector("#add-movie-btn "));
          Actions builder = new Actions(driver);
          builder.moveToElement(element).perform();
        }
        // 5 | mouseOut | css=#add-movie-btn path | 
        {
          WebElement element = driver.findElement(By.tagName("body"));
          Actions builder = new Actions(driver);
          builder.moveToElement(element, 0, 0).perform();
        }
        // 6 | click | id=title | 
        driver.findElement(By.id("title")).click();
        // 7 | type | id=title | Batman: El caballero de la noche asciende
        driver.findElement(By.id("title")).sendKeys("Batman: El caballero de la noche asciende");
        // 8 | click | id=description | 
        driver.findElement(By.id("description")).click();
        // 9 | type | id=description | Acción
        driver.findElement(By.id("description")).sendKeys("Acción");
        // 10 | type | id=year | 2010
        driver.findElement(By.id("year")).sendKeys("2010");
        // 11 | click | id=director_id | 
        driver.findElement(By.id("director_id")).click();
        // 12 | select | id=director_id | label=Cristopher Nolan
        {
          WebElement dropdown = driver.findElement(By.id("director_id"));
          dropdown.findElement(By.xpath("//option[. = 'Cristopher Nolan']")).click();
        }
        // 13 | click | css=.h-min > .flex | 
        driver.findElement(By.cssSelector(".h-min > .flex")).click();
        // 14 | click | css=#add-movie-btn path | 
        driver.findElement(By.cssSelector("#add-movie-btn ")).click();
        // 15 | click | id=title | 
        driver.findElement(By.id("title")).click();
        // 16 | type | id=title | Transcendence
        driver.findElement(By.id("title")).sendKeys("Transcendence");
        // 17 | click | id=description | 
        driver.findElement(By.id("description")).click();
        // 18 | type | id=description | IA
        driver.findElement(By.id("description")).sendKeys("IA");
        // 19 | click | id=year | 
        driver.findElement(By.id("year")).click();
        // 20 | type | id=year | 2012
        driver.findElement(By.id("year")).sendKeys("2012");
        // 21 | click | id=director_id | 
        driver.findElement(By.id("director_id")).click();
        // 22 | select | id=director_id | label=Cristopher Nolan
        {
          WebElement dropdown = driver.findElement(By.id("director_id"));
          dropdown.findElement(By.xpath("//option[. = 'Cristopher Nolan']")).click();
        }
        // 23 | click | css=.h-min > .flex | 
        driver.findElement(By.cssSelector(".h-min > .flex")).click();

        // Cierra el navegador al finalizar
        driver.quit();
    }
}