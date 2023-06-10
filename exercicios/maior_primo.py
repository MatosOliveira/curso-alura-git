def ePrimo(num):
    i = 1
    cont = 0

    if(num > 1):

        while(i <= num):
            if(num % i == 0):
                cont = cont + 1
            i = i + 1

        if (cont == 2):
            return "primo"
        else:
            return "não primo"

def maior_primo(num):
    i = 2
    numPrimo = 0

    while(i <= num):
        if (ePrimo(i) == "primo"):
            numPrimo = i
        i = i + 1
    return numPrimo
        
