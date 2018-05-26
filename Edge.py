class Edge:
    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2

    def __str__(self):
        return str(self.agent1.id) + '-' + str(self.agent2.id)
