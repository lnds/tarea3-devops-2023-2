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
  public void 2peliculasaCristopherNolan() {
    driver.Navigate().GoToUrl("http://localhost:3000/");
    driver.Manage().Window.Size = new System.Drawing.Size(1920, 1048);
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
    driver.FindElement(By.Id("title")).SendKeys("Oppenheimer");
    driver.FindElement(By.Id("description")).Click();
    driver.FindElement(By.Id("description")).SendKeys("Un drama épico que adapta la vida de J. Robert Oppenheimer, considerado el padre de la bomba atómica. Tres horas repletas de intensidad, pero también de altibajos de interés, ya que funciona mucho mejor la última hora más centrada en las consecuencias de lo sucedido a nivel personal que lo anterior, donde hay ocasiones en las que resulta algo impostada e incluso hay momentos muy concretos que rozan el ridículo. A cambio, el despliegue técnico es impecable y Cillian Murphy está muy inspirado al frente de uno de los repartos más espectaculares de los últimos años.");
    driver.FindElement(By.Id("year")).Click();
    driver.FindElement(By.Id("year")).SendKeys("2023");
    driver.FindElement(By.Id("director_id")).Click();
    {
      var dropdown = driver.FindElement(By.Id("director_id"));
      dropdown.FindElement(By.XPath("//option[. = 'Cristopher Nolan']")).Click();
    }
    driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
    driver.FindElement(By.Id(":r1:-tab-1")).Click();
    driver.FindElement(By.Id(":r1:-tab-0")).Click();
    driver.FindElement(By.CssSelector(".mb-10:nth-child(2) .mb-4:nth-child(4)")).Click();
    driver.FindElement(By.CssSelector("#add-movie-btn path")).Click();
    driver.FindElement(By.Id("title")).Click();
    driver.FindElement(By.Id("title")).SendKeys("Inception");
    driver.FindElement(By.Id("year")).Click();
    driver.FindElement(By.Id("year")).SendKeys("2010");
    driver.FindElement(By.Id("director_id")).Click();
    {
      var dropdown = driver.FindElement(By.Id("director_id"));
      dropdown.FindElement(By.XPath("//option[. = 'Cristopher Nolan']")).Click();
    }
    driver.FindElement(By.Id("description")).Click();
    driver.FindElement(By.Id("description")).SendKeys("Probablemente sea uno de los blockbusters favoritos de los flipados con ínfulas -que son solamente una pequeña parte de los seguidores de esta impactante película, no creáis aquí lo que no es-, pero eso no quita para que sea un grandioso espectáculo en el que Nolan aprovechó a tope su libertad para sacar adelante una cinta así sin formar parte de una franquicia o adaptar algo de éxito probado. Es cierto que quizá explique de más alguna cosa -y aún muchos no la entendieron- y que el cineasta se recrea más de la cuenta en algunos aspectos, pero también que a su manera fue el cierre de su etapa más, por así decirlo, pesimista y que aún hoy sigue funcionando como un tiro.");
    driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
    {
      var element = driver.FindElement(By.CssSelector(".h-min > .flex"));
      Actions builder = new Actions(driver);
      builder.MoveToElement(element).Perform();
    }
  }
}
