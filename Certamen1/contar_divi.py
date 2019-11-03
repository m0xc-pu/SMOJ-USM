a = int(input())
b = int(input())
k = int(input())
divisores = 0

while a <= b:
    print(a, a%k, a%k==0)
    if a % k == 0:
        divisores += 1
    a += 1

print(divisores)