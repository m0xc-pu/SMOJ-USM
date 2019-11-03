jug = [('Garrett Reynolds', 89.33), ('Devon Smillie', 87.00),
       ('Simone Barraco'  , 68.66), ('Dakota Roche' , 73.33),
       ('Nathan Williams' , 54.66), ('Broc Raiford' , 84.33),
       ('Colin Varanyak'  , 40.66), ('Chad Kerley'  , 81.33),
       ('Bruno Hoffmann'  , 71.66), ('Ty Morrow'    , 77.33),
       ('Sean Ricany'     , 79.00), ('Dan Lacey'    , 36.00)]

i       = int(input())
j       = int(input())
puntmax = 0

for x in range(i,j+1):
    if jug[x][1] > puntmax:
        puntmax = jug[x][1]
        mejor   = jug[x][0]

print(mejor)