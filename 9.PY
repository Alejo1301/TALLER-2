#Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima todos los números entre 1 y ese número en orden inverso utilizando un bucle 


print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))
n = num
#while para imprimir los números en orden inverso
while n >= 1:
    # Imprimir el número actual
    print(n)
    # Decrementar i en 1
    n-= 1