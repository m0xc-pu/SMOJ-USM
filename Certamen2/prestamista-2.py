clientes = [('Don Ramon', 3500, (9, 4, 2014)),
            ('Miguel',    2785, (30, 10, 2014)), 
            ('Cesar',      100, (28, 5, 2015))]

anno = int(input())

nombreMay = ""
mayor = 0

for x in clientes:
    if anno in x[2]:
        # print(x[1])
        if x[1] > mayor:
            mayor = x[1]
            nombreMay = x[0]

print(nombreMay)