series = [('game of thrones',         'USA', 9.4, ['ficcion']),
          ('24',                      'USA', 8.4, ['accion', 'suspenso']),
          ('orange is the new black', 'USA', 8.5, ['comedia', 'drama']),
          ('sherlock',                'UK',  9.2, ['policial', 'drama', 'suspenso']),
          ('whitecollar',             'USA', 8.2, ['comedia', 'drama', 'suspenso']),
          ('heroes',                  'USA', 7.7, ['ficcion', 'accion']),
          ('mistfit',                 'UK',  8.4, ['accion', 'drama', 'ficcion'])]

pais = input()
lista = []

for x in series:
    if x[1] == pais:
        lista.append((x[0],x[2]))

print(lista)
