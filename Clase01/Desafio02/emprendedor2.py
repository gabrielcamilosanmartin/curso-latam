import math
import sys

precio_venta = int(sys.argv[1])
usuarios_totales = int(sys.argv[2])
usuarios_premium = int(sys.argv[3])
usuarios_gratuitos = int(sys.argv[4])
gastos = int(sys.argv[5])

usuarios_normales = usuarios_totales - (usuarios_gratuitos + usuarios_premium)

utilidad = (2 * precio_venta * usuarios_premium) + (precio_venta * usuarios_normales) - gastos 

if (utilidad > 0):
	utilidad *= .65

print("%.3f" % utilidad)
