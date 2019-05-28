#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys



lista_eleccion = ['piedra', 'papel', 'tijera']


def main():
	notas_gringas=['F', 'D', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A']
	nota = sys.argv[1]

	if (not nota in notas_gringas):
		print('igrese nota correctamente')
		return
	else:
		if nota == 'A-':
			print (6.4)
		else:
			print(0.6*(notas_gringas.index(nota)+1)+1)



	



if __name__ == '__main__': 
    main()