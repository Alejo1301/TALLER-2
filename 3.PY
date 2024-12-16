# Escribe un programa que solicite al usuario un número entero positivo 
# y luego calcule la suma de todos los números divisibles por 3 desde 1 hasta ese número
#  utilizando un bucle while

# Pedir al usuario que ingrese un número entero positivo
num = int(input("Ingrese un número entero positivo: "))


suma = 0
n = 1
# Ciclo while para calcular la suma de los números divisibles por 3
while n <= num:
    if n % 3 == 0:  # Verificar si i es divisible por 3
        suma += n  
    n += 1  
print(f"La suma de los números divisibles por 3 desde 1 hasta", num, "es:", suma)

