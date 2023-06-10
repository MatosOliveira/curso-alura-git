def fizzbuzz(numero):

    div3 = ((numero % 3) == 0)
    div5 = ((numero % 5) == 0)

    if(div3 == True) and (div5 == False):
        return "Fizz"
    else:
        if(div3 == False) and (div5 == True):
            return "Buzz"
        else:
            if((div3 == True) and (div5 == True)):
                return "FizzBuzz"
            else:
                return numero
