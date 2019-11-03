# grupo = {
#     'rick': (160, 19), 'daryl': (140, 15), 'michonne': (85, 8), 'glenn': (75, 0),
#     'maggie': (65, 8), 'carl': (67, 2), 'tyreese': (40, 1), 'carol': (20, 4),
# }

suma_w = 0
suma_h = 0

for x in grupo:
    #print(grupo[x])
    suma_w += grupo[x][0]
    suma_h += grupo[x][1]

print((suma_w,suma_h))