clientes = [('Don Ramon', 3500, (9, 4, 2014)),
            ('Miguel',    2785, (30, 10, 2014)), 
            ('Cesar',      100, (28, 5, 2015))]

nombre = input()
pago = int(input())
dia = int(input())
mes = int(input())
anno  = int(input())

posLista = -1
posCambio = 0

for x in clientes:
    posLista += 1
    # print(posLista,x)
    if nombre == x[0]:
        posCambio = posLista

        deuda = x[1]
        deuda -= pago

        if deuda == 0:
            del clientes[posCambio]
        else:
            del clientes[posCambio]
            clientes.insert(posCambio,(nombre,deuda,(dia,mes,anno)))

print(clientes)