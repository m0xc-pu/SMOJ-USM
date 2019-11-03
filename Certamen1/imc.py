est  = float(input())
peso = float(input())
imc  = round((peso)/(est*est), 2)

print(imc)

if imc < 18.5:
    print("Delgadez")
elif imc >= 18.5 and imc < 25.0:
    print("Normal")
elif imc >= 25.0:
    print("Sobrepeso")