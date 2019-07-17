#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

def main():
	ano = int(sys.argv[1])

	if (ano % 100 == 0): 
		if (ano % 400):
			print('no es bisiesto')
		else:
			print('es bisiesto')
	elif (ano % 4 == 0):
		print('es bisiesto')
	else:
		print('no es bisiesto')




if __name__ == '__main__': 
    main()