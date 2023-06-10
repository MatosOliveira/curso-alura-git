numero = int(input("Digite um número inteiro: "))

digito1 = int(numero % 100)
digito2 = int(digito1 / 10) 

print("O dígito das dezenas é", digito2)
