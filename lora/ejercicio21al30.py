# Sección 3: Operadores Lógicos

# 21. ¿Puede votar?
edad = 19
tiene_documento = True
puede_votar = edad >= 18 and tiene_documento
print("21. ¿Puede votar?:", puede_votar)

# 22. Control de acceso lógico
tiene_pase_vip = False
paga_entrada = True
esta_ebrio = False
puede_entrar = tiene_pase_vip or (paga_entrada and not esta_ebrio)
print("22. Control de acceso lógico:", puede_entrar)

# 23. Validación XOR
cond1 = True
cond2 = False
xor_valido = cond1 != cond2
print("23. Validación XOR:", xor_valido)

# 24. Validación compuesta múltiple
n = 6
valido = n > 0 and (n % 2 == 0 or n % 3 == 0)
print("24. Validación compuesta múltiple:", valido)

# 25. Condición contradictoria
x = 7
contradiccion = x > 5 and x < 1
print("25. Condición contradictoria:", contradiccion)

# 26. Negación lógica
x = 5
condicion_original = x <= 10
condicion_equivalente = not (x > 10)
print("26. Negación lógica:", condicion_equivalente)

# 27. Aprobación de estudiante
nota = 3.5
asistencia = 85
aprueba = nota >= 3.0 and asistencia >= 80
print("27. Aprobación de estudiante:", aprueba)

# 28. Simulación de alarma
temperatura = 39
humedad = 85
alarma = (temperatura < 0 or temperatura > 38) and humedad > 80
print("28. Simulación de alarma:", alarma)

# 29. Contraseña segura
contraseña = "abc123def"
longitud_valida = len(contraseña) > 8
contiene_numero = any(char.isdigit() for char in contraseña)
segura = longitud_valida and contiene_numero
print("29. Contraseña segura:", segura)

# 30. Doble negación lógica
tiene_acceso = False
expresion = not (not tiene_acceso)
