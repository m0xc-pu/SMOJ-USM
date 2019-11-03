o = int(input())

t = []

for f in range(o):
    fil = []
    for c in range(o):
        fil.append(int(input()))
    t.append(fil)

#print(t)

sumas = []

for fila in range(o):
    s = 0
    for colum in range(o):
        #print(fila, colum)
        s += t[fila][colum]
    #print(s , "suma")
    sumas.append(s)

for colum in range(o):
    s = 0
    for fila in range(o):
        #print(fila, colum)
        s += t[fila][colum]
    #print(s, "suma")
    sumas.append(s)

s = 0
for i in range(o):
    s += t[i][i]
sumas.append(s)

r = o-1
s = 0
for i in range(o):
    #print(r-i, i)
    s += t[r-i][i]
sumas.append(s)

#print(sumas)

ver = []

for x in sumas:
    if x not in ver:
        ver.append(x)

#print(ver)

if len(ver) == 1:
    print(ver[0])
else:
    print("NO")