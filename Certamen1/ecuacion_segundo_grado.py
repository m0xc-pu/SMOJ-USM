from math import sqrt

a = float(input())
b = float(input())
c = float(input())
discr = (b*b - 4*a*c)

if a == 0:
    print("No es de segundo grado")
elif discr > 0:
    print((-b + sqrt(discr))/(2*a))
    print((-b - sqrt(discr))/(2*a))
elif discr == 0:
    print((-b + sqrt(discr))/(2*a))
elif discr < 0:
    print("Sin soluciones reales")