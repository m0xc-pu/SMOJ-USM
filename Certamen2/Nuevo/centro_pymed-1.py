abc    = "abcdefghijklmnopqrstuvwxyz"

# ---

palabra = input()

largo = len(palabra)
print("Largo:",largo)

menor = (999,999)

for x in range(largo):
    print(x,"=",palabra[x],"//",largo-1-x,"=",palabra[largo-1-x]) # palabra[largo-1-x]
    for i in range(len(abc)):
        print(palabra[largo-1-x],abc[i],largo-1-x,i,palabra[largo-1-x] == abc[i],"menor actual:",menor)
        if palabra[largo-1-x] == abc[i]:
            if i < menor[0]:
                menor = (i,largo-1-x)

print(menor[1])