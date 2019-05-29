ventas = {
	"Enero": 15000,
	"Febrero": 22000,
	"Marzo": 12000,
	"Abril": 17000,
	"Mayo": 81000,
	"Junio": 13000,
	"Julio": 21000,
	"Agosto": 41200,
	"Septiembre": 25000,
	"Octubre": 21500,
	"Noviembre": 91000,
	"Diciembre": 21000,
}

diccionario_agrupado = {}
for key, value in ventas.items():
	if not value in diccionario_agrupado:
		diccionario_agrupado[value] = 1
	else:
		diccionario_agrupado[value] += 1

print(diccionario_agrupado)
	

