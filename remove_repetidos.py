def remove_repetidos(lista):

   lista2 = []

   lista2.append(lista[0])
   
   for num in lista:
       if (num not in lista2):
           lista2.append(num)
   lista2.sort()

   return(lista2)

    
    
