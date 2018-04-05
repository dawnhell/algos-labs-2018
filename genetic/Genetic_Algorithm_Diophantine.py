from random import random, randrange


class GeneticAlgorithmDiophantine:
    def __init__(self, equation, result, initial_population):
        self.equation = equation
        self.result = result
        self.population = initial_population
        self.chromosome_size = len(initial_population[0])

    def solve(self):
        current_fitness = self.calculate_fitness(self.equation, self.population[0], self.result)
        iterations = 0

        while current_fitness > 0 and iterations < 1000:
            iterations += 1
            middle = int(len(self.population) / 2)

            for i in range(middle):
                child1, child2 = self.one_point_crossingover(
                    self.population[i],
                    self.population[middle + i],
                    self.chromosome_size / 2
                )

                child1 = self.mutation(child1)
                child2 = self.mutation(child2)

                self.population += [child1]
                self.population += [child2]

            # self.rang_selection()
            self.tournament_selection()

            fitness = self.calculate_fitness(self.equation, self.population[0], self.result)

            if fitness < current_fitness:
                current_fitness = fitness

            if current_fitness == 0:
                break

        return current_fitness, self.population, iterations

    def rang_selection(self):
        fitness = []

        for j in range(len(self.population)):
            fitness.append((self.calculate_fitness(self.equation, self.population[j], self.result), j))

        fitness = sorted(fitness)

        new_population = []
        for index, key in enumerate(fitness):
            if index < len(fitness) / 2:
                new_population.append(self.population[key[1]])

        self.population = new_population

    def tournament_selection(self):
        new_population = []

        while len(self.population) > 0:
            if len(self.population) == 1:
                new_population.append(self.population[0])
                del self.population[0]
            else:
                soldier1 = randrange(len(self.population) - 1)
                soldier2 = randrange(len(self.population) - 1)

                soldier1_fitness = self.calculate_fitness(self.equation, self.population[soldier1], self.result)
                soldier2_fitness = self.calculate_fitness(self.equation, self.population[soldier2], self.result)

                if soldier1_fitness < soldier2_fitness:
                    new_population.append(self.population[soldier1])
                else:
                    new_population.append(self.population[soldier2])

                del self.population[soldier1]
                del self.population[soldier2]

        self.population = new_population

    @staticmethod
    def calculate_fitness(equation, population, result):
        temp_solution = 0
        for i in range(len(equation)):
            temp_solution += equation[i] * population[i]

        return abs(result - temp_solution)

    @staticmethod
    def one_point_crossingover(parent1, parent2, crossingover_point):
        offspring1 = parent1[:crossingover_point] + parent2[crossingover_point:]
        offspring2 = parent2[:crossingover_point] + parent1[crossingover_point:]

        return offspring1, offspring2

    def mutation(self, organism):
        if random() < 0.3:
            organism[int(random() * self.chromosome_size)] = int(random() * self.result)

        return organism

