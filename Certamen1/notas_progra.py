c1    = int(input())
c2    = int(input())
c3    = int(input())
lab   = int(input())
equip = int(input())
recup = int(input())

if recup >= 0: # Si rindio recuperativo, reemplaza menor certamen
    if c1 < c3:
        if c1 < c2: # c1 es el menor
            c1 = recup
        else: # c2 es el menor
            c2 = recup
    else:
        if c3 < c2: # c3 es el menor
            c3 = recup
        else: # c2 es menor
            c2 = recup
    
#print(c1,c2,c3)

notaInd = round(((c1+c2+c3)/3)*0.75+lab*0.25)

if notaInd < 55:
    notaFin = notaInd
elif notaInd >= 55:
    notaFin = round(((c1+c2+c3)/3)*0.60 + lab*0.20 + equip*0.20)

if notaFin < 55:
    print("Reprobado")
elif notaFin >= 55:
    print("Aprobado")

print(notaFin)