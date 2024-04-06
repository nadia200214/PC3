import operaciones

if __name__ == "__main__":
    # Ejemplos de uso de las funciones
    print("Suma:", operaciones.suma(5, 3))
    print("Resta:", operaciones.resta(5, 3))
    print("Producto:", operaciones.producto(5, 3))
    print("División:", operaciones.division(5, 3))
    print("División por cero:", operaciones.division(5, 0))
    print("Tipo de dato no válido:", operaciones.suma(5, "a"))