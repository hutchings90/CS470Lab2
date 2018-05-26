import random

class Agent:
    likelihoods = [[1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3]]
    utilities = [100, -70, -70]

    def __init__(self, i):
        self.id = i
        self.reset()

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
        for neighbor in self.neighbors:
            neighbor.updatePosteriors()

    def updatePosteriors(self):
        sum = 0
        postProb= [0]*3
        for i in range(3):  # i is index for working tap number
            pos = DiffusionOfInnovations.likelihoods[tapChosen][i]
            postProb[i] = network.agents[x].priors[i] * pos
            sum += postProb[i]
        alpha = 1 / sum
        for j in range(3):
            network.agents[x].priors[j] = postProb[j]*alpha

    def reset(self):
        self.priors = [1 / 3] * 3
        self.neighbors = []
        self.choice = None
        self.earlyAdopter = False

    def __str__(self):
        string = 'Agent id:\n\t' + str(self.id) + '\npriors:\n'
        string += '\tEarly Adopter: ' + str(self.earlyAdopter)
        priorTotal = 0
        for prior in self.priors:
            string += '\t' + str(prior) + '\n'
            priorTotal += prior
        string += 'priorTotal:\n\t' + str(priorTotal) + '\n'
        string += 'neighbors:\n\t'
        for neighbor in self.neighbors:
            string += str(neighbor.id) + ', '
        return string
