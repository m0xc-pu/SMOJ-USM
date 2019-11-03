def es_pythonia(palabra):
    # Hay?
    hp = False
    hy = False
    ht = False
    hh = False
    ho = False
    hn = False
    hi = False
    ha = False

    # En orden
    for x in palabra:
        #print(x)
        if x == "p" or hp:
            hp = True
            if x == "y" or hy:
                hy = True
                if x == "t" or ht:
                    ht = True
                    if x == "h" or hh:
                        hh = True
                        if x == "o" or ho:
                            ho = True
                            if x == "n" or hn:
                                hn = True
                                if x == "i" or hi:
                                    hi = True
                                    if x == "a" or ha:
                                        ha = True

    return(hp and hy and ht and hh and ho and hn and hi and ha)

num = int(input())
res = []

for x in range(num):
    pal = input()

    if es_pythonia(pal):
        res.append("SI")
    else:
        res.append("NO")

for x in res:
    print(x)