def vogal(c):
    eVogal = False

    if(c == "a") or (c == "e") or (c == "i") or (c == "o") or (c == "u"):
        eVogal = True
    else:
        if(c == "A") or (c == "E") or (c == "I") or (c == "O") or (c == "U"):
            eVogal = True 
        else:
            eVogal = False
    return eVogal
        
      