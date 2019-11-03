morse = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
    ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'),
    ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'), ('0', '-----'), ('1', '.----'), ('2', '..---'),
    ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'),
    ('7', '--...'), ('8', '---..'), ('9', '----.')
    ]

# Dejar las letras unicamente, y de esa forma poder capturar el indice de forma mas facil
letras = []
for x in range(len(morse)):
    letras.append(morse[x][0])
letras.append(" ") # Incluyendo el espacio como numero 36

# Entrada
texto = input() # Ingreso de texto
texto = texto.upper() # Transformar a mayusculas
# print(texto)

# En esta lista se dejara los indices de cada letra del texto a en la lista de morse
indices = []
for x in texto:
    # print(x, letras.index(x))
    if x in letras: # si el caracter es una letra... (si no lo es, lo omite)
        indices.append(letras.index(x))
# print(indices)

frase = []
noHuboEspacio = True # Si hubo un espacio antes
for x in indices:
    if not x == 36: # Si no es un espacio
        print(morse[x][1],end=" ")
        noHuboEspacio = True
    elif x == 36 and noHuboEspacio: # si es un espacio, nueva linea
        print("")
        noHuboEspacio = False
