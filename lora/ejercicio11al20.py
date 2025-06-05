# Sección 2: Operadores Relacionales

# 11. Verificación de rango
x = 55
en_rango = 10 <= x <= 100
print("11. Verificación de rango:", en_rango)

# 12. Comparación de strings (ignorar mayúsculas)
a = "Hola"
b = "hola"
iguales = a.lower() == b.lower()
print("12. Comparación de strings (ignorar mayúsculas):", iguales)

# 13. Igualdad entre tres variables
a = 7
b = 7
c = 7
mismos_valores = (a == b == c)
print("13. Igualdad entre tres variables:", mismos_valores)

# 14. Presencia en lista
lista = [3, 7, 12, 25, 30]
x = 12
presente = x in lista
print("14. Presencia en lista:", presente)

# 15. Divisibilidad por 3 y 5
n = 45
divisible = (n % 3 == 0) and (n % 5 == 0)
print("15. Divisibilidad por 3 y 5:", divisible)

# 16. Números en orden estricto
a = 5
b = 10
c = 20
orden_estricto = a < b < c
print("16. Números en orden estricto:", orden_estricto)

# 17. Comparación doble
x = 15
a = 10
b = 20
entre = a < x < b
print("17. Comparación doble:", entre)

# 18. Relación proporcional
a = 20
b = 10
doble = a == 2 * b
print("18. Relación proporcional:", doble)

# 19. Cambio de signo si negativo
x = -8
if x < 0:
    x = -x
print("19. Cambio de signo si negativo:", x)

# 20. Detección de tipo
x = 3.14  # Cambia este valor para probar otros tipos
if type(x) == int:
    tipo = "entero"
elif type(x) == float:
    tipo = "flotante"
elif type(x) == str:
    tipo = "cadena"
else:
    tipo = "otro"
print("20. Detección de tipo:", tipo)
