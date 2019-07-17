def letra_i(n=5):
	result = ''
	for i in range(0,n):
		for j in range(0,n):
			if (i in [0,n-1]):
				result += '*'
			elif (j == (n//2)):
				result += '*'
			else:
				result += ' '
		if (i != n-1):
			result += '\n'
	return result
		

print(letra_i(8))