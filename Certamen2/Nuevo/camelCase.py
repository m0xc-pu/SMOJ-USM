palabra = input()

mayus = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

cont = 1

for x in palabra:
    if x in mayus:
        cont += 1

print(cont)