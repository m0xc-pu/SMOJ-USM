a = float(input())
b = float(input())
c = float(input())

if a > c: # El lado mayor es la hipotenusa
    if a > b:
        hip  = a
        cat1 = b
        cat2 = c
    else:
        hip  = b
        cat1 = a
        cat2 = c
else:
    if c > b:
        hip  = c
        cat1 = a
        cat2 = b
    else:
        hip  = b
        cat1 = a
        cat2 = c

if hip**2 == cat1**2 + cat2**2:
    rect = True
else:
    rect = False

if a+b > c and b+c > a and c+a > b: # Si es un triangulo valido
    if a==b==c:
        print("Triangulo equilatero")
    elif a==b or b==c or c==a:
        if rect:
            print("Triangulo isosceles rectangulo")
        else:
            print("Triangulo isosceles")
    else:
        if rect:
            print("Triangulo escaleno rectangulo")
        else:
            print("Triangulo escaleno")
else:
    print("No es triangulo")