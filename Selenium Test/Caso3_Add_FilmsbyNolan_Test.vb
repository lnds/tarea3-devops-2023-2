@@ -0,0 +1,54 @@
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
        driver.FindElement(By.Id("title")).SendKeys("Inception")
        driver.FindElement(By.Id("description")).Click()
        driver.FindElement(By.Id("description")).SendKeys("The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious of his targets.")
        driver.FindElement(By.Id("year")).Click()
        driver.FindElement(By.Id("year")).SendKeys("2020")
        driver.FindElement(By.Id("director_id")).Click()
        Dim directorDropdown = driver.FindElement(By.Id("director_id"))
        directorDropdown.FindElement(By.XPath("//option[. = 'Cristopher Nolan']")).Click()
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()

        ' Agrega la segunda película
        driver.FindElement(By.CssSelector("#add-movie-btn .w-16")).Click()
        driver.FindElement(By.Id("title")).Click()
        driver.FindElement(By.Id("title")).SendKeys("The Dark Knight")
        driver.FindElement(By.Id("description")).Click()
        driver.FindElement(By.Id("description")).SendKeys("Based on the DC Comics superhero Batman, it is the sequel to Batman Begins (2005) and the second installment in The Dark Knight Trilogy.")
        driver.FindElement(By.Id("year")).Click()
        driver.FindElement(By.Id("year")).SendKeys("2008")
        driver.FindElement(By.Id("director_id")).Click()
        directorDropdown = driver.FindElement(By.Id("director_id"))
        directorDropdown.FindElement(By.XPath("//option[. = 'Cristopher Nolan']")).Click()
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()
    End Sub
End Class