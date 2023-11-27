using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Remote;
using OpenQA.Selenium.Support.UI;
using OpenQA.Selenium.Interactions;
using Xunit;
public class SuiteTests : IDisposable {
  public IWebDriver driver {get; private set;}
  public IDictionary<String, Object> vars {get; private set;}
  public IJavaScriptExecutor js {get; private set;}
  public SuiteTests()
  {
    driver = new ChromeDriver();
    js = (IJavaScriptExecutor)driver;
    vars = new Dictionary<String, Object>();
  }
  public void Dispose()
  {
    driver.Quit();
  }
  [Fact]
  public void Agregarpeliculasadirectores() {
    driver.Navigate().GoToUrl("http://localhost:3000/");
    driver.Manage().Window.Size = new System.Drawing.Size(1920, 1048);
    driver.FindElement(By.CssSelector("html")).Click();
    driver.FindElement(By.CssSelector("#add-movie-btn path")).Click();
    {
      var element = driver.FindElement(By.CssSelector("#add-movie-btn path"));
      Actions builder = new Actions(driver);
      builder.MoveToElement(element).Perform();
    }
    {
      var element = driver.FindElement(By.tagName("body"));
      Actions builder = new Actions(driver);
      builder.MoveToElement(element, 0, 0).Perform();
    }
    driver.FindElement(By.Id("title")).Click();
    driver.FindElement(By.Id("title")).SendKeys("El planeta de los simios");
    driver.FindElement(By.Id("description")).SendKeys("En lo más bajo de la lista encontramos el intento de Tim Burton de reinventar la franquicia de \'El planeta de los simios\', algo que claramente no le salió tan bien como unos años después a Matt Reeves con su brillante trilogía de precuelas de la historia. Aquí, Tim Burton se aventuró a realiza un remake de una de las películas de ciencia ficción más aclamadas de la historia y con uno de los mejores giros de guion sorpresa del cine.\\n\\nSin embargo, las ambiciones no fueron acompañadas de resultados, que fueron bastante deslucidos. Con su habitual colaboradora Helena Bonham Carter y el protagonismo de Mark Wahlberg, el director no logró salir airoso de este reto mayúsculo. Según los fans en IMDb, es la peor película de Tim Burton. Ouch.");
    driver.FindElement(By.Id("year")).Click();
    driver.FindElement(By.Id("year")).SendKeys("2005");
    driver.FindElement(By.Id("director_id")).Click();
    {
      var dropdown = driver.FindElement(By.Id("director_id"));
      dropdown.FindElement(By.XPath("//option[. = 'Tim Barton']")).Click();
    }
    driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
    {
      var element = driver.FindElement(By.CssSelector(".h-min > .flex"));
      Actions builder = new Actions(driver);
      builder.MoveToElement(element).Perform();
    }
    driver.FindElement(By.CssSelector("#add-movie-btn path")).Click();
    driver.FindElement(By.Id("title")).Click();
    driver.FindElement(By.Id("title")).SendKeys("Kill Bill");
    driver.FindElement(By.Id("description")).SendKeys("Sinopsis: Los miembros (Daryl Hannah, Vivica A. Fox, Michael Madsen y Lucy Liu) del Escuadrón Asesino Víbora Letal, también conocido como DiVAS, irrumpen en la boda de una ex compañera, apodada antiguamente Mamba Negra (Uma Thurman), dispuestos a matar a todos los presentes... pero ella sobrevive. La venganza está servida.");
    driver.FindElement(By.Id("year")).Click();
    driver.FindElement(By.Id("year")).SendKeys("2003");
    driver.FindElement(By.Id("director_id")).Click();
    {
      var dropdown = driver.FindElement(By.Id("director_id"));
      dropdown.FindElement(By.XPath("//option[. = 'Quentin Tarantino']")).Click();
    }
    driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
  }
}
