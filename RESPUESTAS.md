## RESPUESTAS

## RODRIGO MUÑOZ

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).
   R: Dentro de la pirámide de calidad, los test de selenium se ubican en lo referente a calidad funcional, y en particular, el tipo de prueba corresponde a un test de aceptación, ya que prueba el comportamiento de la aplicación, a la vez que se testea la integración entre servicio front-end y back-end, y permite también realizar test de regresión en la medida que se verifica que los cambios efectuados en el código no hayan afectado de manera inesperada a otros servicios.

2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?
   R: El front-end tiene test unitarios definidos en los archivos src/components/AddDirector.test.js y src/components/AddMovie.test.js

3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?
   R: Para correr los test unitarios del backend (movies-api), se debe declarar el comando 'go test' en el archivo docker.compose.yml en el servicio movies-api en la sección command, para que este sea ejecutado cuando se levanta el docker compose.
