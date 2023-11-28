@@ -0,0 +1,54 @@
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

        ' Agrega pelicula 1
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click()
        driver.FindElement(By.Id("title")).Click()
        driver.FindElement(By.Id("title")).SendKeys("Volver")
        driver.FindElement(By.Id("description")).Click()
        driver.FindElement(By.Id("description")).SendKeys("Volver es una película española de 2006 escrita y dirigida por Pedro Almodóvar. Está interpretada por Penélope Cruz, Carmen Maura,")
        driver.FindElement(By.Id("year")).Click()
        driver.FindElement(By.Id("year")).SendKeys("2006")
        driver.FindElement(By.Id("director_id")).Click()
        directorDropdown = driver.FindElement(By.Id("director_id"))
        directorDropdown.FindElement(By.XPath("//option[. = 'Pedro Almodovar']")).Click()
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()

        ' Agrega película 2
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click()
        driver.FindElement(By.Id("title")).Click()
        driver.FindElement(By.Id("title")).SendKeys("Schindler's List")
        driver.FindElement(By.Id("description")).Click()
        driver.FindElement(By.Id("description")).SendKeys("Schindler's List is a 1993 American epic historical drama film directed and produced by Steven Spielberg and written by Steven Zaillian.")
        driver.FindElement(By.Id("year")).Click()
        driver.FindElement(By.Id("year")).SendKeys("1993")
        driver.FindElement(By.Id("director_id")).Click()
        Dim directorDropdown = driver.FindElement(By.Id("director_id"))
        directorDropdown.FindElement(By.XPath("//option[. = 'Steven Spielberg']")).Click()
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()

    End Sub
End Class