def suma(a, b):
    """
    Realiza la suma de dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        float: El resultado de la suma.
    """
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def resta(a, b):
    """
    Realiza la resta de dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        float: El resultado de la resta.
    """
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def producto(a, b):
    """
    Realiza el producto de dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        float: El resultado del producto.
    """
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")

def division(a, b):
    """
    Realiza la división de dos números.

    Args:
        a (float): El dividendo.
        b (float): El divisor.

    Returns:
        float: El resultado de la división.
    """
    try:
        if b == 0:
            raise ZeroDivisionError("No es posible dividir entre cero.")
        resultado = a / b
        return resultado
    except (ZeroDivisionError, TypeError) as e:
        print("Error:", e)