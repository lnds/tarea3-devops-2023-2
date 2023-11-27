Imports System
Imports NUnit.Framework
Imports OpenQA.Selenium
Imports OpenQA.Selenium.Chrome
Imports OpenQA.Selenium.Support.UI

<TestFixture>
Public Class TestCaso2Agrega1PeliculaPorCadaNuevoDirector
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
    Public Sub TestCaso2Agrega1PeliculaPorCadaNuevoDirector()
        driver.Navigate().GoToUrl("http://localhost:3000/")

        ' Agrega la primera película
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click()
        driver.FindElement(By.Id("title")).Click()
        driver.FindElement(By.Id("title")).SendKeys("Jurassic Park")
        driver.FindElement(By.Id("description")).Click()
        driver.FindElement(By.Id("description")).SendKeys("Pelicula de Dinosaurios creados por Ingen de John Hammond.")
        driver.FindElement(By.Id("year")).Click()
        driver.FindElement(By.Id("year")).SendKeys("1993")
        driver.FindElement(By.Id("director_id")).Click()
        Dim directorDropdown = driver.FindElement(By.Id("director_id"))
        directorDropdown.FindElement(By.XPath("//option[. = 'Steven Spielberg']")).Click()
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()

        ' Agrega la segunda película
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click()
        driver.FindElement(By.Id("title")).Click()
        driver.FindElement(By.Id("title")).SendKeys("Transformers")
        driver.FindElement(By.Id("description")).Click()
        driver.FindElement(By.Id("description")).SendKeys("Pelicula de Guerra entre robots extraterrestres (Autobots vs Decepticons)")
        driver.FindElement(By.Id("year")).Click()
        driver.FindElement(By.Id("year")).SendKeys("2007")
        driver.FindElement(By.Id("director_id")).Click()
        directorDropdown = driver.FindElement(By.Id("director_id"))
        directorDropdown.FindElement(By.XPath("//option[. = 'Michael Bay']")).Click()
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()
    End Sub
End Class