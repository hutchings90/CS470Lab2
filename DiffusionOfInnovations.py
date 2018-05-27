import random
import copy
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

    def diffusionRun(self, n):
        self.reset()
        for network in self.networks:
            roundOne = True
            ids = list(range(len(network.agents)))
            random.shuffle(ids)
            for i in range(n):
                network.agents[ids[i]].adoptEarly()
            hasChanged = True
            while hasChanged:
                hasChanged = False
                copyAgents = copy.deepcopy(network.agents)
                for i in ids:
                    agent = network.agents[i]
                    if agent.earlyAdopter == False:
                        hunt = agent.hunt
                        agent.chooseHunt(copyAgents[i].neighbors, roundOne)
                        if hunt != agent.hunt:
                            hasChanged = True
            roundOne = False
            print('stags', end='\t')
            for i in ids:
                agent = network.agents[i]
                if agent.hunt == 0:
                    print(agent.id, end=', ')
            print('\nhares', end='\t')
            for i in ids:
                agent = network.agents[i]
                if agent.hunt == 1:
                    print(agent.id, end=', ')
            print('\n')

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
diffusionOfInnovations.diffusionRun(1)
diffusionOfInnovations.diffusionRun(2)
