num = int(input())

digit = 1
suma = 0
mult = 10
cont = 0
while digit != 0:
    digit = (num%mult)//(mult//10)
    suma += digit
    cont += 1
    mult *= 10

print(cont-1,suma)