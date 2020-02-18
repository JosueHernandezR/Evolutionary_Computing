import numpy as np
# Basado en programación dinámica
# Programa para el problema de mochila 0-1
# Devuelve el valor máximo que puede
# ser puesto en una mochila de capacidad W

def knapSack(W, wt, val): 
    #Filas
    n = len (val) + 1
    # Columnas
    W = W + 1
    K = np.zeros((n, W))
    # print(n,W)
    # Esto se usa para iterar listas (Lists comprehensions)
    #K = np.array([[0 for x in range(W+1)] for x in range(n+1)])
    # for y in range(W):
    #     K[0,y] = y
    # for x in range(n):
    #     K[x,0] = x
    # print(K)
    for i in range(1,n):
        # print("Iteración i: ",i) 
        for w in range(1,W):
            # print("Iteración w: ", w) 
            if i == 0 or w == 0: 
                K[i][w] = 0
                # print("Caso if:", i)
                # print(K)
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  
                            K[i-1][w]) 
                # print("Caso else if:", i)
                # print(K)
            else: 
                K[i][w] = K[i-1][w] 
                # print("Caso else:", i)
                # print(K)
    print("La matriz resultante es: ")
    print(K)
    return K[n-1][W-1] 
  

val = [20, 10, 5] 
wt = [4, 8, 3] 
W = 5
print("El resultado es:",knapSack(W, wt, val)) 