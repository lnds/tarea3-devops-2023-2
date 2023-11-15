# Respuestas
# Jaime Norambuena Sagredo

##Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).
Mayormente pertenecen a los tipos de regresión y aceptación.

##Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?
Si, tiene test unitarios, están definidos en movies-front/src/components y sin los archivos con extensión .test.js (AddDirector.test.js, AddMovie.test.js).

##Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?
No me funcionó, estuve probando agregar al command del servicio movies-api el "go test", por ejemplo así, pero no me funcionó: "command: /movies-api -b ${BIND_IP} -p ${BIND_PORT} && go test"

El archivo que contiene los test está en (en Python): tests/test_tarea3.py
Utilicé Python y Pytest, traté de poner algunos comentarios y dejar el código relativamente ordenado.