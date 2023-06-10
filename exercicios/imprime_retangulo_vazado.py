i = int(input("digite a largura: "))
j = int(input("digite a altura: "))

linha = 1

while linha <= j:
    coluna = 1
    while coluna <= i:
        if ((coluna == 1) or (coluna == i)) or ((linha == 1) or (linha == j)):
            print("#", end = "")
        else:
            if(linha > 1) and (linha < j):
                print(" ", end = "")
        coluna = coluna + 1
    linha = linha + 1
    print()
