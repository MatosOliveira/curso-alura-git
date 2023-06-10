def maximo(x, y, z):
    if((x >= y) and (x >= z)):
        return x
    else:
        if((x <= y) and (y >= z)):
            return y
        else:
            if ((x <= z) and (y <= z)):
                return z

def test_maximo():
    assert maximo(0,-1, 1) == 0
