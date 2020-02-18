import numpy as np

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    #Llena las matrices conforme al tamaño de las palabras
    #Para las filas iniciando en 1
    for x in range(size_x):
        matrix [x, 0] = x
    #Para las columnas
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    print ("El número de cambios son: ",matrix[size_x - 1, size_y - 1])
    print (matrix)
    return (matrix[size_x - 1, size_y - 1])

a=input("Primera palabra: ")
b=input("Segunda palabra: ")

"""
a= "texto"
b= "libro"
"""
levenshtein(a,b)