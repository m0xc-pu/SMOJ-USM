grupo = {
    'rick': (160, 19), 'daryl': (140, 15), 'michonne': (85, 8), 'glenn': (75, 0),
    'maggie': (65, 8), 'carl': (67, 2), 'tyreese': (40, 1), 'carol': (20, 4),
}

total_w = 0
total_h = 0

for x in grupo:
    #print(grupo[x])
    total_w += grupo[x][0]
    total_h += grupo[x][1]

dicc = {}

for x in grupo:
    w = grupo[x][0]
    h = grupo[x][1]
    puntos = round((w/total_w) + 2 * (h/total_h),2)
    #print(puntos)
    
    dicc[x] = puntos

#print(dicc)

lis1 = []
nombr = []

for x in dicc:
    #print(dicc[x])
    lis1.append((dicc[x],x))

lis1.sort()
lis1.reverse()
#print(lis1)

for x in lis1:
    #print(x[1])
    nombr.append(x[1])

print(nombr)