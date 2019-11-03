cant = int(input())

lis1 = []

for x in range(cant):
    roca = input()
    mine_l = []
    for mine in roca:
        if mine not in mine_l:
            mine_l.append(mine)
    lis1.append(mine_l)

s = ''

for x in lis1:
    for i in x:
        s = s + i
    
cont = 0
abc = 'abcdefghijklmnopqrstuvwxyz'

for x in abc:
    # print(x, s.count(x))
    if s.count(x) == cant:
        cont += 1
        
print(cont)