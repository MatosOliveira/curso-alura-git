numero = int(input("Digite um número: "))

div3 = ((numero % 3) == 0)
div5 = ((numero % 5) == 0)

if(div3 == True) and (div5 == False):
	print("O Número", numero, "é divísivel por 3, mas não é por 5")
else:
        if(div3 == False) and (div5 == True):
                print("O Número", numero, "é divísivel por 5, mas não é por 3")
        else:
                if(div3 == True) and (div5 == True):
                        print("O Número", numero, "é divísivel por 3 e 5")
                else:
                        print("O Número", numero, "não é divísivel por 3 e por 5")
