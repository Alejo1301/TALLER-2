#Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima todos los números entre 1 y ese número que sean múltiplos de 5 utilizando un bucle while

print("Perdir al usuario ingresar un nuemero entero positivo")
num = int(input("Ingrese un número entero positivo: "))

# Inicializar la variable n en 1
n = 1

# Ciclo while para imprimir los múltiplos de 5
while n <= num:
    if n % 5 == 0:  # Verificar si i es múltiplo de 5
        print(n)
    n += 1

