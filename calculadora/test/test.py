from calculadora import operacion


def test():
    print("Test suma:", operacion(5, 3, "+") == 8)
    print("Test resta:", operacion(10, 4, "-") == 6)
    print("Test multiplicación:", operacion(6, 7, "*") == 42)
    print("Test división:", operacion(9, 2, "/") == 4)
    print("Test división por cero:", operacion(5, 0, "/") == "Error: No se puede dividir entre 0.")
    print("Test número negativo:", operacion(-5, 3, "+") == "Error: Solo se permiten números enteros positivos.")
    print("Test operacion inválido:", operacion(5, 3, "%") == "Error: operacion no válido.")


test()