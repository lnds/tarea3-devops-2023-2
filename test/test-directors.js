const { Builder, By, Key, until } = require('selenium-webdriver');

async function addDirector(nameDirector) {
  // Inicializar el driver
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    // Navegar a una URL
    await driver.get('http://localhost:3000/');
 // Encontrar un elemento por su selector CSS, en este caso, un botón con el id 'myButton'
    let myButton = await driver.findElement(By.id(':r1:-tab-1'));
    await myButton.click();

    let addDirector = await driver.findElement(By.id('add-director-btn'));
    await addDirector.click();

    let inputDirector = await driver.findElement(By.id('name'));
    await inputDirector.sendKeys(nameDirector);

   let bttnAddDirector = await driver.findElement(By.id('bttnAddDirector'));
   await bttnAddDirector.click();

    // Esperar unos segundos para ver los resultados
    await driver.sleep(2000);
    } finally {
    // Cerrar el navegador al finalizar
    await driver.quit();
    }
}

  // Ejecutar la función
addDirector("Ridley Scott");
addDirector("James Cameron");