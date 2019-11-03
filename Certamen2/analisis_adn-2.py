adn    = input()
contAT = 0
contCG = 0
valido = True

for x in adn:
    if x == "A" or x == "T":
        contAT += 1
    elif x == "C" or x == "G":
        contCG += 1
    elif x != " ":
        valido = False

if valido:
    if contCG > contAT:
        print("Es de especie vegetal")
    else:
        print("Es de especie animal")
else:
    print("No es valida")