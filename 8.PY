# Escribe un programa que solicite al usuario un número entero positivo y luego imprima los primeros n 
# números impares utilizando un bucle while

print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))

# Inicializar la variable i en 1 (primer número impar)
n = 1

# Bucle while para imprimir los primeros n números impares
while num > 0:
    # Imprimir el número impar actual
    print(n)
    # Decrementar num en 1
    num -= 1
    # Incrementar i en 2 (para obtener el siguiente número impar)
    n += 2
