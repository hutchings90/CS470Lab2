import Network

class DiffusionOfInnovations:
    likelihoodOptions = [
        [[1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3]],
        [[1 / 2, 1 / 4, 1 / 4], [1 / 4, 1 / 2, 1 / 4], [1 / 4, 1 / 4, 1 / 2]],
        [[1 / 4, 1 / 2, 1 / 4], [1 / 4, 1 / 4, 1 / 2], [1 / 2, 1 / 4, 1 / 4]],
    ]
    utilities = [[100, -70, -70], [-70, 100, -70], [-70, -70, 100]]
    numAgentOptions = [.05, .45]
    accuracyOptions = ['accurate', 'inaccurate', 'random']
    boundOptions = [.1]
    def __init__(self):
        self.reset()

    def reset(self):
        self.oneCycle = Network.makeOneCycle()
        self.twoCycle = Network.makeTwoCycle()
        self.complete = Network.makeComplete()
        self.adHoc = Network.makeAdHoc()

    def cascadeAndUtilityRun(self, network):
        with open('output2.csv', 'w+') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for likelihoods in DiffusionOfInnovations.likelihoodOptions:
                writer.writerow('likelihoods:,' + str(likelihoods))
                for numAgents in DiffusionOfInnovations.numAgentOptions:
                    writer.writerow('numAgents:,' + str(numAgents))
                    for accuracy in DiffusionOfInnovations.accuracyOptions:
                        writer.writerow(accuracy)
                        for bound in DiffusionOfInnovations.boundOptions:
                            totals = [0] * 3
                            total = 0
                            for b in range(5):
                                self.reset(likelihoods)
                                self.setPriors(accuracy, bound, int(numAgents * len(network.agents)))
                                self.chooseTap(network.agents[0])
                                tapChosen = self.sequentialKnowledge[0]
                                for i in range(1, len(network.agents)):
                                    self.calculatePosterior(i,tapChosen)
                                    self.chooseTap(network.agents[i])
                                    tapChosen= self.sequentialKnowledge[i]
                                for tap in self.taps:
                                    totals[tap.id] += len(tap.visitors)
                                total += len(network.agents)
                            writer.writerow('Tap,#Visitors,#Households,%Visitors')
                            for i in range(len(totals)):
                                visitorCount = totals[i]
                                writer.writerow(str(i) + ',' + str(visitorCount) + ',' + str(total) + ',' + str((visitorCount / total) * 100))

    def calculatePosterior(self,count, tapChosen):
        for x in range(count, len(network.agents)):
            sum = 0
            postProb= [0]*3
            for i in range(3):  # i is index for working tap number
                pos = self.likelihoods[tapChosen][i]
                postProb[i] = network.agents[x].priors[i] * pos
                sum += postProb[i]
            alpha = 1 / sum
            for j in range(3):
                network.agents[x].priors[j] = postProb[j]*alpha

    def setPriors(self, accuracy, bound, numAgents):
        if accuracy == 'accurate':
            self.accuratePriors(bound, numAgents)
        elif accuracy == 'inaccurate':
            self.inaccuratePriors(bound, numAgents)
        elif accuracy == 'random':
            self.randomPriors()

    def accuratePriors(self, bound, stop):
        inc = random.uniform(.01, bound)
        for i in range(stop):
            agent = network.agents[i]
            agent.priors[0] += inc
            agent.priors[1] -= random.uniform(0,inc)
            agent.priors[2] = 1 - agent.priors[0] - agent.priors[1]

    def inaccuratePriors(self, bound, stop):
        inc = random.uniform(.01, bound)
        for i in range(stop):
            agent = network.agents[i]
            agent.priors[0] -= inc
            agent.priors[1] += random.uniform(0, inc)
            agent.priors[2] = 1 - agent.priors[0] - agent.priors[1]

    def randomPriors(self):
        for agent in network.agents:
            priors = []
            for i in range(3):
                priors.append(random.randint(0, 1000))
            s = sum(priors)
            for i in range(3):
                priors[i] = priors[i] / s
            agent.priors = priors

    def chooseTap(self, agent):
        chosenTap = agent.chooseTap()
        self.sequentialKnowledge.append(chosenTap)
        self.taps[chosenTap].visit(agent)

    def visitTapUtility(self, chosenTap, agent):
        self.sequentialKnowledge.append(chosenTap)
        self.taps[chosenTap].utilityVisit(agent)

    def reset(self, likelihoods):
        self.likelihoods = likelihoods

        self.taps = [0] * 3
        for i in range(len(self.taps)):
            self.taps[i] = Tap(i)
        self.taps[0].isAvailable = True

        network.agents = [0] * random.randint(20, 50)
        for i in range(len(network.agents)):
            network.agents[i] = Household(i)

        self.sequentialKnowledge = []

    def __str__(self):
        string = '------------------------------------------ DiffusionOfInnovations ------------------------------------------\n'
        string += str(self.oneCycle) + '\n\n'
        string += str(self.twoCycle) + '\n\n'
        string += str(self.complete) + '\n\n'
        string += str(self.adHoc)
        return string

print(DiffusionOfInnovations())