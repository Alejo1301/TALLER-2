#Escribe un programa que solicite al usuario dos números enteros positivos y 
# luego imprima la suma de todos los números entre ellos (inclusive) utilizando un bucle while


print("Pedir al usuario que ingrese dos números enteros positivos")
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))

#  num1 debe ser  menor o igual a num2
if num1 > num2:
    num1, num2 = num2, num1

suma = 0
n = num1

while n <= num2:
    suma += n
    n += 1
print("La suma de los números entre", num1, "y", num2, "es:", suma)
