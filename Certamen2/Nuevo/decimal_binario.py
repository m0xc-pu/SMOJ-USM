num = int(input())
bina = []

ult = num // 2
temp = ult
rest = num % 2
#print(ult, rest)
bina.append(rest)

while ult != 0:
    temp = ult // 2
    rest = ult % 2
    #print(temp, rest)
    ult = temp
    bina.append(rest)

#print(bina)
bina.reverse()
#print(bina)

while not (len(bina) % 4 == 0):
    bina.insert(0,0)
    #print("agrega")

#print(bina)

texto = ""
indi = 0
cont = 0

while indi < len(bina):
    texto += str(bina[indi])
    indi += 1
    cont += 1
    if cont == 4:
        texto += " "
        cont = 0

print(texto)