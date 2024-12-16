#Escribe un programa que solicite al usuario un número entero positivo y 
# luego imprima todos los números primos menores o iguales a ese número utilizando un bucle while.

print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))

n = 2

while n <= num:
    # Inicializar la variable es_primo en True
    es_primo = True
    # Ciclo while para verificar si n es primo
    m = 2
    while m < n:
        if n % m == 0:
            es_primo = False
            break
        m += 1

    # Imprimir n si es primo
    if es_primo:
        print(m)
    n+= 1