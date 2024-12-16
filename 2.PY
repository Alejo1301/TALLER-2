#Escribe un programa que solicite al usuario dos números enteros positivos
#  y luego imprima todos los números entre ellos (inclusive) utilizando un bucle while.

print("Pedir al usuario que ingrese dos números enteros positivos")
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))

# Asegurarse de que num1 sea menor o igual a num2
if num1 > num2:
    num1, num2 = num2, num1

# Inicializar la variable n en num1
n = num1

# Ciclo while para imprimir los números entre num1 y num2
while n <= num2:
    print(n)
    n += 1

