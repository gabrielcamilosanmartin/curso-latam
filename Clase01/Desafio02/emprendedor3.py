import math
import sys

precio_venta = int(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = int(sys.argv[3])

if len(sys.argv) == 5:
	utilidad_ano_anterior = int(sys.argv[4])
else:
	utilidad_ano_anterior = 1000

utilidad = (precio_venta * usuarios) - gastos
if (utilidad > 0):
	utilidad *= .65
utilidad += utilidad_ano_anterior
print("%.3f" % utilidad) 




