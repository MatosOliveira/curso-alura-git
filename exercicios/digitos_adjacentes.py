n= int(input("Digite um número inteiro: "))
cont = 0
digito1 = 0
digito2 = 0

while(n // 10 != 0):
    digito1 = (n % 10)
    digito2 = ((n % 100) // 10)

    if(digito1 == digito2):
        cont = cont + 1
    n = (n // 10)

if(cont >= 1):
    print("sim")
else: 
    print("não")

