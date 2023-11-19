# Respuestas Cristian Luttgue

## Todos los test se encuentran en la carpeta test del directorio

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

Selenium puede ser utilizado para pruebas de regresión y funcionales, debido a que al automatizar las acciones del usuario es posible garantizar que se cumpla los requisitos y además es posible revisar si se "rompe" alguna funcionalidad (regresión).  

2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

Si, se encuentran definidos dentro Si, se encuentran definidos dentro de la carpeta components, los archivos de test son aquellos que poseen .test en el nombre del archivo 

3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?

Debería agregar en la sección command de movies api el comando go test. Quedaría de la siguiente manera:

``` command: /movies-api -b ${BIND_IP} -p ${BIND_PORT} && go test
