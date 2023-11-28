## Alumno
Alejandro Montoya
Nota: se incorpora container selenium en donde se puede realizar la ejecucion de las pruebas (se deja un archivo main y archivos para cada test).

## 1.- Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).
R: Selenium es del tipo UI Testing, Webdriver permite crear test de regresion, selenium Grid son servidores que permiten ejecutar nuestros script y Selenium IDE que fue el usado en este ejecicio corresponde a test de integracion. Ya que simula al usuario y asi se verifica las interacciones entre las distintas piezas de software.

## 2.- Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?
R: Contine dos test unitarios, uno para cada accion de la aplicacion. Boton Agregar directores (AddDirector.test.js) y Boton agregar peliculas (AddMovie.test.js)

## 3.-Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?
R: se debe cambiar el comando actual a "./movies-api server_test.go -b ${BIND_IP} -p ${BIND_PORT}" en el servicio movies-api