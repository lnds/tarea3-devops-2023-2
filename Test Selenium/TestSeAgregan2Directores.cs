using System;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

[TestFixture]
public class TestSeAgregan2Directores
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
    public void TestSeAgregan2Directores()
    {
        driver.Navigate().GoToUrl("http://localhost:3000/");
        driver.Manage().Window.Size = new System.Drawing.Size(1936, 1048);
        driver.FindElement(By.Id(":r1:-tab-1")).Click();
        driver.FindElement(By.CSS_SELECTOR, "#add-director-btn path").Click();
        driver.FindElement(By.ID, "name").Click();
        driver.FindElement(By.ID, "name").SendKeys("test 1");
        driver.FindElement(By.CSS_SELECTOR, ".h-min > .flex").Click();
        driver.FindElement(By.CSS_SELECTOR, "#add-director-btn path").Click();
        var element1 = driver.FindElement(By.CSS_SELECTOR, "#add-director-btn path");
        var actions1 = new Actions(driver);
        actions1.MoveToElement(element1).Perform();
        var element2 = driver.FindElement(By.CssSelector("body"));
        var actions2 = new Actions(driver);
        actions2.MoveToElement(element2, 0, 0).Perform();
        driver.FindElement(By.ID, "name").Click();
        driver.FindElement(By.ID, "name").SendKeys("test 2");
        driver.FindElement(By.CSS_SELECTOR, ".h-min > .flex").Click();
        driver.FindElement(By.ID(":r1:-tab-0")).Click();
        driver.FindElement(By.CSS_SELECTOR, "#add-movie-btn path").Click();
    }
}