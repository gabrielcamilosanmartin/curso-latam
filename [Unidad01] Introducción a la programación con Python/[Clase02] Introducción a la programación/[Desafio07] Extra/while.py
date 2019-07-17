import time
contador = 0
while True:
	velocidad = input('ingrese velocidad: ')
	time.sleep(1)
	if float(velocidad) > 60:
		contador += 1
		print ('infraccion')
		if contador >=3:
			print ('licencia suspendida')
			break
