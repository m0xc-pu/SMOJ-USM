tabla = [
	( 65 , 'A' ), ( 66 , 'B' ), ( 67 , 'C' ), ( 68 , 'D' ), ( 69 , 'E' ),
	( 70 , 'F' ), ( 71 , 'G' ), ( 72 , 'H' ), ( 73 , 'I' ), ( 74 , 'J' ),
	( 75 , 'K' ), ( 76 , 'L' ), ( 77 , 'M' ), ( 78 , 'N' ), ( 79 , 'O' ),
	( 80 , 'P' ), ( 81 , 'Q' ), ( 82 , 'R' ), ( 83 , 'S' ), ( 84 , 'T' ),
	( 85 , 'U' ), ( 86 , 'V' ), ( 87 , 'W' ), ( 88 , 'X' ), ( 89 , 'Y' ),
	( 90 , 'Z' )
        ]

#Creacion de lista y tuplas
mensaje = []
cantchar = int(input())
for x in range(cantchar):
    inicio = int(input())
    step = int(input())
    veces = int(input())
    mensaje.append((inicio,step,veces))
print(mensaje)
#[(42, 10, 4), (479, -100, 5), (70, 1, 7), (65, 500, 1)]

#Decodificacion
cod = []
for x in mensaje:
    inicio,step,veces = x
    nterm = inicio + (step * (veces-1))
    #print(inicio, step, veces, nterm)
    cod.append(nterm)
#print(cod)

#Traduccion
msj = []
for x in cod:
    for i in tabla:
        term,letr = i
        #print(x,term,letr)
        if x == term:
            msj.append(letr)

#Impresion
for x in msj:
    print(x,end="")