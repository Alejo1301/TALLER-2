#Escribe un programa que solicite al usuario dos números enteros positivos y 
# luego imprima la tabla de multiplicar del primer número hasta el segundo número
#  utilizando un bucle while.

print("Pedir al usuario que ingrese dos números enteros positivos")
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))

# Asegurarse de que num1 sea menor o igual a num2
if num1 > num2:
    num1, num2 = num2, num1

n = 1
# Bucle while para imprimir la tabla de multiplicar
while n <= 10:
    # Imprimir la tabla de multiplicar para cada número entre num1 y num2
    m = num1
    while m <= num2:
        # Imprimir el resultado de la multiplicación
        print(f"{m} x {n} = {m * n}")
        # Incrementar j en 1
        m += 1
    # Imprimir una línea en blanco para separar las tablas
    print()
    # Incrementar i en 1
    n += 1
