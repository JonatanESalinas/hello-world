

def suma(num1, num2, modo):
	if modo == 1:
		return (num1 + num2)
	else:
		return (num1 * num2)

if __name__ == '__main__':
	print("Estoy usando GitHub")
	print("Suma: " + str(suma(4,8,1)))
	print("Multiplicacion: " + str(suma(4,8,2)))
