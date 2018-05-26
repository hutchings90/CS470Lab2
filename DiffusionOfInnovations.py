import Network
from Tap import Tap

class DiffusionOfInnovations:
    def __init__(self):
        self.reset()

    def cascadeRun(self, network):
        self.reset()
        self.randomPriors()
        ids = list(range(len(network.agents)))
        random.shuffle(ids)
        for i in ids:
            agent = network.agents[i]
            agent.chooseTap()

    def reset(self):
        self.taps = [0] * 3
        for i in range(len(self.taps)):
            self.taps[i] = Tap(i)
        self.taps[0].isAvailable = True

        self.networks = [Network.makeOneCycle(), Network.makeTwoCycle(), Network.makeComplete(), Network.makeAdHoc()]

    def __str__(self):
        string = '------------------------------------------ DiffusionOfInnovations ------------------------------------------\n'
        for network in self.network:
            string += str(network) + '\n\n'
        return string

print(DiffusionOfInnovations())
