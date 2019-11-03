entr  = input()
num   = "1234567890"
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if len(entr) >= 6:
    cont_num = 0
    cont_min = 0
    cont_may = 0
    for x in entr:
        if x in num:
            # print(x,"num")
            cont_num += 1
        elif x in minus:
            # print(x,"min")
            cont_min += 1
        elif x in mayus:
            # print(x,"may")
            cont_may += 1

    # print(cont_num,cont_min,cont_may)
    if cont_num > 0 and cont_min > 0 and cont_may > 0:
        print("T")
    else:
        print("F")
else:
    print("F")