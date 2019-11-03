estudiantes = [('Hildegard', ['MAT023', 'QUI010', 'INF155']),
               ('Bastian',   ['MAT226', 'MAT243']),
               ('Sebastian', ['IWI131', 'QUI010']),
               ('Cristian',  ['MAT021', 'FIS110', 'QUI010']),
               ('Belen',     ['MAT023', 'FIS110', 'INF239', 'EFI102'])]

curso = input()
lista = []
for x in estudiantes:
    # print(x[1], curso in x[1])
    if curso in x[1]:
        lista.append(x[0])

print(lista)