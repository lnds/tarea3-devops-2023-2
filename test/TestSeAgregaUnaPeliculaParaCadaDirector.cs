using System;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

[TestFixture]
public class TestSeAgregaUnaPeliculaParaCadaDirector
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
    public void TestSeAgregaUnaPeliculaParaCadaDirector()
    {
        driver.Close();
        driver.Navigate().GoToUrl("http://localhost:3000/");
        driver.Manage().Window.Size = new System.Drawing.Size(1505, 803);
        driver.FindElement(By.Id(":r1:-tab-0")).Click();
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click();
        driver.FindElement(By.Id("title")).Click();
        driver.FindElement(By.Id("title")).SendKeys("movie 1");
        driver.FindElement(By.Id("description")).SendKeys("test desc");
        driver.FindElement(By.Id("year")).SendKeys("2022");
        var directorDropdown1 = new SelectElement(driver.FindElement(By.Id("director_id")));
        directorDropdown1.SelectByText("test 1");
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click();
        driver.FindElement(By.Id("title")).Click();
        driver.FindElement(By.Id("title")).SendKeys("movie 2");
        driver.FindElement(By.Id("description")).SendKeys("test desc 2");
        driver.FindElement(By.Id("year")).Click();
        driver.FindElement(By.Id("year")).SendKeys("2023");
        driver.FindElement(By.Id("director_id")).Click();
        var directorDropdown2 = new SelectElement(driver.FindElement(By.Id("director_id")));
        directorDropdown2.SelectByText("test 2");
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click();
    }
}
