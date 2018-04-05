from Genetic_Algorithm_Diophantine import GeneticAlgorithmDiophantine
from random import random


def main():
    equation = [1, 2, 3, 4]
    result = 30
    initial_population = [
        [int(random() * result) for _ in range(len(equation))]
        for _ in range(10)
    ]

    print GeneticAlgorithmDiophantine(equation, result, initial_population).solve()


main()
