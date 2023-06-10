n = int(input("Digite um número inteiro: "))
soma = 0

while(n // 10 != 0):
    digito = (n % 10)
    soma = soma + digito
    n = (n // 10)

if(n < 10):
    soma = soma + n
print(soma)