package test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;

public class SeleniuntTest {
	 public static void main(String[] args) {
		 
		 System.setProperty("webdriver.gecko.driver", "C:\\Workspace-SpringTools\\test\\ruta\\geckodriver.exe");
		 
		   //Inicializa el WebDriver
           WebDriver driver = new FirefoxDriver();
           // 1 | open | / | 
           driver.get("http://localhost:3000/");
           // 2 | setWindowSize | 812x866 | 
           driver.manage().window().setSize(new Dimension(812, 866));
           // 3 | click | id=:r1:-tab-1 | 
           driver.findElement(By.id(":r1:-tab-1")).click();
           // 4 | click | css=#add-director-btn .w-16 | 
           driver.findElement(By.cssSelector("#add-director-btn .w-16")).click();
           // 5 | click | id=name | 
           driver.findElement(By.id("name")).click();
           // 6 | type | id=name | Pablo Larrain
           driver.findElement(By.id("name")).sendKeys("Pablo Larrain");
           // 7 | click | css=.h-min > .flex | 
           driver.findElement(By.cssSelector(".h-min > .flex")).click();
           // 8 | mouseOver | css=.h-min > .flex | 
           {
             WebElement element = driver.findElement(By.cssSelector(".h-min > .flex"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element).perform();
           }
           // 9 | click | css=#add-director-btn .w-16 | 
           driver.findElement(By.cssSelector("#add-director-btn .w-16")).click();
           // 10 | mouseOver | css=#add-director-btn .w-16 | 
           {
             WebElement element = driver.findElement(By.cssSelector("#add-director-btn .w-16"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element).perform();
           }
           // 11 | mouseOut | css=#add-director-btn .w-16 | 
           {
             WebElement element = driver.findElement(By.tagName("body"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element, 0, 0).perform();
           }
           // 12 | click | id=name | 
           driver.findElement(By.id("name")).click();
           // 13 | type | id=name | Andrés Wood
           driver.findElement(By.id("name")).sendKeys("Andrés Wood");
           // 14 | click | css=.h-min > .flex | 
           driver.findElement(By.cssSelector(".h-min > .flex")).click();
           // 15 | click | id=:r1:-tab-0 | 
           driver.findElement(By.id(":r1:-tab-0")).click();
           // 16 | click | css=#add-movie-btn .w-16 | 
           driver.findElement(By.cssSelector("#add-movie-btn .w-16")).click();
           // 17 | click | id=title | 
           driver.findElement(By.id("title")).click();
           // 18 | click | css=.top-0 | 
           driver.findElement(By.cssSelector(".top-0")).click();
           // 19 | click | css=.ml-auto > .h-5 | 
           driver.findElement(By.cssSelector(".ml-auto > .h-5")).click();
          
           /*Test 2*/
           
           // 3 | click | id=:r1:-tab-1 | 
           driver.findElement(By.id(":r1:-tab-1")).click();
           // 4 | click | id=:r1:-tab-0 | 
           driver.findElement(By.id(":r1:-tab-0")).click();
           // 5 | click | css=#add-movie-btn .w-16 | 
           driver.findElement(By.cssSelector("#add-movie-btn .w-16")).click();
           // 6 | click | id=title | 
           driver.findElement(By.id("title")).click();
           // 7 | type | id=title | Machuca
           driver.findElement(By.id("title")).sendKeys("Machuca");
           // 8 | type | id=description | Dos niños chilenos de 12 años de diferenbtes clases sociales se hacen amigos en 1073. Ambos descubreb el mundo del otro mientras aumentan las tensiones politicas en su país.
           driver.findElement(By.id("description")).sendKeys("Dos niños chilenos de 12 años de diferenbtes clases sociales se hacen amigos en 1073. Ambos descubreb el mundo del otro mientras aumentan las tensiones politicas en su país.");
           // 9 | click | id=year | 
           driver.findElement(By.id("year")).click();
           // 10 | type | id=year | 2003
           driver.findElement(By.id("year")).sendKeys("2003");
           // 11 | click | id=description | 
           driver.findElement(By.id("description")).click();
           // 12 | click | id=description | 
           driver.findElement(By.id("description")).click();
           // 13 | type | id=description | Dos niños chilenos de 12 años de diferenbtes clases sociales se hacen amigos en 1973. Ambos descubreb el mundo del otro mientras aumentan las tensiones politicas en su país.
           driver.findElement(By.id("description")).sendKeys("Dos niños chilenos de 12 años de diferenbtes clases sociales se hacen amigos en 1973. Ambos descubreb el mundo del otro mientras aumentan las tensiones politicas en su país.");
           // 14 | click | id=director_id | 
           driver.findElement(By.id("director_id")).click();
           // 15 | select | id=director_id | label=Andrés Wood
           {
             WebElement dropdown = driver.findElement(By.id("director_id"));
             dropdown.findElement(By.xpath("//option[. = 'Andrés Wood']")).click();
           }
           // 16 | click | css=.h-min > .flex | 
           driver.findElement(By.cssSelector(".h-min > .flex")).click();
           // 17 | click | id=:r1:-tab-1 | 
           driver.findElement(By.id(":r1:-tab-1")).click();
           // 18 | click | id=:r1:-tab-0 | 
           driver.findElement(By.id(":r1:-tab-0")).click();
           // 19 | click | css=#add-movie-btn path | 
           driver.findElement(By.cssSelector("#add-movie-btn path")).click();
           // 20 | mouseOver | css=#add-movie-btn path | 
           {
             WebElement element = driver.findElement(By.cssSelector("#add-movie-btn path"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element).perform();
           }
           // 21 | mouseOut | css=#add-movie-btn path | 
           {
             WebElement element = driver.findElement(By.tagName("body"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element, 0, 0).perform();
           }
           // 22 | click | id=title | 
           driver.findElement(By.id("title")).click();
           // 23 | type | id=title | Tony Manero
           driver.findElement(By.id("title")).sendKeys("Tony Manero");
           // 24 | click | id=description | 
           driver.findElement(By.id("description")).click();
           // 25 | type | id=description | Pelicula de un hombre de cerca de 50 años obsesionado con el personaje Tony Manero, encarnado por Jhon Travolta en la pelicula Saturday Night Fever, dedicado a simular sus modismos y sus grandes desplieges en el baile.
           driver.findElement(By.id("description")).sendKeys("Pelicula de un hombre de cerca de 50 años obsesionado con el personaje Tony Manero, encarnado por Jhon Travolta en la pelicula Saturday Night Fever, dedicado a simular sus modismos y sus grandes desplieges en el baile.");
           // 26 | click | id=year | 
           driver.findElement(By.id("year")).click();
           // 27 | type | id=year | 2008
           driver.findElement(By.id("year")).sendKeys("2008");
           // 28 | click | id=director_id | 
           driver.findElement(By.id("director_id")).click();
           // 29 | select | id=director_id | label=Pablo Larrain
           {
             WebElement dropdown = driver.findElement(By.id("director_id"));
             dropdown.findElement(By.xpath("//option[. = 'Pablo Larrain']")).click();
           }
           // 30 | click | css=.h-min > .flex | 
           driver.findElement(By.cssSelector(".h-min > .flex")).click();
           // 31 | mouseOver | css=.h-min > .flex | 
           {
             WebElement element = driver.findElement(By.cssSelector(".h-min > .flex"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element).perform();
           }
           
           /*Test 3*/
        // 3 | click | id=:r1:-tab-1 | 
           driver.findElement(By.id(":r1:-tab-1")).click();
           // 4 | click | css=#add-director-btn .w-16 | 
           driver.findElement(By.cssSelector("#add-director-btn .w-16")).click();
           // 5 | click | id=name | 
           driver.findElement(By.id("name")).click();
           // 6 | type | id=name | Pablo Larrain
           driver.findElement(By.id("name")).sendKeys("Pablo Larrain");
           // 7 | click | css=.h-min > .flex | 
           driver.findElement(By.cssSelector(".h-min > .flex")).click();
           // 8 | mouseOver | css=.h-min > .flex | 
           {
             WebElement element = driver.findElement(By.cssSelector(".h-min > .flex"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element).perform();
           }
           // 9 | click | css=#add-director-btn .w-16 | 
           driver.findElement(By.cssSelector("#add-director-btn .w-16")).click();
           // 10 | mouseOver | css=#add-director-btn .w-16 | 
           {
             WebElement element = driver.findElement(By.cssSelector("#add-director-btn .w-16"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element).perform();
           }
           // 11 | mouseOut | css=#add-director-btn .w-16 | 
           {
             WebElement element = driver.findElement(By.tagName("body"));
             Actions builder = new Actions(driver);
             builder.moveToElement(element, 0, 0).perform();
           }
           // 12 | click | id=name | 
           driver.findElement(By.id("name")).click();
           // 13 | type | id=name | Andrés Wood
           driver.findElement(By.id("name")).sendKeys("Andrés Wood");
           // 14 | click | css=.h-min > .flex | 
           driver.findElement(By.cssSelector(".h-min > .flex")).click();
           // 15 | click | id=:r1:-tab-0 | 
           driver.findElement(By.id(":r1:-tab-0")).click();
           // 16 | click | css=#add-movie-btn .w-16 | 
           driver.findElement(By.cssSelector("#add-movie-btn .w-16")).click();
           // 17 | click | id=title | 
           driver.findElement(By.id("title")).click();
           // 18 | click | css=.top-0 | 
           driver.findElement(By.cssSelector(".top-0")).click();
           // 19 | click | css=.ml-auto > .h-5 | 
           driver.findElement(By.cssSelector(".ml-auto > .h-5")).click();
           driver.quit();
         }	 
	 }

