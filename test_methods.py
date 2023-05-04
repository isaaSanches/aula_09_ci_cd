import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    a = 2
    b = 5

    output = methods.soma(a, b)
    
    assert output == 7

def test_subtracao():
    a = 6
    b = 2

    output = methods.subtracao(a, b)
    
    assert output == 4
    
def test_divisao():
    a = 6
    b = 3

    output = methods.divisao(a, b)
    
    assert output == 2


def test_multiplicacao():
    a = 2
    b = 5

    output = methods.multiplicacao(a, b)
    
    assert output == 10

def test_potencia():
    b = 3

    output = methods.potencia( b)
    
    assert output == 9

