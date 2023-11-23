const { Builder, By, Key, until } = require('selenium-webdriver');
const { Select } = require('selenium-webdriver');

async function addMovie(titleMovie, descriptionMovie, yearMovie, directorMovie) {
    // Inicializar el driver
    let driver = await new Builder().forBrowser('chrome').build();
  
    try {
      // Navegar a una URL
      await driver.get('http://localhost:3000/');
  
      let addMovie = await driver.findElement(By.id('add-movie-btn'));
      await addMovie.click();
  
      let title = await driver.findElement(By.id('title'));
      await title.sendKeys(titleMovie);

      let description = await driver.findElement(By.id('description'));
      await description.sendKeys(descriptionMovie);

      let year = await driver.findElement(By.id('year'));
      await year.sendKeys(yearMovie);


      let mySelect = await driver.findElement(By.id('director_id'));
      let select = new Select(mySelect);
      await select.selectByValue(directorMovie); 
  
      let btnAddMovie = await driver.findElement(By.id('btnAddMovie'));
       await btnAddMovie.click();
  
      // Esperar unos segundos para ver los resultados
       await driver.sleep(4000);
      } finally {
      // Cerrar el navegador al finalizar
        await driver.quit();
      }
  }

  // Ejecutar la función
//addMovies a cada director
addMovie("Memento", "Basada en Memento Mori, de Jonathan Nolan", "2000","1")
addMovie("Little Women", "Gerwig altera cronológicamente la trama de la obra y alterna pasajes de los primeros años de las niñas con su vida profesional, con la intención de hacer una nueva visión de la novela tras 150 años, haciendo hincapié en el subtexto feminista de la obra.", "2019","2")
addMovie("Gladiador", "es una película épica del género péplum y acción del año 2000 dirigida por Ridley Scott y protagonizada por Russell Crowe, Joaquin Phoenix y Connie Nielsen. ", "2000","3")
addMovie("Avatar", "es una película épica de ciencia ficción militar y animación estadounidense de 2009,5​6​ escrita, producida y dirigida por James Cameron y protagonizada por Sam Worthington, Zoe Saldaña, Sigourney Weaver, Stephen Lang y Michelle Rodriguez.", "2009","4")


//add 2 movies de Crhistopher Nolan

addMovie("Batman Begins", "es una película de superhéroes británica-estadounidense de 2005 basada en el personaje Batman de DC Comics, dirigida por el cineasta inglés Christopher Nolan, escrita por Nolan y David S. Goyer y protagonizada por Christian Bale, Michael Caine, Liam Neeson, Katie Holmes, Gary Oldman, Cillian Murphy, Tom Wilkinson, Rutger Hauer, con Ken Watanabe y Morgan Freeman.", "2005","1")
addMovie("Interstellar", "es una película épica de drama y ciencia ficción británico-estadounidense y canadiense de 2014, dirigida por Christopher Nolan y protagonizada por Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine y Matt Damon.", "2014","1")