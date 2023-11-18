Nombre: Sebastian Ignacio Jara Castro


1- Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

Se ubican en la parte superior de la pirámide, en el sector de la calidad funcional. Corresponden a tests de tipo de aceptación, porque buscan probar el comportamiento de la aplicación
de la misma manera en que un usuario lo haría. Se podría decir que en algunos esto también podría considerarse como test de integración, ya que varios componentes podrian estar interactuando entre sí.

2- Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

Si tiene tests unitarios, se encuentran definidos en AddDirector.test.js y AddMovie.test.js

3- Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?

Se podria modificar el comando que se ejecuta agregando "go test" : command: ["sh", "-c", "go test ./... && exec /movies-api -b ${BIND_IP} -p ${BIND_PORT}"]