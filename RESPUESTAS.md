Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).
    
    Los test de selenium se ubican o se enfocan en la funcionalidad del sistema, dentro de los tipos de pruebas que podemos realizar en selenium, podemos generar pruebas automatizadas que nos muestren que las funcionalidades cumplan con los estandares de aceptacion, podemos realizar pruebas de regresion para verificar que los nuevos cambios no afecten el correcto funcionamiento, en resumen, selenium esta enfocado en las pruebas funcionales del sistema.

Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

    El front-end posee 2 test unitarios AddDirector.test.js y AddMovie.test.js los que estan definidos en la ruta: movies-front/src/components

Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?

    Para ejecutar los test, modificar la declaracion de command agregando && 'go Test' del servicio movies-app para cuando levantemos el contenedor, ejecute los test correspondientes.