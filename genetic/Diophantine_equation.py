from Genetic_Algorithm_Diophantine import GeneticAlgorithmDiophantine
from random import random


def main():
    equation = [1, 2, 3, 4]
    result = 30
    initial_population = [
        [int(random() * result) for _ in range(4)]
        for _ in range(6)
    ]

    print GeneticAlgorithmDiophantine(equation, result, initial_population).solve()


main()
