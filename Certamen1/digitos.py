num = input()
dig = len(num)
sum = 0

for x in range(dig):
    sum += int(num[x])

print(dig, sum)
