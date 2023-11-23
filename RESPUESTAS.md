Nombre: Jimena Silva Navarrete


1.- Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).

Respuesta 1:

Los tests realizados con Selenium suelen ubicarse principalmente en dos áreas dentro de la pirámide de pruebas, dependiendo de su naturaleza y complejidad:

Tests de UI (Interfaz de Usuario) o Pruebas de extremo a extremo (E2E) - Calidad Funcional:
Estos tests se enfocan en simular la interacción de un usuario real con la aplicación a través de la interfaz de usuario. Aquí es donde Selenium generalmente se utiliza para automatizar navegadores y simular acciones como clics, ingreso de datos, selección de elementos, etc. Estos tests se encuentran en la parte superior de la pirámide de pruebas y pueden ser más lentos y frágiles debido a su dependencia de la UI. Pertenecen al nivel de pruebas de aceptación o pruebas E2E.

Tests de Integración con GUI:
Aunque Selenium es ampliamente utilizado para pruebas de UI, también puede ser parte de las pruebas de integración en las que se verifican interacciones entre componentes o módulos con una capa mínima de la interfaz de usuario. Estos tests podrían estar en el nivel intermedio de la pirámide y se utilizan para validar la integración de los diferentes componentes del sistema, aunque su enfoque no sea únicamente la interfaz de usuario.


2.-Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

Respuesta 2:

Si el fornt-end tiene tests unitarios en los siguientes archivos:
-movies-front/src/components/AddDirector.test.js
-movies-front/src/components/AddMovie.test.js



3.-Para probar test unitarios en GO se usa el comando go test. ¿Cómo tendría que modificar el archivo docker-compose para correr los tests unitarios del backend?


Respuesta 3:

se necesita realizar algunas modificaciones al archivo docker-compose.yml para configurar el entorno de ejecución de las pruebas, como el ejemplo que se muestra a continuación:


test:
    build:
      context: ./movies-api
      dockerfile: Dockerfile
    command: go test ./... # Comando para ejecutar los tests unitarios
    depends_on:
      - movies-api