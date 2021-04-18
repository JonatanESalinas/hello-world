

def my_calculation(num1, num2, modo):
	if modo == 1:
		return (num1 + num2)
	else:
		return (num1 * num2)

if __name__ == '__main__':
	print("Estoy usando GitHub")
	number1 = int(input("Please give me a number:\n"))
	number2 = int(input("Please give me another number:\n"))
	print("Suma: " + str(my_calculation(number1,number2,1)))
	print("Multiplicacion: " + str(my_calculation(number1,number2,2)))
