#Escribe un programa que solicite al usuario un número entero positivo y 
# luego calcule la cantidad de dígitos del número utilizando un bucle while.


print("Pedir al usuario que ingrese un número entero positivo")
num = int(input("Ingrese un número entero positivo: "))

# Inicializar la variable contador en 0
contador = 0
# Bucle while para calcular la cantidad de dígitos
while num > 0:
    # Incrementar el contador en 1
    contador += 1
    # Eliminar el último dígito del número
    num //= 10
print(f"La cantidad de dígitos del número es:", {contador})
