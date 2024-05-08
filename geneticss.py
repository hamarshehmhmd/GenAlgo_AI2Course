import numpy as np


def initialize_population(pop_size, chrom_length):
    return np.random.randint(2, size=(pop_size, chrom_length))


def evaluate_population(population):
    return np.sum(population, axis=1)


def selection(population, fitness):
    probabilities = fitness / np.sum(fitness)
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[selected_indices]


def crossover(parent1, parent2, crossover_rate):
    if np.random.rand() < crossover_rate:
        crossover_point = np.random.randint(1, len(parent1))
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2
    else:
        return parent1, parent2


def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual


def genetic_algorithm(pop_size, chrom_length, crossover_rate, mutation_rate):
    population = initialize_population(pop_size, chrom_length)
    best_individual = None
    best_fitness = -1
    iteration = 0

    while True:
        fitness = evaluate_population(population)
        max_fitness = np.max(fitness)

        if max_fitness > best_fitness:
            best_fitness = max_fitness
            best_individual = population[np.argmax(fitness)]
            print("New best individual found:", best_individual, "Fitness:", best_fitness)

        selected_population = selection(population, fitness)

        new_population = []
        for i in range(0, pop_size, 2):
            parent1, parent2 = selected_population[i], selected_population[i + 1]
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = np.array(new_population)

        iteration += 1

    return best_individual, best_fitness


pop_size = 50
chrom_length = 50
crossover_rate = 0.6
mutation_rate = 0.03

best_individual, best_fitness = genetic_algorithm(pop_size, chrom_length, crossover_rate, mutation_rate)
print("Best individual found:", best_individual, "Fitness:", best_fitness)
