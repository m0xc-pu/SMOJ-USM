a = int(input())
b = int(input())
sum = 0

def es_primo(num):
    cantMult = 0

    for x in range(1,num): # Contar los multiplos del numero, si las hay, aparte del 1, y exceptuando a si mismo
        if num % x == 0:
            cantMult += 1

    if cantMult == 1: # Si el numero solo posee un unico multiplo (1), entonces es primo
        return True
    else:
        return False

for x in range(a,b+1):
    if es_primo(x):
        sum += x

print(sum)