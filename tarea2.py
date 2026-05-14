def modulo (a,b):
    """Funcion de modulo que recibe 2 parametros y retorna el modulo, pero si alguno de los parametros es mayor o igual a 100, retorna un mensaje de error

    Args:
        a (numero): primer parametro
        b (numero): segundo parametro

    Returns:
        numero: resultado del modulo de a y b
    >>> modulo(10, 3)    
    1
    >>> modulo(150, 3)
    'Error: Los valores son demasiado grandes'
    """
    if (a >=100 or b >= 100):   
        return "Error: Los valores son demasiado grandes"; 
    return a % b;


def enesima (a,b):
    """Funcion de raiz enesima que recibe 2 parametros y retorna la raiz enesima, 
    pero si alguno de los parametros es mayor o igual a 10 o menor a 0, retorna un mensaje de error

    Args:
        a (numero): primer parametro
        b (numero): segundo parametro

    Returns:
        numero: resultado de la raiz enesima de a y b
    >>> enesima(9, 2)
    3.0
    >>> enesima(4, 2)
    2.0
    >>> enesima(-5, 3)
    'Error: Los valores están fuera del rango permitido'
    """

    
    if(a>=0 and a<=10 and b>=0 and b <=10):
        return a**(1/b);
    else:
        return 'Error: Los valores están fuera del rango permitido'


# 
def valor_absoluto(a: float):
    """Valor absoluto de un número real.

    Args:
        a (float): numero real

    Returns:
        float: valor absoluto de a
        >>> valor_absoluto(-5.5)
        5.5
        >>> valor_absoluto(3.2)
        3.2
    """
    if a < 0:
        return a * -1
    else:
        return a
    