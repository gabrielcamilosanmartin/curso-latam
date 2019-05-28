n = int(input("Ingrese un número para comenzar la cuenta\n"))
resultado = 0
for i in range(0, n + 1, 2):
	resultado += i
print(resultado)
