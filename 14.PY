#Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima la suma de los números de Fibonacci hasta ese número utilizando un bucle while

print("Pedir al usuario que ingrese un número entero positivo")
n = int(input("Ingrese un número entero positivo: "))

# Inicializar las variables a y b con los primeros dos números de Fibonacci
a = 0
b = 1

# Inicializar la variable suma en 0
suma = 0
# Bucle while para calcular la suma de los números de Fibonacci
while a <= n:
    # Sumar a a la suma
    suma += a
    # Calcular el siguiente número de Fibonacci
    a, b = b, a + b
print("La suma de los números de Fibonacci hasta", n, "es:", suma)


