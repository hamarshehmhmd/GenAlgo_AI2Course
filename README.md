# Construction Material Agent & Genetic Algorithm

This repository contains two Python scripts: one implementing a Construction Material Agent and the other implementing a Genetic Algorithm.

## Construction Material Agent

The Construction Material Agent simulates the buying and selling of construction materials for building houses. It defines a class `ConstructionMaterialAgent` that manages materials and money for construction purposes. 

### Features

- Manages inventory of construction materials.
- Sells materials to builders based on house component requirements.
- Checks availability of materials before selling.
- Tracks money transactions.

### Usage

To use the Construction Material Agent:

1. Ensure you have Python installed.
2. Run the script `construction_material_agent.py`.
3. Check the console output for details of transactions.

## Genetic Algorithm

The Genetic Algorithm is an optimization algorithm inspired by the process of natural selection. This implementation aims to find an individual with the highest fitness score.

### Features

- Generates random individuals.
- Calculates fitness of individuals.
- Implements selection, crossover, and mutation operations.
- Evolves a population over generations to find the best individual.

### Usage

To use the Genetic Algorithm:

1. Ensure you have Python installed.
2. Run the script `genetic_algorithm.py`.
3. Check the console output for the best fitness progress and the best individual found.

## Example

An example of using the Genetic Algorithm to optimize parameters:

```python
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
