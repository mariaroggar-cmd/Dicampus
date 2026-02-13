def operacion():
    try:
        num1 = int(input("Ingresa el primer número entero positivo: "))
        if num1 < 0:
            print("Error: Solo se permiten números enteros positivos.")
            return

        num2 = int(input("Ingresa el segundo número entero positivo: "))
        if num2 < 0:
            print("Error: Solo se permiten números enteros positivos.")
            return

        operador = input("Ingresa la operación (+, -, *, /): ")

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                print("Error: No se puede dividir entre 0.")
                return
            resultado = num1 // num2
        else:
            print("Error: Operador no válido.")
            return

        print("Resultado:", resultado)

    except ValueError:
        print("Error: Solo se permiten números enteros.")

operacion()


