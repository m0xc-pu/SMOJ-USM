msj = input()
msj = msj.lower()
p = 0

char = "abcdefghijklmnopqrstuvwxyz"
numb = "1234567890"
esp = " "


for x in msj:
    #print(x)
    if x in char:
        #print("car")
        p += 10
    elif x in numb:
        #print("num")
        p += 20
    elif x in esp:
        #print("espacio")
        p += 0
    else:
        #print("especial")
        p += 30

print("$"+ str(p))