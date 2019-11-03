def seguro(entr):
    if len(entr) >= 6:
        num   = "1234567890"
        minus = "abcdefghijklmnopqrstuvwxyz"
        mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cont_num = 0
        cont_min = 0
        cont_may = 0
        for x in entr:
            if x in num:
                cont_num += 1
            elif x in minus:
                cont_min += 1
            elif x in mayus:
                cont_may += 1
        if cont_num > 0 and cont_min > 0 and cont_may > 0:
            return True
        else:
            return False
    else:
        return False

cant = int(input("Ingrese numero de contrasennas a revisar: "))
seg = 0
nseg = 0

for x in range(cant):
    contr = input("Ingrese contrasenna: ")
    if seguro(contr):
        seg += 1
    else:
        nseg += 1

print("******************")
print("Numero de contrasennas seguras / No-seguras:",seg,"/",nseg)