cartelera = [# (mes, pais, nombre_pelicula, annio_filmacion, [sala1, sala2, ...])
            ('julio'  , 'FRANCIA' , 'Melo'               , 1986, ['sala3', 'sala1']),
            ('enero'  , 'CHILE'   , 'Gloria'             , 2013, ['sala1', 'sala2']),
            ('marzo'  , 'ALEMANIA', 'Tiempo de Canibales', 2014, ['sala1', 'sala2']),
            ('marzo'  , 'ALEMANIA', 'Soul Kitchen'       , 2009, ['sala3', 'sala4']),
            ('febrero', 'FRANCIA' , 'El muelle'          , 1962, ['sala1', 'sala3']),
            ('febrero', 'FRANCIA' , 'La dama de honor'   , 2004, ['sala1', 'sala4']),
            ('abril'  , 'RUSIA'   , 'Padre del soldado'  , 1964, ['sala3', 'sala2', 'sala4']),
            ('mayo'   , 'MEXICO'  , 'Cumbres'            , 2013, ['sala3', 'sala2']),
            ('junio'  , 'BELGICA' , 'Rondo'              , 2012, ['sala4', 'sala2'])]

s = input()
dicc = {}
lis = []

for x in cartelera:
    if s in x[4]:
        dicc[x[0]] = []

for x in cartelera:
    if s in x[4]:
        dicc[x[0]].append(x[2])

print(dicc)