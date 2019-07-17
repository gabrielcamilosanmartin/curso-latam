def letra_o(n=5):
	result = ''
	for i in range(0,n):
		for j in range(0,n):
			if (j in [0,n-1] or i in [0,n-1]):
				result += '*'
			else:
				result += ' '
		if (i != n-1):
			result += '\n'
	return result

print(letra_o(5))