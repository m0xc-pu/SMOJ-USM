entrada = input()
mover = int(input())

mover = mover % 26 # 

s = []

for x in entrada:
    s.append(ord(x))

# print(s)

strin = ""

for x in s:

    # ASCII, ASCII movido, Es mayuscula?
    # print(x, x+mover, (x >= 65 and x <= 90))

    if (x >= 97 and x <= 122): # Si la letra es minuscula

        # ASCII movido, se pasa del limite de las letras?
        # print(x+mover, x+mover > 122)

        if (x + mover > 122): # Si se pasa de los ASCII de letras

            # print(chr(x + mover - 26))
            strin += chr(x + mover - 26) # Agregar letra al string

        else:
            # print(chr(x+mover))
            strin += chr(x+mover)
        
    elif (x >= 65 and x <= 90): # Si la letra es mayuscula

        # ASCII movido, se pasa del limite de las letras?
        # print(x+mover, x+mover > 90)

        if (x + mover > 90): # Si se pasa de los ASCII de letras

            # print(chr(x + mover - 26))
            strin += chr(x + mover - 26)

        else:

            # print(chr(x+mover))
            strin += chr(x+mover)
        
    else: # Si es otro simbolo que no sea una letra
        strin += chr(x) # Agreega el simbolo sin modificar

print(strin)
