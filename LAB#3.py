import random


def generate_individual():
    return [random.randint(0, 1) for _ in range(50)]


def calculate_fitness(individual):
    return sum(individual)


def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, individual in enumerate(population):
        current += fitnesses[i]
        if current > pick:
            return individual


def crossover(parent1, parent2, crossover_rate=0.7):
    if random.random() < crossover_rate:
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1, parent2


def mutate(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]


def genetic_algorithm(population_size=100, generations=500, crossover_rate=0.7, mutation_rate=0.01):
    population = [generate_individual() for _ in range(population_size)]
    best_fitness_progress = []

    for _ in range(generations):
        fitnesses = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitnesses)
        best_fitness_progress.append(best_fitness)

        new_population = []
        # Preserve the best individual
        elite = max(population, key=calculate_fitness)
        new_population.append(elite[:])
        while len(new_population) < population_size:
            parent1 = roulette_wheel_selection(population, fitnesses)
            parent2 = roulette_wheel_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population[:population_size]
        if calculate_fitness(elite) == 50:
            break
    return best_fitness_progress, max(population, key=calculate_fitness)


# Testing loop
results = {}
for pop_size in [10, 50, 100]:
    for cross_rate in [0.5, 0.7, 0.9]:
        for mut_rate in [0.01, 0.05, 0.1]:
            progress, best_individual = genetic_algorithm(
                population_size=pop_size,
                generations=500,
                crossover_rate=cross_rate,
                mutation_rate=mut_rate
            )
            results[(pop_size, cross_rate, mut_rate)] = {
                "Best Fitness Progress": progress,
                "Best Individual Fitness": calculate_fitness(best_individual),
                "Best Individual": best_individual
            }

print(results)
