from calculadora import sumar

def test_sumar_bien():
    assert sumar(2, 3) == 5

def test_sumar_mal():
    # Esta prueba fallará si descomentamos la línea de abajo o si el código está mal
    assert sumar(1, 1) == 2