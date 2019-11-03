msg = input()
msg = msg.lower()

sos = list("sos")

c = 0

for x in msg:
    if x not in sos:
        #print(x, "aaaa")
        c += 1

print(c)