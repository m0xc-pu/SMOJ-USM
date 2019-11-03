dic_ruta = {1: 3,
            2: 1,
            3: 2,
            4: 5,
            5: 2,
            6: 5,
            7: 6,
            8: 9,
            9: 3}

inicio = int(input())
final  = int(input())
actual = inicio
lista_rec = []

while actual != final:
    # print(dic_ruta[actual])
    lista_rec.append(dic_ruta[actual])
    actual = dic_ruta[actual]
    # print(dic_ruta[actual])
    # print()

print(lista_rec)