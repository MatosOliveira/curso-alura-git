def fatorial(n):
    fat = 1

    if(n < 0):
        fat = 0
        print("Numero negativo")
    else:
        if(n == 0):
            return fat
        else:
            while(n > 1):
                fat = fat * n
                n = n - 1  
    return fat


def num_binomial(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-10) == 0

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120

