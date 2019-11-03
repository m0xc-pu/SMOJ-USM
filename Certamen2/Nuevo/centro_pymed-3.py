def imprimir_orden(texto):
    abc   = "abcdefghijklmnopqrstuvwxyz"
    final = []

    for x in abc:
        for i in texto:
            if x == i:
                final.append(i)

    for x in final:
        print(x,end="")
    
    print()

cont = 1
ult  = 1
while ult != "0":
    ult = input("Ingrese informacion sanguinea " + str(cont) + ": ")
    if ult != "0":
        print("Informacion Ordenada: ",end="")
        imprimir_orden(ult)
        cont += 1
    else:
        cont -= 1
        print("Cadenas ordenadas: " + str(cont))