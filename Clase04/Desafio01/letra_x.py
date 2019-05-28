def letra_x(n=5):
	result = ''
	for i in range(0,n):
		for j in range(0,n):
			if (i == j or i+j == n-1):
				result += '*'
			else:
				result += ' '
		if (i != n-1):
			result += '\n'
	return result


print(letra_x(6))