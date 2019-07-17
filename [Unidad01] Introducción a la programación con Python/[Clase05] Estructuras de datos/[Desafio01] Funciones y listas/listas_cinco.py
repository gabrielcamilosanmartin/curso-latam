from listas_uno import *
import velocidad

promedio = velocidad.promedio(list(map(lambda x: x[1], listas_uno)))

print (list(map(lambda x: x[1] ,list(filter(lambda x: x[1] > promedio, listas_uno)))))
