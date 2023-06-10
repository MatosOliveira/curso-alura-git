def maximo(x, y):
    if(x <= y):
        return y
    else:
        return x

def test_maximo():
    assert maximo(0,-1) == 0
