Imports System
Imports NUnit.Framework
Imports OpenQA.Selenium
Imports OpenQA.Selenium.Chrome
Imports OpenQA.Selenium.Support.UI

<TestFixture>
Public Class TestCaso3Agrega2PeliculasDirectorNolan
    Private driver As IWebDriver
    Private wait As WebDriverWait

    <SetUp>
    Public Sub Setup()
        driver = New ChromeDriver()
        driver.Manage().Window.Size = New System.Drawing.Size(1050, 708)
        wait = New WebDriverWait(driver, TimeSpan.FromSeconds(10))
    End Sub

    <TearDown>
    Public Sub Teardown()
        driver.Quit()
    End Sub

    <Test>
    Public Sub TestCaso3Agrega2PeliculasDirectorNolan()
        driver.Navigate().GoToUrl("http://localhost:3000/")

        ' Agrega la primera película
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click()
        driver.FindElement(By.Id("title")).Click()
        driver.FindElement(By.Id("title")).SendKeys("Batman Begins")
        driver.FindElement(By.Id("description")).Click()
        driver.FindElement(By.Id("description")).SendKeys("Como Bruce Wayne, un joven multimillonario se convirtió en un superhéroe de la ciudad Gotham.")
        driver.FindElement(By.Id("year")).Click()
        driver.FindElement(By.Id("year")).SendKeys("2015")
        driver.FindElement(By.Id("director_id")).Click()
        Dim directorDropdown = driver.FindElement(By.Id("director_id"))
        directorDropdown.FindElement(By.XPath("//option[. = 'Cristopher Nolan']")).Click()
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()

        ' Agrega la segunda película
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click()
        driver.FindElement(By.Id("title")).Click()
        driver.FindElement(By.Id("title")).SendKeys("Interstellar")
        driver.FindElement(By.Id("description")).Click()
        driver.FindElement(By.Id("description")).SendKeys("Película inspirada en la teoría del experto en relatividad Kip Stephen sobre la existencia de agujeros negros.")
        driver.FindElement(By.Id("year")).Click()
        driver.FindElement(By.Id("year")).SendKeys("2014")
        driver.FindElement(By.Id("director_id")).Click()
        directorDropdown = driver.FindElement(By.Id("director_id"))
        directorDropdown.FindElement(By.XPath("//option[. = 'Cristopher Nolan']")).Click()
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()
    End Sub
End Class