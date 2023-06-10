def maior_elemento(lista):
    lista2 = []
    lista2.append(lista[0])

    for i in lista:
        if(i >= lista2[0]):
            lista2[0] = i
    
    return lista2[0]
