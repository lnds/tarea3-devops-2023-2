## 1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

R1: En la pirámide de testing, los test de Selenium se ubican en la calidad funcional. Y corresponde al tipo de test aceptación e integración.

## 2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

R2: Tiene dos test unitarios: AddDirector.test.js y AddMovie.test.js en la ruta movies-front/src/components


## 3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?


R3: Hay que cambiar la línea command:  ./movies-api -b ${BIND_IP} -p ${BIND_PORT} y dejarla de l siguiente manera: 
./movies-api -b ${BIND_IP} -p ${BIND_PORT} && go test

