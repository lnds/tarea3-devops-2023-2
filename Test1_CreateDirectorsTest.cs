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
  public void CreateDirectors() {
    driver.Navigate().GoToUrl("http://localhost:3000/");
    driver.Manage().Window.Size = new System.Drawing.Size(1920, 1048);
    driver.FindElement(By.Id(":r1:-tab-1")).Click();
    driver.FindElement(By.CssSelector("#add-director-btn path")).Click();
    driver.FindElement(By.Id("name")).Click();
    driver.FindElement(By.Id("name")).SendKeys("Quentin Tarantino");
    driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
    driver.FindElement(By.CssSelector("#add-director-btn path")).Click();
    driver.FindElement(By.Id("name")).Click();
    driver.FindElement(By.Id("name")).SendKeys("Tim Burton");
    driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
  }
}
