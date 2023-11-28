from selenium import webdriver 
from selenium.webdriver.common.by import By 

from Tarea3_Caso1_AgregarDirectores import *
from Tarea3_Caso2_Agregarunapeliculaacadaunodelosdirectores import *
from Tarea3_Caso3_AgregardospeliculasmasaldirectorCristopherNolan import *

Caso1 = Test1Agregardirectores()
Caso1.setup_method()
Caso1.test_1Agregardirectores()
Caso1.teardown_method
Caso2 = Test2Agregarunapeliculaacadaunodelosdirectores()
Caso2.setup_method()
Caso2.test_2Agregarunapeliculaacadaunodelosdirectores()
Caso2.teardown_method
Caso3 = Test3AgregardospeliculasmasaldirectorCristopherNolan()
Caso3.setup_method()
Caso3.test_3AgregardospeliculasmasaldirectorCristopherNolan()
Caso3.teardown_method