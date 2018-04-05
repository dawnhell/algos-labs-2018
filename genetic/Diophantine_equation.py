from Genetic_Algorithm_Diophantine import GeneticAlgorithmDiophantine
from random import random


def main():
    f = file("results.txt", "rw+")

    very_very_simple_equation = [1, 2, 3]
    result = 30
    initial_population = [
        [int(random() * result) for _ in range(len(very_very_simple_equation))]
        for _ in range(5)
    ]
    answer = GeneticAlgorithmDiophantine(very_very_simple_equation, result, initial_population).solve(1)

    f.write("Diophantine equation x + 2y + 3z = 30:\n")
    f.write("\nRank selection:\n")
    f.write("Fitness: " + str(answer[0]) + ", solution: " + str(answer[1][0]) + ", iterations: " + str(answer[2]) + "\n")

    answer = GeneticAlgorithmDiophantine(very_very_simple_equation, result, initial_population).solve(2)

    f.write("\nTournament selection:\n")
    f.write("Fitness: " + str(answer[0]) + ", solution: " + str(answer[1][0]) + ", iterations: " + str(answer[2]) + "\n")

    more_complex_equation = [1, 2, 3, 5, 23, 7, 45, 23, 1, 87, 34]
    result = 500
    initial_population = [
        [int(random() * result) for _ in range(len(more_complex_equation))]
        for _ in range(10)
    ]
    answer = GeneticAlgorithmDiophantine(more_complex_equation, result, initial_population).solve(1)

    f.write("\n\nDiophantine equation a + 2b + 3c + 5d + 23e + 7f + 45g + 23h + i + 87j + 34k = 500:\n")
    f.write("\nRank selection:\n")
    f.write("Fitness: " + str(answer[0]) + ", solution: " + str(answer[1][0]) + ", iterations: " + str(answer[2]) + "\n")

    answer = GeneticAlgorithmDiophantine(more_complex_equation, result, initial_population).solve(2)

    f.write("\nTournament selection:\n")
    f.write("Fitness: " + str(answer[0]) + ", solution: " + str(answer[1][0]) + ", iterations: " + str(answer[2]) + "\n")

    f.close()


main()
