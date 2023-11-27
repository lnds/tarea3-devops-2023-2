Nombre: Francisca Valdés Barrera

Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

Selenium generalmente se ubican en la capa de pruebas de aceptación en la pirámide de testing. Estos tests se centran en validar que la aplicación funciona correctamente desde la perspectiva del usuario final, simulando interacciones reales con la interfaz de usuario.
Sin embargo, también puede ser utilizado en algunos casos para pruebas de integración.

Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?


Si el fornt-end tiene tests unitarios en los siguientes archivos:
-movies-front/src/components/AddDirector.test.js
-movies-front/src/components/AddMovie.test.js

Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?

agregaria un servicio adicional


 backend-tests:
    depends_on:
      - movies-api
    build:
      context: ./movies-api
      dockerfile: Dockerfile 
    container_name: backend-tests
    command: go test  # Comando para ejecutar los tests unitarios
    