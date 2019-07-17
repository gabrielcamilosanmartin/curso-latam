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

quarters = {}
count = 0
trimestre = 1
for key, values in ventas.items():
	if count % 3 == 0:
		q = "Q"+str(trimestre)
		quarters[q] = []
		trimestre += 1
	count += 1
	quarters[q].append(values) 
print(quarters)