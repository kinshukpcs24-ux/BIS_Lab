import math
import random

def fitness(i):
  return math.sin(i)
def cross(i1, i2, c_param):
  return i1*c_param + (1 - c_param)*i2

def mutate(i, mut_param):
  return i + random.gauss(0, mut_param)

def evolve(initial_population, ft, c_prob, c_param, mut_prob, mut_param, G):
  population = initial_population
  new_population = []

  for g in range(G):
    for i in range(len(population)):
      if fitness(population[i]) < ft:
        population[i] = 0
  
    for i in population:
      for j in population:
        if i!=j and i*j != 0:
          if random.random() > c_prob:
            new_population.append(cross(i, j, c_param))
  
    for i in range(len(new_population)):
      if random.random() > mut_prob:
        new_population[i] = mutate(new_population[i], mut_param)
  
    population = new_population
    new_population = []
  
  return population

def main():
  population = [random.random() for i in range(10)]
  final_population = []
  GENERATIONS = int(input("Enter number of generations: "))

  for i in range(2):
    print(f"\nPOPULATION SET {i+1}")
    FITNESS_THRESHOLD = float(input("Enter fitness threshold: "))
    CROSSOVER_PROBABILITY = float(input("Enter crossover probability: "))
    CROSSOVER_PARAM = float(input("Enter crossover parameter: "))
    MUTATION_PROBABILITY = float(input("Enter mutation probability: "))
    MUTATION_PARAM = float(input("Enter mutation parameter: "))

    final_population = evolve(population, FITNESS_THRESHOLD, CROSSOVER_PROBABILITY, CROSSOVER_PARAM, MUTATION_PROBABILITY, MUTATION_PARAM, GENERATIONS)
    print(f"\nResults after {GENERATIONS} generations:")
    print(f"Number of individuals : ", len(final_population))
    print("Average fitness of individuals : ", sum(final_population) / len(final_population) if len(final_population) !=0 else 0)
    print("Best individual : ", max(final_population) if len(final_population) !=0 else 0)
    print("Worst individual : ", min(final_population) if len(final_population) !=0 else 0)

main()
