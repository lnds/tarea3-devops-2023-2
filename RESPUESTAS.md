## JULIO SOTO SÁNCHEZ

## Respuestas

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

 Dentro de la piramide de Testing los test con Selenium se encuentran en la calidad funcional. Estos test corresponden al tipo de Test de Aceptación e Integración.

2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

El front-end si posee 2 Test unitarios identificados con los siguientes archivos:

    - AddDirector.test.js
    - AddMovie.test.js

Los archivos se encuentran en la carpeta movies-front/src/components

3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?

En el archivo docker-compose.yml debemos agregar el comando "&& go test" en la sección de command, según como se muestra a continuación:

```
movies-api:
    build:
      context: ./movies-api/
      dockerfile: Dockerfile
    ports:
      - ${BIND_PORT}:${BIND_PORT}
    environment:
      - BIND_IP
      - BIND_PORT
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
      - POSTGRES_SERVER
      - POSTGRES_PORT
    command:
      [
        "/movies-api",
        "-b",
        "${BIND_IP}",
        "-p",
        "${BIND_PORT}",
        "&&",
        "go test"
      ]
    depends_on:
      - postgres
```