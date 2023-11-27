Notas
Los test se encuentran en la carpeta TEST, se encuentran en python.
Marisleydis Socas Alvez- Equipo 3


## Preguntas

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).
Dentro de la pirámide de testing, los test de Selenium se ubican en la parte superior de la priramide de testing, ya que se enfoca en la Calidad Funcional, las pruebas que se ejecutan con Selenium cubren las pruebas de regresión y pueden usarse también para las pruebas de Aceptación.

2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

SI, el front-end si posee test unitarios, pero para agregarkis se debe realizar lo siguiente: en el dockerfile, se integra la linea
CMD ["npm", "test"] en docker-compose tests: build: context: . dockerfile: Dockerfile command: npm test depends_on: - app los test unitarios por defecto del proyecto se encuentran en: movies-front src components *.test.js los terminados en .test.js

3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?
En este caso se debe agregar un servicio nuevo tests: build: context: go test ./ dockerfile: Dockerfile command: npm test depends_on: - app

Evidencia
![Alt text](evidencia_tarea3.png)