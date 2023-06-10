numero = int(input("Digite um número: "))

div3 = ((numero % 3) == 0)
div5 = ((numero % 5) == 0)

if(div3 == True) and (div5 == False):
	print("FizzBuzz")
else:
	print(numero)
