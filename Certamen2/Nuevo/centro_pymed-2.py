abc    = "abcdefghijklmnopqrstuvwxyz"
string = input()
orden  = []

for x in abc:
    for i in string:
        if x == i:
            orden.append(i)

for x in orden:
    print(x,end="")