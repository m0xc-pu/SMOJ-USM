pal = input()
vocal = "aeiou"
cont = 0

for x in pal:
    if x in vocal:
        cont += 1

print(cont)