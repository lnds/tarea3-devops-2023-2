Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).
RESPUESTA:
Selenium se ajusta a la parte superior de la pirámide, lo que implica pruebas de interfaz de usuario. Por lo tanto, se utiliza principalmente para realizar pruebas de aceptación y, en algunos casos, pruebas de regresión.

Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?
RESPUESTA:
El FrontEnd cuenta con test unitarios y se encuentran definidos en los siguientes archivos: movies-front/src/component, `AddMovie.test.js` y `AddDirector.test.js`


Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?
RESPUESTA:
Para probar los test unitarios se deben realizar los siguiente cambios en el servicio `movies-api` del docker-compose:

1. Modificar el valor de `target` de la propiedad `build` a  `build-stage`. 
2. En la propiedad `command` se debe modificar por `go test`.


NOTA: SE AGREGA LA CARPETA "test-selenium" CON PROYECTO JAVA.