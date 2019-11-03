estafados = [('12.234.567-8', 2000000,   'pelados_furiosos',    (25, 5, 2015)),
             ('9.111.567-k',  5500000,   'multibank',           (1, 10, 2014)),
             ('14.987.007-1', 100000000, 'inversiones_seguras', (30, 11, 2016)),
             ('12.234.567-8', 10000000,  'multibank',           (2, 7, 2015)), 
             ('12.234.567-8', 2500000,   'multibank',           (18, 1, 2016))]

rut = input()
ant = 0
lista = []

for x in estafados:
    # print(x[0], rut, rut == x[0])
    if rut == x[0]:
        # print(x[2])
        if ant != x[2]:
            lista.append(x[2])
            ant = x[2]

if lista == []:
    print("Rut no estafado")
else:
    print(lista)