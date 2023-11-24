Nombre alumno: Claudio Alejandro Galleguillos Perez

Pruebas Selenium
Se incorpora carpeta pruebatest, que incorpora proyecto maven para ejecuion de pruebas con el script de selenium (solo funciona con firefox)

Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

Respuesta: de aceptación e integración, las pruebas son al flujo de la aplicacion realizando acciones reales sobre el aplicativo, verificando el correcto funcionamiento.
Integración, ya que puede que se prueben funcinaliades que tengan dependencias unas de otras.

Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

Respuesta: Si, en los archivos, AddDirector.test.js y AddMovie.test.js

Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?

la linea 39 debe quedar como sigue.

movies-api:
    build:
      context: ./movies-api/
      target: build-release-stage
      dockerfile: Dockerfile
    environment:
      - BIND_IP=${BIND_IP}
      - BIND_PORT=${BIND_PORT}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_SERVER=${POSTGRES_SERVER}
      - POSTGRES_PORT=${POSTGRES_PORT}
    depends_on:
      - postgres  
    restart: always
    ports:
      - ${BIND_PORT}:${BIND_PORT}
    expose:
      - ${BIND_PORT}
    command: go test  ### para ejecutar test

Nombre alumno: Claudio Alejandro Galleguillos Perez