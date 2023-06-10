num = int(input("Digite um número inteiro: "))
i = 1
cont = 0

if(num > 1):

    while(i <= num):
        if(num % i == 0):
            cont = cont + 1
        i = i + 1

    if (cont == 2):
        print("primo")
    else:
        print("não primo")

