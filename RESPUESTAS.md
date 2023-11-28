# Javier Teillier

## Respuestas

1. Dentro de la pirámide de testing, ¿en que sector se ubican los tests con Selenium? ¿A cuál o cuáles tipos de test coresponde (regresión, integración, aceptación, etc).  
R: En la pirámide se ubica dentro de la calidad funcional. Corresponde a los test de regresión. Corresponde a los tipos de test de aceptación y regresión.

2. Indique si el front-end tiene tests unitarios. Si es así, ¿en cuáles archivos se encuentran definidos?  
R: Si tiene test unitarios definidos. Estos se encuentran en los archivos:
- AddDirector.test.js
- AddMovie.test.js

3. Para probar test unitarios en GO se usa el comando `go test`. ¿Cómo tendría que modificar el archivo `docker-compose` para correr los tests unitarios del backend?  
R: En movies-api modifiqué el atributo command de la siguiente manera:
```yaml
command: ["/movies-api", "-b", "${BIND_IP}", "-p", "${BIND_PORT}", "&&", "go", "test"]
```
Como se puede ver agregué los test como un segundo comando.