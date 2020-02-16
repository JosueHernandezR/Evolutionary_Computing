# Encuentra el minimo de monedas
def findMin(V): 
	# Ordenadas de manera ascendente
	deno = [1,2,5] 
	n = len(deno) 
	ans = [] 
	i = n - 1

	while(i >= 0): 
		# Encuentra las denominaciones
		while (V >= deno[i]):
            # Resta la denomianción mas alta al cambio para poder encontrar la siguiente moneda que
            # aun pueda darse 
			V -= deno[i];
            #Agrega la denominación restada a una lista.
			ans.append(deno[i]); 
		i -= 1
	# Imprime el resultado
	for i in range(len(ans)): 
		print(ans[i], end = " ") 

if __name__ == '__main__': 
	n = 13
	print("Following is minimal number", 
		"of change for", n, ": ", end = "") 
	findMin(n) 