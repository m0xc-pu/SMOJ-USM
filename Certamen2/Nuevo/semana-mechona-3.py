def cantVocal(texto):
    vocal = "aeiouAEIOU"
    cont = 0
    for x in texto:
        if x in vocal:
            cont += 1
    return cont

meta = int(input())

al1 = 0
al2 = 0
al3 = 0

flag = True

while flag:
    mayor = 0

    punt1 = cantVocal(input())
    punt2 = cantVocal(input())
    punt3 = cantVocal(input())
    mayor = max(punt1,punt2,punt3)

    if mayor == punt1:
        al1 += 1
    elif mayor == punt2:
        al2 += 1
    elif mayor == punt3:
        al3 += 1

    # print(meta,al1,al2,al3)

    if al1 == meta:
        print("1")
        flag = False
    elif al2 == meta:
        print("2")
        flag = False
    elif al3 == meta:
        print("3")
        flag = False