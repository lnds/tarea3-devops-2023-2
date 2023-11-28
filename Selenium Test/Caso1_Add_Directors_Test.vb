@@ -0,0 +1,47 @@
Imports System
Imports NUnit.Framework
Imports OpenQA.Selenium
Imports OpenQA.Selenium.Chrome
Imports OpenQA.Selenium.Support.UI

<TestFixture>
Public Class TestCaso1Agrega2Directores
    Private driver As IWebDriver
    Private wait As WebDriverWait

    <SetUp>
    Public Sub Setup()
        driver = New ChromeDriver()
        driver.Manage().Window.Size = New System.Drawing.Size(1382, 744)
        wait = New WebDriverWait(driver, TimeSpan.FromSeconds(10))
    End Sub

    <TearDown>
    Public Sub Teardown()
        driver.Quit()
    End Sub

    <Test>
    Public Sub TestCaso1Agrega2Directores()
        driver.Navigate().GoToUrl("http://localhost:3000/")

        ' Agrega el primer director
        driver.FindElement(By.Id(":r1:-tab-1")).Click()
        Dim element = driver.FindElement(By.CSSSelector("#add-director-btn .w-16"))
        Dim actions = New ActionChains(driver)
        actions.MoveToElement(element).Perform()
        driver.FindElement(By.CSSSelector("#add-director-btn .w-16")).Click()
        element = driver.FindElement(By.CssSelector("body"))
        actions = New ActionChains(driver)
        actions.MoveToElement(element, 0, 0).Perform()
        driver.FindElement(By.Id("name")).Click()
        driver.FindElement(By.Id("name")).SendKeys("Steven Spielberg")
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()

        ' Agrega el segundo director
        driver.FindElement(By.CSSSelector("#add-director-btn .w-16")).Click()
        driver.FindElement(By.Id("name")).Click()
        driver.FindElement(By.Id("name")).SendKeys("Pedro Almodovar")
        driver.FindElement(By.CssSelector(".h-min > .flex")).Click()
    End Sub
End Class