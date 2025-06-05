# 1. Intercambio sin variable auxiliar
a = 10
b = 20
a, b = b, a
print("1. Intercambio sin variable auxiliar:", a, b)

# 2. Suma de cuadrados
a = 5
b = 3
c = a**2 + b**2
print("2. Suma de cuadrados:", c)

# 3. Conversión de tipos
num = 42
num_str = str(num)
num_float = float(num_str)
num_int = int(num_float)
print("3. Conversión de tipos:", num_str, num_float, num_int)

# 4. Redondeo y formato
numero = 17.8567
redondeado = round(numero, 2)
resultado = "Resultado: " + str(redondeado)
print("4. Redondeo y formato:", resultado)

# 5. Concatenación de variables
nombre = "Juan"
edad = 25
mensaje = "Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años."
print("5. Concatenación de variables:", mensaje)

# 6. Cálculo de edad actual
anio_actual = 2025
anio_nacimiento = 2000
edad_actual = anio_actual - anio_nacimiento
print("6. Cálculo de edad actual:", edad_actual)

# 7. Cuenta regresiva con variables
print("7. Cuenta regresiva con variables:")
n = 10
while n >= 0:
    print(n)
    n -= 1

# 8. Valor absoluto sin usar abs()
x = -15
valor_absoluto = x if x >= 0 else -x
print("8. Valor absoluto sin usar abs():", valor_absoluto)

# 9. Incremento/decremento según paridad
n = 8
if n % 2 == 0:
    n += 1
else:
    n -= 1
print("9. Incremento/decremento según paridad:", n)

# 10. Máximo entre tres números
a = 12
b = 25
c = 18
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print("10. Máximo entre tres números:", mayor)
