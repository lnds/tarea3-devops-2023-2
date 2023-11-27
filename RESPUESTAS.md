## Preguntas y respuestas

# Nombre de Alumno : JOSE SANTELICES K.

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).
2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?
3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?


R1: Selenium se encuentra en la capa fucional de la piramide, corresponde a Test de aceptación e integración, tamnien se pueden hacer test unitarios y de regresión

R2: Si existen los test unitarios:
    Para el front-end, dentro de la carpeta movies-front/src/components/ existen 2 archivos de pruebas unitarias, AddDirector.test.js y AddMovie.test.js

R3: Para correr los tests unitarios del backend?
Se debe agregar al YML el commando: `command: bash -c "cd /app && go get -d -v && go test --tags integration -v"` dentro de la sección `movies-api`.