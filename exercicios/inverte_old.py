def inverte():
    lista = lista_num()

    for i in lista:
        print(i)

def lista_num():
    
    lista = []
    lista2 = []
    num = ""

    while (num != 0):
        num = int(input("Digite um número inteiro: "))
        lista.append(num)
    
    i = len(lista)

    while (i > 0):
        if(lista[i - 1] == 0):
            i = i - 1
            lista2.append(lista[i - 1])
        else:
            lista2.append(lista[i - 1])
        i = i - 1

    return lista2



