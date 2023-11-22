# Alumno

Rodrigo Alejandro Navarro Martinez

## Respuestas de Preguntas

**1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).**

R. Los test realizados con Selenium se ubica en la `calidad funcional`, ya que están simulando las acciones de un usuario en la aplicación para asegurar que las funciones claves estén trabajando según lo esperado. Lo anterior corresponde al tipo de test `aceptación`, también podría considerarse de `integración`, ya que está interactuando con varias capas del sistema, como por ejemplo el backend y base de datos.


**2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?**

R. Si, en la ruta movies-front/src/component, cuenta con dos archivos de test unitarios: `AddMovie.test.js` y `AddDirector.test.js`

**3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?**

R. Para probar los test unitarios se debe realizar 2 cambios en el servicio `movies-api` del docker-compose:

1. Modificar el valor de `target` de la propiedad `build` a  `build-stage`. Esto es para que los tests se ejecuten antes del deploy.

2. En la propiedad `command` se debe modificar por `go test`. 

La configuración quedaría así:

```yaml:

movies-api:
    depends_on:
      - postgres
      - flyway
    restart: always
    build: 
      context: ./movies-api/
      target: build-stage
      dockerfile: Dockerfile
    container_name: movies-api
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_PORT=${POSTGRES_PORT}
      - POSTGRES_SERVER=${POSTGRES_SERVER}
      - BIND_IP=${BIND_IP}
      - BIND_PORT=${BIND_PORT}
    ports:
      - "${BIND_PORT}:${BIND_PORT}"
    command: go test 

```
