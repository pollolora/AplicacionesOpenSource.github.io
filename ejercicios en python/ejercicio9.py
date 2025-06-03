print("Ejercicio 9: Verificar múltiplo")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if b == 0:
    print("No se puede dividir entre cero.")
elif a % b == 0:
    print(f"{a} es múltiplo de {b}.")
else:
    print(f"{a} no es múltiplo de {b}.")
