from listas_uno import *
import velocidad

promedio1 = velocidad.promedio(list(map(lambda x: x[1], listas_uno)))
promedio2 = velocidad.promedio(list(map(lambda x: x[2], listas_uno)))
promedio3 = velocidad.promedio(list(map(lambda x: x[4], listas_uno)))

print("Promedio: " + str(promedio1))
print("Promedio: " + str(promedio2))
print("Promedio: " + str(promedio3))