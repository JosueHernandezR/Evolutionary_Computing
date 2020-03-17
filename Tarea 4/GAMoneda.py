import os
from random import randint
import random
# Cambio a realizar
cambio = 9
# Denominaciones
monedas = [5, 2, 1]
# El tamaño del cromosoma es el tamaño de la lista de monedas
long_cromosomas = len(monedas)
# Generaciones
Generacion = 30
# Tamaño de población
población = 10

# Clase que define un cromosoma
class Cromosoma:
    cromosoma = []
    fitness = 0
    cambio = 0

    def __init__(self, cromosoma, cambio, fitness):
        self.cromosoma = cromosoma
        self.cambio = cambio
        self.fitness = fitness


def seleccionar(cromosoma):
    nuevos = []
    cromosomas_ordenado_fitness = sorted(
        cromosoma, key=lambda cromosoma: cromosoma.fitness, reverse=False)
    nuevos.append(cromosomas_ordenado_fitness[0])
    #print("Nuevos [0]: ", nuevos)
    nuevos.append(cromosomas_ordenado_fitness[1])
    #print("Nuevos [1]: ", nuevos)
    cromosomas = generar_población(nuevos, población - 2)
    for i in range(2, población-2):
        nuevos.append(cromosomas[i])
    print(type(nuevos))
    return nuevos

#Proceso de mutación
def mutar(cromosoma):
    aleatorio = randint(0, long_cromosomas-1)
    if cromosoma[aleatorio] == 2:
        cromosoma[aleatorio] = 1

    elif cromosoma[aleatorio] == 1:
        cromosoma[aleatorio] = 0

    else:
        cromosoma[aleatorio] = 2
    return cromosoma


def evaluar_fitness(cromosoma):
    cambio_cromosoma = 0
    fitness = 1
    for i in range(long_cromosomas):
        cambio_cromosoma += cromosoma[i]*monedas[i]

        if cambio_cromosoma > cambio:
            fitness = 0

        if cambio_cromosoma <= cambio:
            fitness = cambio_cromosoma

    return (cambio_cromosoma, fitness)


def generar_cromosoma(cromosoma):
    for i in range(long_cromosomas):
        if random.random() < 0.5:
            cromosoma.append(1)
        elif random.random() > 0.75:
            cromosoma.append(0)
        else:
            cromosoma.append(2)
    return cromosoma


def generar_población(cromosomas, población):
    for i in range(población):
        cromosoma = []
        cromosoma = generar_cromosoma(cromosoma)
        (cambio, fitness) = evaluar_fitness(cromosoma)
        cromosomas.append(Cromosoma(cromosoma, cambio, fitness))
    return cromosomas


os.system("clear")
print("CMP con GA \n\Change:", cambio)
print("\nMonedas:", monedas)
num_generacion = 1
cromosomas = []
cromosomas = generar_población(cromosomas, población)

# crea las generaciones
for j in range(Generacion):
    sol = []
    print("\nGeneracion", num_generacion, ":")
    for i in range(población):
        print(cromosomas[i].cromosoma, "\tCambio = ", cromosomas[i].cambio,
              "\tAptitud = ", cromosomas[i].fitness, sep="")
        sol.append(cromosomas[i].fitness)
    sol.sort(reverse=True)
    print("La mejor solucion de la generacion ", num_generacion,
          "es la que tiene el valor de fitness: ", sol[0])
    cromosomas = seleccionar(cromosomas)
    num_generacion += 1
