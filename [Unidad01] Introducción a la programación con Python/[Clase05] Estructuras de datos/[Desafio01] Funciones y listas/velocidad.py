from functools import reduce

def promedio(lista):
	return (reduce(lambda x, y: x+y, lista)) / len(lista)