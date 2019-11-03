a    = int(input())
b    = int(input())

while a != b:
    if a > b:
        t = a-b
        a = b
        b = t
    else:
        t = b-a
        a = b
        b = t

if a == b:
    print(a)