<!-- He creado una calculadora con funciones basicas de sumar, restrar, multiplicar y dividir, que no admita dividir por cero y que no admita decimales. -->


def calculadora(): <!-- Esta es la funcion principal -->
    try: <!-- nos pide que intentemos esa funciona con diferentes variables y con la operación que queramos hacer -->
        num1 = int(input("Ingresa el primer número entero positivo: "))
        <!-- Aquí vienen las condiciones, el primero es la funcion de la suma de las 2 variables enunciadas antes. Aparece indicado que solo amdite númeos positivos, no 0 ni decimales. Luego viene la resta, la multiplicación y la división. También aparece como última condición que no se puede dividir por 0 -->
            
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

calculadora()


        