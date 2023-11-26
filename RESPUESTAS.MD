Tarea3-devops-2023-2 
Nombre: Gerardo Alonso
Archivo selenium ejecutable: GA_Tarea3_DevOps.py que debe ser invocado a través de main.py (ejecuta sobre navegador mozilla firefox)


##Pregunta 1:
Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

El testing forma parte del bloque "Aceptación e integración".
Aceptacion cuando se refiere a las pruebas aplicadas sobre la interfaz de usuario (front)
Integración cuando se prueba la funcionalidad de los componentes que se están tocando durante el test.


##Pregunta 2:
Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

Se pueden encontrar archivos con tests unitarios en los archivos:
1) ./movies-front/src/components/AddDirector.test.js
2) ./movies-front/src/components/AddMovie.test.js

Para hacer uso de ellos deben incorporarse como parte de los servicios a levantar.

##Pregunta 3:
Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?

La alternativa que sigue mejores prácticas indica la creación de un servicio adicional que llame a estos componentes de test.
Esto se puede lograr agregando, por ejemplo

movies-api-test:
   build:
      context: ./movies-api
      dockerfile: Dockerfile
      target: build-release-stage
    depends_on:
      - movies-api  
    command: go test ./... # Comando para ejecutar los tests unitarios
  
Una alternativa más directa es agregar en el command del servicio que se desea testear un "&& go test".