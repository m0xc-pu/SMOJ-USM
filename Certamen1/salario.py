n = float(input())

if n <= 500000.0:
    print(n*1.10)
elif n > 500000.0 and n <= 1000000.0:
    print(n*1.07)
elif n > 1000000.0:
    print(n*1.05)