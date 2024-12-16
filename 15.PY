#Escribe un programa que solicite al usuario un número entero positivo y 
# uego imprima el promedio de todos los números desde 1 hasta ese número utilizando un bucle while.


print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))

suma = 0
# Inicializar la variable contador en 0
contador = 0
n = 1
#  while para calcular la suma de los números
while n <= num:
    suma += n
    contador += 1
    # Incrementar i en 1
    n += 1
promedio = suma / contador
print("El promedio de los números desde 1 hasta", num, "es:", promedio)