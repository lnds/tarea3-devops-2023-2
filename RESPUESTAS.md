## Notas
    Los test se encuentran en la carpeta TEST, se encuentran en python.

## Preguntas
# Alumno Eugenio Bravo
1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).
    Los test de Selenium se ubican en la parte superior de la priramide de testing, ya que corresponde a una end-to-end o de usuario, en cuanto al tipo, es de aceptacion
2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?
    en este caso, SI posee test unitarios, pero para sumarlos se hace de la siguiente manera:
    en el dockerfile, se integra esta linea    
        CMD ["npm", "test"]
    en docker-compose
        tests:
            build:
                context: .
                dockerfile: Dockerfile
            command: npm test
            depends_on:
                - app
    los test unitarios por defecto del proyecto se encuentran en:
        movies-front
            src
                components
                    *.test.js
    los terminados en .test.js
3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?
    Se debe agregar un servicio nuevo
        tests:
            build:
                context: go test ./
                dockerfile: Dockerfile
            command: npm test
            depends_on:
                - app