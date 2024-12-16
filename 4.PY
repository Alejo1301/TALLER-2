
#Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima si el número es un número de Armstrong utilizando un bucle while.


print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))

# Inicializar la variable suma en 0
suma = 0
# Inicializar la variable i en 1
n = 1
# Inicializar la variable longitud en 0
longitud = 0
# Ciclo while para calcular la longitud del número
while n <= num:
    if n == num:
        longitud += 1
        break
    longitud += 1
    n *= 10

# Reiniciar la variable n en 1
n = 1
# Ciclo while para calcular la suma de los dígitos elevados a la longitud
while n <= num:
    digito = num % 10
    suma += digito ** longitud
    num //= 10
    n += 1

# Imprimir el resultado
if suma == n - 1:
    print("El número es un número de Armstrong")
else:
    print("El número no es un número de Armstrong")