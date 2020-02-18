def vueltasProgDin(listaValoresMonedas,vueltas,minMonedas,monedasUsadas):
    for centavos in range(vueltas+1):
        conteoMonedas = centavos
        nuevaMoneda = 1
        for j in [m for m in listaValoresMonedas if m <= centavos]:
            if minMonedas[centavos-j] + 1 < conteoMonedas:
               conteoMonedas = minMonedas[centavos-j]+1
               nuevaMoneda = j
        minMonedas[centavos] = conteoMonedas
        monedasUsadas[centavos] = nuevaMoneda
    # print(monedasUsadas)
    return minMonedas[vueltas]

def imprimirMonedas(monedasUsadas,vueltas):
    moneda = vueltas
    while moneda > 0:
        estaMoneda = monedasUsadas[moneda]
        print(estaMoneda)
        moneda = moneda - estaMoneda

def main():
    cantidad = int(input("Ingrese el cambio a devolver: "))
    listaM = [1,2,5,10,20,50]
    print("Las monedas disponibles son: ", listaM)
    monedasUsadas = [0]*(cantidad+1)
    conteoMonedas = [0]*(cantidad+1)

    print("Son",vueltasProgDin(listaM,cantidad,conteoMonedas,monedasUsadas),"monedas a devolver.")
    print("Tales monedas son:")
    imprimirMonedas(monedasUsadas,cantidad)
    print("La lista usada es la siguiente:")
    print(monedasUsadas)

main()
