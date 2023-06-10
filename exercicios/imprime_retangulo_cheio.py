i = int(input("digite a largura: "))
j = int(input("digite a altura: "))

linha = 1

while linha <= j:
    coluna = 1
    while coluna <= i:
        print("#", end = "") 
        coluna = coluna + 1
    linha = linha + 1
    print()

