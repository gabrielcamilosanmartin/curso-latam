from listas_uno import *
import velocidad

promedio = velocidad.promedio(list(map(lambda x: x[1], listas_uno)))

for lista_uno in listas_uno:
	if lista_uno[1] >  promedio:
		print(lista_uno)
