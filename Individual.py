import random

class Individual:
	# Updates the fitness value based on the genom and the map.
    def updateFitness(self):
        #TODO implement fitness function
        #how many violations?
        num = 0
        for border in self.map.borders:
            s1 = self.genome[self.map.states[border.index1]] #color 1
            s2 = self.genome[self.map.states[border.index2]] #color 2
            if s1 != s2:
                num += 1
        self.fitness=num 

    def random_individual(self):
        # TODO implement random generation of an individual
        self.genome = {state: random.randint(1, 4) for state in self.map.states}  # Assuming 4 colors


    def __init__(self,map):
        self.map=map# the map
        self.fitness=0
        # TODO some representation of the genome of the individual
        # TODO implement random generation of an individual
        self.random_individual()
        self.updateFitness()

    # Reproduces a child randomly from two individuals (see textbook).
	# x The first parent.
	# y The second parent.
	# return The child created from the two individuals.
    def reproduce(self, x, y):
        child = Individual(x.map)
        # TODO: Implement the reproduction process to create a child from parents x and y.
        # For example, you can perform one-point crossover.
        crossover_point = random.randint(1, len(self.map.states) - 1)
        for i, state in enumerate(self.map.states):
            if i < crossover_point:
                child.genome[state] = x.genome[state]
            else:
                child.genome[state] = y.genome[state]
        child.updateFitness()
        return child

	# Randomly mutates the individual.
    def mutate(self):
        # TODO implement random mutation of the individual
        state_to_mutate = random.choice(list(self.map.states))
        new_color = random.randint(1, 4)  # Assuming 4 colors
        self.genome[state_to_mutate] = new_color
        self.updateFitness()

	# Checks whether the individual represents a valid goal state.
	# return Whether the individual represents a valid goal state.
    def isGoal(self):
        return self.fitness == len(self.map.borders)

    def printresult(self):
        # TODO implement printing the individual in the following format:
        # fitness: 15
        # North Carolina: 0
        # South Carolina: 2
        # ...
        dict = {
            1:'Red',
            2:'Blue',
            3:'Yellow',
            4:'Green'
        }
        print("Your result:")
        print("Fitness Rating: ", self.fitness)
        for key, value in self.genome.items():
            print(key, ": ", dict[value])

