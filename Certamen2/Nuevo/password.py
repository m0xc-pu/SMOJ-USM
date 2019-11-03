minus = "abcdefghijklmnopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
esp = "!@#$%^&*()-+"
num = "0123456789"

inp = input()

l = len(inp) # Longitud clave
f = 0 # Suponemos que no faltan caracteres
r = 0 # Suponemos que no faltan requisitos

# Cantidad de...
c_num = 0
c_minus = 0
c_mayus = 0
c_esp = 0

if not l >= 6: # Si la clave NO tiene al menos 6 caracteres
    f = abs(l - 6)

# Para cada letra de la clave...
for x in inp:
    if x in num:
        c_num += 1
    if x in minus:
        c_minus += 1
    if x in mayus:
        c_mayus += 1
    if x in esp:
        c_esp += 1

# Si no hay... agrega 1 a los requisitos
if c_num == 0:
    r += 1
if c_minus == 0:
    r += 1
if c_mayus == 0:
    r += 1
if c_esp == 0:
    r += 1

#print(c_num, c_minus, c_mayus, c_esp)
#print(f, r)

if f > r:
    print(f)
else:
    print(r)