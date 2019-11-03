futbolistas = {1:  ('Valdes', 'arquero'),
               23: ('Umtiti', 'defensa'),
               3:  ('Pique', 'defensa'),
               2:  ('Semedo', 'defensa'),
               7:  ('Coutinho', 'centrocampista'),
               22: ('Vidal', 'centrocampista'),
               5:  ('Busquets', 'centrocampista'),
               9:  ('Suarez', 'delantero'),
               11: ('Dembele', 'delantero'),
               10: ('Messi', 'delantero')}

tipo = input()
lista = []

for x in futbolistas:
    # print(futbolistas[x],tipo,futbolistas[x][1])
    if tipo == futbolistas[x][1]:
        lista.append(futbolistas[x][0])

print(lista)