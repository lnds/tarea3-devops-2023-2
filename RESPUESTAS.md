# Rodrigo Saez

## Preguntas

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

Dentro de la pirámide Selenium evalua la calidad funcional, ya que las pruebas solo valida en este caso que la página web haga lo que debe. Selenium permite crear test de regresión, también test de aceptación con las pruebas de uso que haría un usuario.

2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

Si podemos encontrar dentro de la ruta movies-front/src/components los archivos AddDirector.test.js y AddMovies.test.js

3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?

Se debe agregar en la linea de command del servicio movies-api un && go test y la ruta donde se encuentran los archivos de prueba con el mismo nombre del componente  acompañado de _test.go