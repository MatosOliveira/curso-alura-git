def inverte(lista):
    print(inverte_lista(lista))

def inverte_lista(lista):
    
    lista2 = []

    for i in lista:
        if(i != 0):
            lista2.append(i)
    lista2.reverse()
    
    return(lista2) 



