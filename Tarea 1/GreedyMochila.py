def knapSack(w, wt, val, n):
    # Devuelve el valor máximo que se puede poner en una mochila de capácidad W
    
    #Caso base
    if n == 0 or w == 0:
        return 0
    if (wt[n-1] > w):
        # Si el peso del enésimo elemento es superior a
        # Mochila de capacidad w, entonces este artículo
        # no se puede incluir en la solución óptima.
        return knapSack(w, wt, val, n-1)
    else:
        #Devuelve el máximo de dos casos:
        #- N-ésimo artículo incluido
        #- no incluido

        return max(val[n-1] + knapSack(w-wt[n-1], wt, val, n-1),
                   knapSack(w, wt, val, n-1))
def main():
    '''Entry point to the program'''
    val = [4,10,2,2,1]
    wt = [12, 4, 2, 1, 1]
    w = 15
    n = len(val)
    print("The values are: ", val)
    print("The weights are: ", wt)
    print("The maximum weight is: ", w)
    print(f"Total value which the Knapsack Bag of weight {w} can hold is:\t{knapSack(w, wt, val, n)}")
main()