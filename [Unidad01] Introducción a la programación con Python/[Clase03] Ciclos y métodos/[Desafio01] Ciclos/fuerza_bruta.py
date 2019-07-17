password = input("Ingrese un número para comenzar la cuenta\n").lower()
abecedatio = 'abcdefghijklmnopqrstuvwxyz'
contador = 0
for i in range(0, len(password)):
	for j in range (0, len(abecedatio)):
		contador += 1
		if (abecedatio[j] == password[i]):
			break
print(str(contador) + " intentos")



