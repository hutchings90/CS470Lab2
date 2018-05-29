import random
import copy
import Network
from Tap import Tap

class DiffusionOfInnovations:
    def cascadeRuns(self):
        self.cascadeRun(None)
        self.cascadeRun([1, 0, 0])
        self.cascadeRun([0, 1 / 2, 1 / 2])
        print('------------------------------')

    def cascadeRun(self, priors):
        self.reset()
        print(priors)
        for network in self.networks:
            ids = list(range(len(network.agents)))
            random.shuffle(ids)
            if priors != None:
                network.agents[ids[0]].priors = copy.deepcopy(priors)
            for i in ids:
                agent = network.agents[i]
                agent.chooseTap()
                print(str(agent.id) + '-' + str(agent.choice), end=', ')
            print()
        print()

    def diffusionRun(self, n):
        self.reset()
        asdf = 0
        for network in self.networks:
            generations = 0
            asdf += 1
            roundOne = True
            ids = list(range(len(network.agents)))
            if asdf == 4:
                network.agents[0].adoptEarly()
                network.agents[5].adoptEarly()
                network.agents[7].adoptEarly()
                network.agents[9].adoptEarly()
                network.agents[11].adoptEarly()
                network.agents[12].adoptEarly()
            else:
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
                            print(agent.id, end=', ')
                            hasChanged = True
                if hasChanged:
                    generations += 1
                print()
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
            print('\nGenerations:', generations, '\n')

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
# diffusionOfInnovations.diffusionRun(1)
# diffusionOfInnovations.diffusionRun(2)
for i in range(3):
    diffusionOfInnovations.cascadeRuns()
