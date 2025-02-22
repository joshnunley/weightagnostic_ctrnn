import matplotlib.pyplot as plt
import numpy as np

from CTRNN import CTRNN
from EvolSearch import EvolSearch
from fitnessFunction_vehicle import fitnessFunction_vehicle

ctrnn_size = 12
pop_size = 200
step_size = 0.005


########################
# Evolve Solutions
########################

genotype_size = ctrnn_size ** 2 + 2 * ctrnn_size


evol_params = {
    "num_processes": 6,
    "pop_size": pop_size,  # population size
    "genotype_size": genotype_size,  # dimensionality of solution
    "fitness_function": lambda x: fitnessFunction_vehicle(
        x, ctrnn_size, step_size
    ),  # custom function defined to evaluate fitness of a solution
    "elitist_fraction": 0.1,  # fraction of population retained as is between generation
    "mutation_variance": 0.005,  # mutation noise added to offspring.
}
initial_pop = np.zeros(shape=(pop_size, genotype_size))
variable_mins = []
variable_maxes = []


evolution = EvolSearch(evol_params, initial_pop)
evolution.step_generation()

best_fitness = []
best_fitness.append(evolution.get_best_individual_fitness())
print("best fitness: ", best_fitness)

print(evolution.get_best_individual())

mean_fitness = []
mean_fitness.append(evolution.get_mean_fitness())

while best_fitness[-1] < 500:
    print("HERE")
    evolution.step_generation()
    best_individual = evolution.get_best_individual()
    best_individual_fitness = fitnessFunction_vehicle(
        best_individual, ctrnn_size, step_size
    )

    best_fitness.append(best_individual_fitness)
    mean_fitness.append(evolution.get_mean_fitness())

    print(len(best_fitness), best_fitness[-1], evolution.get_mean_fitness())

