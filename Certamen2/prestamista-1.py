clientes = [('Don Ramon', 3500, (9, 4, 2014)),
            ('Miguel',    2785, (30, 10, 2014)), 
            ('Cesar',      100, (28, 5, 2015))]

suma = 0
for x in clientes:
    # print(x[1])
    suma += x[1]

print(suma)