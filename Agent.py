class Agent:
    def __init__(self, i):
        self.id = i
        self.priors = [1 / 3] * 3

    def chooseTap(self):
        bestP = max(self.priors)
        bestIndices = []
        for i in range(3):
            if self.priors[i] == bestP:
                bestIndices.append(i)
        random.shuffle(bestIndices)
        return bestIndices[random.randint(0, len(bestIndices) - 1)]

    def __str__(self):
        string = 'id:\n\t' + str(self.id) + '\npriors:\n'
        priorTotal = 0
        for prior in self.priors:
            string += '\t' + str(prior) + '\n'
            priorTotal += prior
        string += 'priorTotal:\n\t' + str(priorTotal) + '\n'
        return string
