print("Ejercicio 6: Calculadora simple")
x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
if y != 0:
    print("División:", x / y)
else:
    print("No se puede dividir entre cero.")
