numero = input()
digitos = len(numero)

suma = 0
for x in numero:
    suma += int(x)**digitos

if int(numero) == suma:
    print("Es de Armstrong")
else:
    print("No es de Armstrong")