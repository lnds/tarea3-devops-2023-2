# Respuestas a Tarea 3

## Actividades

Se realiza la actividad descrita. 

## Preguntas

### 1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test corresponde (regresión, integración, aceptación, etc).

### Partiendo de las definiciones vistas en clases para la pirámide de testing: 
Calidad Funcional corresponde a:  
-Cómo el mundo exterior percibe nuestro trabajo, sin importar cómo lo hayamos construido, el producto tiene que hacer lo que se espera y lo tiene que hacer bien. Sin importar si hay problemas en la calidad o arquitectura del código.  
Calidad Estructural corresponde a:  
-Acá nos interesa cómo está construido el sistema, nos interesa conocer el “estado de salud de nuestra base de código”, como debe ser el código según su calidad estructural: entendible, mantenible, escalable, efectivo, eficiente, seguro, evita duplicidad, es mejorable, tiene demasiados cambios en poco tiempo, es difícil de leer, o hay mucha carga lógica en una pieza de código.  
Calidad de Proceso corresponde a:  
-Cómo el proceso es todo lo que hacemos día a día que puede afectar el valor percibido por nuestros usuarios o por nosotros mismos. Cómo nos comunicamos, codificamos, compartimos conocimiento y pedimos ayuda. Corresponden a temas de calidad proceso si las tareas tienen requisitos claros, si se tiene solo un sistema de tracking de incidencias, si el flujo es continuo y estructurado, si hay buena comunicación y si el proceso cuenta con ceremonias y artefactos claros y que aportan valor.  

### Se puede decir que Selenium claramente corresponde a un testeo de calidad funcional, porque analiza que el software haga lo que se pide y lo haga bien, no se preocupa por el código que hay detrás ni por el proceso que se ha realizado.  

### Los tipos de test son los siguientes: 
TEST DE ACEPTACIÓN: Verifica si el sistema cumple con los criterios de aceptación y si satisface los requisitos del cliente. Se centra en la funcionalidad general del sistema y su capacidad para cumplir con los objetivos previamente establecidos.  
TEST DE REGRESIÓN: Asegurar que las modificaciones en el código (nuevas características, correcciones de errores) no afecten negativamente a las funcionalidades existentes. Se ejecutan pruebas en áreas específicas del código que podrían haber sido afectadas por cambios recientes.  
TEST DE INTEGRACIÓN: Evaluar la interacción entre módulos o subsistemas para garantizar que funcionen de manera conjunta como un sistema completo. Se prueba la interfaz y la comunicación entre los diferentes componentes del sistema.  
TEST DE PERFORMANCE: Evaluar el rendimiento del sistema en términos de velocidad, escalabilidad y estabilidad bajo diferentes condiciones, como carga máxima o situaciones de estrés. Se busca identificar cuellos de botella, problemas de rendimiento y optimizar el sistema para garantizar un funcionamiento eficiente.  
TEST UNITARIO: Verificar el correcto funcionamiento de las unidades más pequeñas de código, como funciones o métodos individuales. Se prueba cada unidad de forma aislada para garantizar que produzca los resultados esperados y cumpla con los requisitos especificados.  

### Selenium corresponde a un test de integración, porque evaluá el funcionamiento de la aplicación como sistema completo, en la medida que es utilizado. Obteniendo resultados y incorporando entradas a través de la interfaz de la aplicación construida.  

Selenium no parece ser un test de aceptación, porque aunque podría permitir evaluar requerimientos de clientes, es esperable que estos ya estén resueltos, como por ejemplo poder agregar una película o director en nuestra aplicación.  

Más aya de para decir si el código integrado dejo de funcionar, no parece que selenium sea un test adecuado para decir si modificaciones en el código afectan la aplican, por lo que no parece ser de regresión.  

Selenium podría utilizarse para medir el performance de una aplicación, especialmente uno podría medir el tiempo que tarda en realizarse algunas sus acciones, pero no parece ese ser el objetivo de Selenium.  

Selenium no tiene un enfoque de test unitario, porque prueba las acciones realizadas en la prueba desde la interfaz, probando el funcionamiento de la aplicación de manera integrada. Aunque con conocimiento especifico de la aplicación, uno podría probar módulos específicos con selenium, definiendo las pruebas con ese objetivo.   

### 2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?

### En scr/components hay 2 tests unitarios AddDirector.test.js y AddMovie.test.js, para testear unitariamente agregar director y película.  

### 3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?





