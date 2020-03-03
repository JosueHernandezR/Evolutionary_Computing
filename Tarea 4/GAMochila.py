# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import random as rd
from random import randint
import matplotlib.pyplot as plt
# Rango de datos 1-10
item_number = np.arange(1, 11)
# Peso aleatorio entre 1 a 15
weight = np.random.randint(1, 15, size=10)
# Valor aleatorio entre 10 y 750
value = np.random.randint(10, 750, size=10)
# Máximo peso que puede llevar en la mochila
knapsack_threshold = 35
# Imprime los elementos creados
print('The list is as follows:')
print('Item No.   Weight   Value')
for i in range(item_number.shape[0]):
    print('{0}          {1}         {2}\n'.format(
        item_number[i], weight[i], value[i]))

# Soluciones por  población
solutions_per_pop = 8
pop_size = (solutions_per_pop, item_number.shape[0])
print('Population size = {}'.format(pop_size))
initial_population = np.random.randint(2, size=pop_size)
initial_population = initial_population.astype(int)
# Número de generaciones
num_generations = 50
# Número de filas = soluciones po población
# Número de columnas = N+umero de objetos
print('Initial population: \n{}'.format(initial_population))


#  La función fitness que se usa para este problema es:
# fitness = suma(c_i*v_i, i, 1, n); SI suma(c_i*w_i, i, 1, n) <= kw
# Donde n = Longitud del cromosoma
# c_i = iésima generación
# v_i = iésimo valor
# w_i = iésimo peso
# kw  = tamaño de la mochila

def cal_fitness(weight, value, population, threshold):
    fitness = np.empty(population.shape[0])
    for i in range(population.shape[0]):
        # Sumatoria
        S1 = np.sum(population[i] * value)
        S2 = np.sum(population[i] * weight)
        # SI se cumple la condición
        if S2 <= threshold:
            fitness[i] = S1
        else:
            fitness[i] = 0
    return fitness.astype(int)

# Ahora seleccionamos a las personas más aptas para que puedan someterse a un crossover.
# En la selección, para cada iteración seleccionamos al individuo más apto y lo agregamos a los padres.


def selection(fitness, num_parents, population):
    fitness = list(fitness)
    parents = np.empty((num_parents, population.shape[1]))
    for i in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        parents[i, :] = population[max_fitness_idx[0][0], :]
        fitness[max_fitness_idx[0][0]] = -999999
    return parents

# Para el crossover se usara el de un punto (La primera mitad del coromosa 1
# y la segunda mitad del cromosoma 2)


def crossover(parents, num_offsprings):
    offsprings = np.empty((num_offsprings, parents.shape[1]))
    crossover_point = int(parents.shape[1]/2)
    crossover_rate = 0.8
    i = 0
    while (parents.shape[0] < num_offsprings):
        parent1_index = i % parents.shape[0]
        parent2_index = (i+1) % parents.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1_index = i % parents.shape[0]
        parent2_index = (i+1) % parents.shape[0]
        offsprings[i, 0:crossover_point] = parents[parent1_index,
                                                   0:crossover_point]
        offsprings[i, crossover_point:] = parents[parent2_index,
                                                  crossover_point:]
        i = +1
    return offsprings

# En la mutación, el cromosoma sufrirá mutación se está haciendo al azar.
# Para crear mutantes usaremos la técnica de cambio de bits, es decir,
# si el gen seleccionado que va a sufrir mutación es 1, cámbielo a 0 y viceversa.


def mutation(offsprings):
    mutants = np.empty((offsprings.shape))
    mutation_rate = 0.4
    for i in range(mutants.shape[0]):
        random_value = rd.random()
        mutants[i, :] = offsprings[i, :]
        if random_value > mutation_rate:
            continue
        int_random_value = randint(0, offsprings.shape[1]-1)
        if mutants[i, int_random_value] == 0:
            mutants[i, int_random_value] = 1
        else:
            mutants[i, int_random_value] = 0
    return mutants


def optimize(weight, value, population, pop_size, num_generations, threshold):
    parameters, fitness_history = [], []
    num_parents = int(pop_size[0]/2)
    num_offsprings = pop_size[0] - num_parents
    for i in range(num_generations):
        fitness = cal_fitness(weight, value, population, threshold)
        fitness_history.append(fitness)
        parents = selection(fitness, num_parents, population)
        offsprings = crossover(parents, num_offsprings)
        mutants = mutation(offsprings)
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = mutants

    print('Last generation: \n{}\n'.format(population))
    fitness_last_gen = cal_fitness(weight, value, population, threshold)
    print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(population[max_fitness[0][0], :])
    return parameters, fitness_history


parameters, fitness_history = optimize( weight, value, initial_population, pop_size, num_generations, knapsack_threshold)
print('The optimized parameters for the given inputs are: \n{}'.format(parameters))
selected_items = item_number * parameters
print('\nSelected items that will maximize the knapsack without breaking it:')
for i in range(selected_items.shape[1]):
    if selected_items[0][i] != 0:
        print('{}\n'.format(selected_items[0][i]))


fitness_history_mean = [np.mean(fitness) for fitness in fitness_history]
fitness_history_max = [np.max(fitness) for fitness in fitness_history]
plt.plot(list(range(num_generations)), fitness_history_mean, label='Mean Fitness')
plt.plot(list(range(num_generations)), fitness_history_max, label='Max Fitness')
plt.legend()
plt.title('Fitness through the generations')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.show()
print(np.asarray(fitness_history).shape)
