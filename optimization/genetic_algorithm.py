import random
import numpy as np
from typing import List


def simulate_traffic(signal_timings: List[int]) -> float:
    """
    Simulate traffic and return the overall waiting time for vehicles based on the given signal timings.

    Args:
        signal_timings (List[int]): A list of green light durations (in seconds) for each intersection.

    Returns:
        float: Simulated total waiting time for vehicles.
    """
    # Placeholder for actual simulation logic
    total_wait_time = sum(signal_timings) * random.uniform(
        0.8, 1.2
    )  # Simulated wait time
    return total_wait_time


def fitness(signal_timings: List[int]) -> float:
    """
    Calculate the fitness of a set of signal timings by simulating traffic.
    Fitness is inversely proportional to the total wait time (lower wait time = better fitness).

    Args:
        signal_timings (List[int]): A list of green light durations (in seconds) for each intersection.

    Returns:
        float: Fitness score, where higher is better.
    """
    total_wait_time = simulate_traffic(signal_timings)
    return 1 / total_wait_time  # Lower wait time means better fitness


def create_population(pop_size: int, num_intersections: int) -> List[List[int]]:
    """
    Create an initial population of signal timings for multiple intersections.

    Args:
        pop_size (int): The number of individuals in the population.
        num_intersections (int): The number of intersections (each individual will have a timing for each intersection).

    Returns:
        List[List[int]]: A population of individuals, each represented as a list of signal timings (in seconds).
    """
    return [
        np.random.randint(10, 120, size=num_intersections).tolist()
        for _ in range(pop_size)
    ]


def select(
    population: List[List[int]], fitnesses: List[float], num_parents: int
) -> List[List[int]]:
    """
    Select the top individuals with the highest fitness scores to be the parents of the next generation.

    Args:
        population (List[List[int]]): The current population of individuals.
        fitnesses (List[float]): The fitness scores for each individual.
        num_parents (int): The number of parents to select for reproduction.

    Returns:
        List[List[int]]: A list of selected parents for the next generation.
    """
    sorted_pop = [x for _, x in sorted(zip(fitnesses, population), reverse=True)]
    return sorted_pop[:num_parents]


def crossover(parents: List[List[int]], offspring_size: int) -> List[List[int]]:
    """
    Perform crossover to create new offspring by combining genes (signal timings) from two parents.

    Args:
        parents (List[List[int]]): A list of parent individuals.
        offspring_size (int): The number of offspring to generate.

    Returns:
        List[List[int]]: A list of new offspring created by crossover.
    """
    offspring = []
    for _ in range(offspring_size):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)

        # Perform crossover by randomly mixing the genes (green light durations)
        child = [random.choice(gene) for gene in zip(parent1, parent2)]
        offspring.append(child)
    return offspring


def mutate(offspring: List[List[int]], mutation_rate: float = 0.1) -> List[List[int]]:
    """
    Apply mutation to the offspring, randomly altering some signal timings.

    Args:
        offspring (List[List[int]]): A list of offspring individuals.
        mutation_rate (float): The probability of mutating each individual (default is 10%).

    Returns:
        List[List[int]]: The mutated offspring.
    """
    for child in offspring:
        if random.random() < mutation_rate:
            # Randomly change one green light duration
            mutation_index = random.randint(0, len(child) - 1)
            child[mutation_index] = random.randint(
                10, 120
            )  # New random green light duration
    return offspring


def genetic_algorithm(
    pop_size: int, num_intersections: int, generations: int
) -> List[int]:
    """
    Run the genetic algorithm to optimize traffic signal timings for multiple intersections.

    Args:
        pop_size (int): The number of individuals in the population.
        num_intersections (int): The number of intersections (each individual will have a timing for each intersection).
        generations (int): The number of generations to evolve the population.

    Returns:
        List[int]: The optimal signal timings (in seconds) for each intersection after running the GA.
    """
    # Create initial population
    population = create_population(pop_size, num_intersections)

    for gen in range(generations):
        # Evaluate fitness for each individual in the population
        fitnesses = [fitness(individual) for individual in population]

        # Select the top individuals to be the parents
        parents = select(population, fitnesses, num_parents=pop_size // 2)

        # Generate new offspring through crossover
        offspring_size = pop_size - len(parents)
        offspring = crossover(parents, offspring_size)

        # Mutate some offspring
        offspring = mutate(offspring)

        # Form the new population
        population = parents + offspring

        # Output the best solution in the current generation
        best_fitness = max(fitnesses)
        best_solution = population[fitnesses.index(best_fitness)]
        print(
            f"Generation {gen+1}: Best Fitness = {best_fitness}, Best Solution = {best_solution}"
        )

    # Return the best solution from the final generation
    return best_solution
