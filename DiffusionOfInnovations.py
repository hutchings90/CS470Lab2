import random
import Network
from Tap import Tap

class DiffusionOfInnovations:
    def cascadeRuns(self):
        n = random.randint(1, 3)
        self.cascadeRun(None, n)
        self.cascadeRun([1, 0, 0], n)
        self.cascadeRun([0, 1 / 2, 1 / 2], n)

    def cascadeRun(self, priors, n):
        self.reset()
        print()
        for network in self.networks:
            ids = list(range(len(network.agents)))
            random.shuffle(ids)
            if priors != None:
                for i in range(n):
                    network.agents[ids[i]].priors = priors
            for i in ids:
                agent = network.agents[i]
                priors = agent.priors
                agent.chooseTap()
                print(str(agent.id) + '-' + str(agent.choice), end=', ')
            print()

    def reset(self):
        self.taps = [0] * 3
        for i in range(len(self.taps)):
            self.taps[i] = Tap(i)
        self.taps[0].isAvailable = True
        self.networks = [Network.makeOneCycle(), Network.makeTwoCycle(), Network.makeComplete(), Network.makeAdHoc()]

    def __str__(self):
        string = '------------------------------------------ DiffusionOfInnovations ------------------------------------------\n'
        for network in self.networks:
            string += str(network) + '\n\n'
        return string

diffusionOfInnovations = DiffusionOfInnovations()
diffusionOfInnovations.cascadeRuns()
