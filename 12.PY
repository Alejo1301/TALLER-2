#Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima todos los números entre 1 y ese número que sean múltiplos de 7 utilizando un bucle while

print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))

n = 1

# Bucle while para imprimir los múltiplos de 7
while n <= num:
    # Verificar si n es múltiplo de 7
    if n % 7 == 0:
        # Imprimir i si es múltiplo de 7
        print(n)
    
    n += 1