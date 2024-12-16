#Escribe un programa que solicite al usuario un número entero positivo 
# y luego imprima la suma de los cuadrados de todos los números desde 1 hasta ese número
#  utilizando un bucle while.

print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))

suma = 0
n = 1
while n <= num:
    # Calcular el cuadrado de n y sumarlo a la suma
    suma += n ** 2
   
    n += 1

print("La suma de los cuadrados de todos los números desde 1 hasta", num, "es:", suma)