using System;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

[TestFixture]
public class TestAgregarPeliculasANolan
{
    private IWebDriver driver;
    private WebDriverWait wait;

    [SetUp]
    public void SetUp()
    {
        driver = new ChromeDriver();
        wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));
    }

    [TearDown]
    public void TearDown()
    {
        driver.Quit();
    }

    [Test]
    public void TestAgregarPeliculasANolan()
    {
        driver.Navigate().GoToUrl("http://localhost:3000/");
        driver.Manage().Window.Size = new System.Drawing.Size(1505, 803);
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click();
        var element1 = driver.FindElement(By.CssSelector("#add-movie-btn .w-16"));
        var actions1 = new Actions(driver);
        actions1.MoveToElement(element1).Perform();
        var element2 = driver.FindElement(By.CssSelector("body"));
        var actions2 = new Actions(driver);
        actions2.MoveToElement(element2, 0, 0).Perform();
        driver.FindElement(By.Id("title")).Click();
        driver.FindElement(By.Id("title")).SendKeys("movie nolan 1");
        driver.FindElement(By.Id("description")).SendKeys("test");
        driver.FindElement(By.Id("year")).Click();
        driver.FindElement(By.Id("year")).SendKeys("2025");
        driver.FindElement(By.Id("director_id")).Click();
        var directorDropdown1 = new SelectElement(driver.FindElement(By.Id("director_id")));
        directorDropdown1.SelectByText("Cristopher Nolan");
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
        driver.FindElement(By.CssSelector("#add-movie-btn path")).Click();
        driver.FindElement(By.Id("title")).Click();
        driver.FindElement(By.Id("title")).SendKeys("movie nolan 2");
        driver.FindElement(By.Id("description")).Click();
        driver.FindElement(By.Id("description")).SendKeys("test 2");
        driver.FindElement(By.Id("year")).Click();
        driver.FindElement(By.Id("year")).SendKeys("2026");
        driver.FindElement(By.Id("director_id")).Click();
        var directorDropdown2 = new SelectElement(driver.FindElement(By.Id("director_id")));
        directorDropdown2.SelectByText("Cristopher Nolan");
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
    }
}