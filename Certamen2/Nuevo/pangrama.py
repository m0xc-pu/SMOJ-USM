texto = input()
texto = texto.lower()

minus = list("abcdefghijklmnopqrstuvwxyz")
letras = []

#print(texto)

for x in texto:
    if x != " " and x != "." and x != ",":
        if x not in letras:
            letras.append(x)

letras.sort()
# print(letras)
# print(letras == minus)

if letras == minus:
    print("PANGRAMA")
else:
    print("NO PANGRAMA")