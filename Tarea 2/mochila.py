
# Basado en programación dinámica
# Programa para el problema de mochila 0-1
# Devuelve el valor máximo que puede
# ser puesto en una mochila de capacidad W

def knapSack(W, wt, val, n): 
    # Esto se usa para iterar listas (Lists comprehensions)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  

    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  

val = [50, 100, 10] 
wt = [40, 50, 15] 
W = 60
n = len(val) 
print(knapSack(W, wt, val, n)) 