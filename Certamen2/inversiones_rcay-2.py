estafados = [('12.234.567-8', 2000000,   'pelados_furiosos',    (25, 5, 2015)),
             ('9.111.567-k',  5500000,   'multibank',           (1, 10, 2014)),
             ('14.987.007-1', 100000000, 'inversiones_seguras', (30, 11, 2016)),
             ('12.234.567-8', 10000000,  'multibank',           (2, 7, 2015)), 
             ('12.234.567-8', 2500000,   'multibank',           (18, 1, 2016))]

dicc = {}

for x in estafados:
    # print(x[2])
    dicc[x[2]] = 0

for x in estafados:
    dicc[x[2]] += x[1]

print(dicc)
