## Preguntas

1. Dentro de la pirámide de testing, 
  ¿en que sector se ubican los tests con Selenium? 

   Se ubican en los test funcionales.

  ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

   Corresponde a los test de aceptacion.
   
2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

   Si tiene tests unitarios.
   En los archivos:
     - movies-front/src/components/AddDirector.test.js
     - movies-front/src/components/AddMovie.test.js

3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?
   
   cambiar 
         command:  ./movies-api -b ${BIND_IP} -p ${BIND_PORT}
   Por 
         entrypoint: "go test -v ./... && ./movies-api -b ${BIND_IP} -p ${BIND_PORT}"

   En el servicio movies-api
     

## FRANKLIN CRUCES - Tarea 3
