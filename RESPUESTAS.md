# Respuestas

## Nombre Alumno: Sebastián Urbano

### 1.- Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

Los test con Selenium, son los test de interfaz de usuario, por lo que se considerarían de regresión, ya que son pruebas automatizadas para las funcionalidades de la aplicación, de manera que ante nuevos cambios, se corren los test de regresión, de manera que no se tenga errores con respecto a las funcionalidades anteriores.

### 2.- Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

El front si cuenta con test-unitarios o unit-test, los cuales se encuentran dentro de la carpeta de componentes, de manera que se analiza cada uno de los componentes, ejecutándose con jest, la librería de test.

### Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?

Para ejecutar los test unitarios, se deben agregar al command que se tiene en la ejecución de docker de movies-api, de manera que se agregue el comando go test