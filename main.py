import numpy as np


POPULATION_SIZE = 50
GENE_LENGTH = 50
MUTATION_RATE = 0.03
TARGET = [1] * GENE_LENGTH
class Individual(object):
    '''
    Class representing individual in population
    '''
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(cls):
        '''
        create random genes for mutation
        '''
        return np.random.randint(2)

    @classmethod
    def create_gnome(cls):
        '''
        create chromosome or string of genes
        '''
        gnome_len = GENE_LENGTH
        return [cls.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''

        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            prob = np.random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.45:
                child_chromosome.append(gp1)

            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.90:
                child_chromosome.append(gp2)

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())

        # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(child_chromosome)

    def cal_fitness(self):
        '''
        Calculate fitness score, it is the sum of all genes
        '''
        return sum(self.chromosome)

# Driver code
def main():
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    while not found:

        # Sort the population in decreasing order of fitness score
        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        # If the individual having highest fitness score i.e.
        # the sum of all genes is equal to the target,
        # then we know that we have reached the target
        # and break the loop
        if population[0].fitness >= sum(TARGET):
            found = True
            break

        # Otherwise generate new offsprings for the new generation
        new_generation = []

        # Perform Elitism, that means 10% of fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # From 50% of the fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = np.random.choice(population[:50])
            parent2 = np.random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tSum: {}\tFitness: {}".format(generation, sum(population[0].chromosome), population[0].fitness))

        if population[0].fitness == 50:
            print("List of numbers: {}".format(population[0].chromosome))

        generation += 1

    print("Generation: {}\tSum: {}\tFitness: {}".format(generation, sum(population[0].chromosome), population[0].fitness))

if __name__ == '__main__':
    main()
