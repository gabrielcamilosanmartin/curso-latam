def filter(diccionario, filtro):
	diccionario_nuevo = {}
	for clave, valor in diccionario.items():
		if (valor > filtro):
			diccionario_nuevo[clave] = valor
	return diccionario_nuevo
