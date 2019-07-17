#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys



lista_eleccion = ['piedra', 'papel', 'tijera']


def main():
	eleccion = sys.argv[1].lower()
	if (not eleccion in lista_eleccion):
		print('Argumento inválido: Debe ser piedra, papel o tijera.')
		return

	eleccion_computador = random.choice(lista_eleccion)
	print ("Computador juega "+eleccion_computador) 

	if(eleccion == eleccion_computador):
		print('Empataste')
	elif ((eleccion == 'piedra' and eleccion_computador == 'tijera') or (eleccion == 'tijera' and eleccion_computador == 'papel') or (eleccion == 'papel' and eleccion_computador == 'piedra')):
		print("Ganaste")
	else:
		print("Perdiste")
	



if __name__ == '__main__': 
    main()