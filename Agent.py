import random

class Agent:
    likelihoods = [[1 / 2, 1 / 4, 1 / 4], [1 / 4, 1 / 2, 1 / 4], [1 / 4, 1 / 4, 1 / 2]]
    utilities = [
        [[2, 2], [0, 1]],
        [[1, 0], [1, 1]]
    ]

    def __init__(self, i):
        self.id = i
        self.priors = [1 / 3] * 3
        self.neighbors = []
        self.choice = None
        self.earlyAdopter = False
        self.hunt = 1

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def chooseTap(self):
        bestP = max(self.priors)
        bestIndices = []
        for i in range(3):
            if self.priors[i] == bestP:
                bestIndices.append(i)
        random.shuffle(bestIndices)
        self.choice = bestIndices[random.randint(0, len(bestIndices) - 1)]
        self.updateNeighborPosteriors()
        return self.choice

    def updateNeighborPosteriors(self):
        choice = self.choice
        for neighbor in self.neighbors:
            neighbor.updatePosteriors(choice)

    def updatePosteriors(self, choice):
        sum = 0
        postProb = [0] * 3
        for i in range(3):
            pos = Agent.likelihoods[choice][i]
            postProb[i] = self.priors[i] * pos
            sum += postProb[i]
        alpha = 1 / sum
        for j in range(3):
            self.priors[j] = postProb[j] * alpha

    def __str__(self):
        string = 'Agent id:\n\t' + str(self.id) + '\npriors:\n'
        string += '\tEarly Adopter: ' + str(self.earlyAdopter) + '\n'
        priorTotal = 0
        for prior in self.priors:
            string += '\t' + str(prior) + '\n'
            priorTotal += prior
        string += 'priorTotal:\n\t' + str(priorTotal) + '\n'
        string += 'neighbors:\n\t'
        for neighbor in self.neighbors:
            string += str(neighbor.id) + ', '
        return string

    def adoptEarly(self):
        self.earlyAdopter = True
        self.hunt = 0

    def chooseHunt(self, neighbors, y):
        changeCount = 0
        stayCount = 0
        mySwitch = (self.hunt + 1) % 2
        for neighbor in neighbors:
            changeCount += Agent.utilities[mySwitch][neighbor.hunt][0]
            stayCount += Agent.utilities[self.hunt][neighbor.hunt][0]
        if changeCount > stayCount:
            self.hunt = mySwitch
        return self.hunt
