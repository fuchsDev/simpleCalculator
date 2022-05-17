#functions
def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y


#menu
print("\n******************* Python Calculator *******************")
print("\nSelecione o numero da opção desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multriplicação")
print("4 - Divisão")


#collect input
opcDesejada = 0
while (opcDesejada < 1 or opcDesejada > 4):
    opcDesejada = int(input("\nDigite sua opção desejada (1/2/3/4): "))

else:
    num1 = float(input("Digite o Primeiro Numero: "))
    num2 = float(input("Digite o Segundo Numero: "))


#work input
if opcDesejada == 1:
	print("\n")
	print(num1, "+", num2, "=", add(num1, num2))
	print("\n")

elif opcDesejada == 2:
	print("\n")
	print(num1, "-", num2, "=", subtract(num1, num2))
	print("\n")

elif opcDesejada == 3:
	print("\n")
	print(num1, "*", num2, "=", multiply(num1, num2))
	print("\n")

elif opcDesejada == 4:
	print("\n")
	print(num1, "/", num2, "=", divide(num1, num2))
	print("\n")