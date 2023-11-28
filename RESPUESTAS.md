Tomás Sánchez

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test corresponde (regresión, integración, aceptación, etc).

Se ubica en la cúspide de la pirámide de testing, calidad funcional, y corresponde al tipo test regresión.

2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

el front si contiene los test unitarios, se encuentran definidos en los archivos con la extension "test" dentro de su nombre, como por ejemplo  AddDirector.test.js


3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?

esta podría ser una opción /movies-api -b ${BIND_IP} -p ${BIND_PORT} ; go test, de todas formar el dockerfile se necesita configurar.-
