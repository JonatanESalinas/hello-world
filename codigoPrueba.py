

def my_calculation(num1, num2, modo):
	if modo == 1:
		return (num1 + num2)
	else:
		return (num1 * num2)

if __name__ == '__main__':
	print("Estoy usando GitHub")
	print("Suma: " + str(my_calculation(4,8,1)))
	print("Multiplicacion: " + str(my_calculation(4,8,2)))
