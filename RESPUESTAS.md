Respuestas:
Robert Alexis Valenzuela Murillo

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

Tipos de Test con Selenium en la Pirámide:

Pruebas de Aceptación (End-to-End / E2E):
Los tests de Selenium generalmente se consideran pruebas de aceptación, ya que simulan la interacción completa del usuario con la aplicación.
Verifican que el sistema funcione según lo esperado desde el inicio hasta el final.

Pruebas de Regresión:
Dado que las pruebas de Selenium pueden abarcar varias funcionalidades y capas de la aplicación, a menudo se utilizan como pruebas de regresión para asegurar que los cambios recientes no hayan introducido problemas en áreas existentes de la aplicación.


2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

El front-end si posee test unitarios y estos se encuentran en:
 ./movies-front/src/components/AddDirector.test.js
 ./movies-front/src/components/AddMovie.test.js


3. Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?

Para probar test unitarios de GO, se debe crear un nuevo servicio en el archivo docker-compose.yml de la siguiente forma:

 movies-api-test:
    build:
      context: ./movies-api
      dockerfile: Dockerfile
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_SERVER=${POSTGRES_SERVER}
      - POSTGRES_PORT=${POSTGRES_PORT}
    command: go test ./... 
    depends_on:
      - postgres
    restart: no
	
Este servicio llamado movies-api-test, utiliza el mismo contexto de construcción y Dockerfile que el servicio principal movies-api. El comando go test ./... se encarga de ejecutar todos los tests en el directorio del proyecto.
Para este caso, correría el archivo "server_test.go" que se encuentra dentro del directorio.