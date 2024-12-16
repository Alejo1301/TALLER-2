#Escribe un programa que solicite al usuario un número entero positivo y luego
#  imprima la suma de los primeros n números pares utilizando un bucle while


print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))

suma = 0
n = 2

while num > 0:
    # Sumar i a la suma
    suma += n
    num -= 1
    n += 2

print("La suma de los primeros", num+1, "números pares es:", suma)