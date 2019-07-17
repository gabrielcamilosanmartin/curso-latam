import math
import sys

precio_venta = int(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = int(sys.argv[3])

utilidad = (precio_venta * usuarios) - gastos
if (utilidad > 0):
	utilidad *= .65
print("%.3f" % utilidad)
