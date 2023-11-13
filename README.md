# Tarea 3

Haz un fork de este repo.
Luego ejecuta las actividades descritas más abajo. Responde las preguntas en un archivo llamado `RESPUESTAS.md`.
Debes entregar tu tarea como un pull request que incluya el archivo `docker-compose.yml`, el script Selenium, y el archivo con respuestas.
Recuerda agregar tu nombre en el archivo de respuestas. 

## Actividades

- Configura un archivo docker-compose para ejecutar esta aplicación (usa archivo final de la tarea 2).
- Levanta la aplicación con `docker-compose up -d`
- Escribe un test en selenium en el lenguaje que te resulte más sencillo, también puedes usar Selenium IDE y exportar el resultado.
- El test que escribas debe implementar lo siguiente:
   
   - Caso 1: Agregar 2 directores
   - Caso 2: Agregar 1 película para cada uno de los directores.
   - Caso 3: Agregar 2 películas más al director Cristopher Nolan.
     

Nota: El script selenium *debe estar en algún lenguaje de programación*, no se aceptará la exportación del proyecto desde Selenium IDE.

## Preguntas

1. Dentro de la pirámide de testing, en que sector se ubican los tests con Selenium
2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?
3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?

## Pauta

- 1.0 puntos por completar el archivo `docker-compose.yml`.
- 3.0 puntos por agregar el test (1 punto por cada caso implementado).
- 0.5 puntos por la pregunta 1
- 0.5 puntos por la pregunta 2
- 1.0 punto por la pregunta 3



