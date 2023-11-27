## Alumno: Erikson Fuenzalida

# Nota
Los test realizados se encuentran en la carpeta "test", ahi se encuentran los archivos .vb mas capturas de imagenes donde se ve las pruebas de Selenium y como quedaron visualmente en la web pestaña movies y directors.

## Preguntas

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

R.- Los test de Selenium se ubican en la parte alta de la piramide de testing, tanto para "Aceptación" ya que permite testear la integración en servicios end-to-end como tambien en "Regresión", para verificar algún cambio efectuado en el código no genere conflicto en su ejecución.

2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

R.- El front-end si posee test unitarios, y estos se encuentran definidos en:
    movies-front/src/components/AddDirector.test.js
    movies-front/src/components/AddMovie.test.js

3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?

R.- Para agregar los test unitarios en Go dentro del archivo docker-compose.yml tendriamos que modificar la siguiente linea a "command: go test" para que cuando se levante el docker ejecute el comando indicado.
Ejemplo de como quedaria:
    tests:
        build:
            context: ./movies-api
            dockerfile: Dockerfile
        command: go test
