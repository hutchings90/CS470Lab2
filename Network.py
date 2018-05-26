from Agent import Agent
from Edge import Edge

class Network:
    def __init__(self, agents, edges):
        self.agents = agents
        self.edges = edges
        self.setNeighbors()

    def setNeighbors(self):
        for edge in self.edges:
            edge.agent1.addNeighbor(edge.agent2)
            edge.agent2.addNeighbor(edge.agent1)

    def __str__(self):
        string = '------------------------------ Network ------------------------------\n'
        string += '-- Agents (' + str(len(self.agents)) + ') ----------------------------------\n'
        for agent in self.agents:
            string += str(agent) + '\n\n'
        string += '\n-- Edges (' + str(len(self.edges)) + ') ------------------------------------\n'
        for edge in self.edges:
            string += str(edge) + ', '
        return string

def makeOneCycle():
    agents = []
    for i in range(7):
        agents.append(Agent(i))
    edges = [
        Edge(agents[0], agents[1]),
        Edge(agents[1], agents[2]),
        Edge(agents[2], agents[3]),
        Edge(agents[3], agents[4]),
        Edge(agents[4], agents[5]),
        Edge(agents[5], agents[6]),
        Edge(agents[6], agents[0])
    ]
    return Network(agents, edges)

def makeTwoCycle():
    agents = []
    for i in range(7):
        agents.append(Agent(i))
    edges = [
        Edge(agents[0], agents[1]),
        Edge(agents[0], agents[2]),
        Edge(agents[0], agents[5]),
        Edge(agents[0], agents[6]),
        Edge(agents[1], agents[2]),
        Edge(agents[1], agents[3]),
        Edge(agents[1], agents[6]),
        Edge(agents[2], agents[3]),
        Edge(agents[2], agents[4]),
        Edge(agents[3], agents[4]),
        Edge(agents[3], agents[5]),
        Edge(agents[4], agents[5]),
        Edge(agents[4], agents[6]),
        Edge(agents[5], agents[6]),
    ]
    return Network(agents, edges)

def makeComplete():
    agents = []
    for i in range(7):
        agents.append(Agent(i))
    edges = []
    for i in range(7):
        for j in range(i + 1, 7):
            edges.append(Edge(agents[i], agents[j]))
    return Network(agents, edges)

def makeAdHoc():
    agents = []
    for i in range(17):
        agents.append(Agent(i))
    edges = [
        Edge(agents[0], agents[1]),
        Edge(agents[0], agents[2]),
        Edge(agents[1], agents[2]),
        Edge(agents[2], agents[4]),
        Edge(agents[4], agents[3]),
        Edge(agents[3], agents[8]),
        Edge(agents[3], agents[9]),
        Edge(agents[4], agents[5]),
        Edge(agents[5], agents[9]),
        Edge(agents[9], agents[8]),
        Edge(agents[5], agents[6]),
        Edge(agents[9], agents[6]),
        Edge(agents[9], agents[7]),
        Edge(agents[6], agents[7]),
        Edge(agents[7], agents[8]),
        Edge(agents[7], agents[13]),
        Edge(agents[5], agents[10]),
        Edge(agents[6], agents[11]),
        Edge(agents[10], agents[11]),
        Edge(agents[11], agents[12]),
        Edge(agents[12], agents[13]),
        Edge(agents[13], agents[16]),
        Edge(agents[12], agents[16]),
        Edge(agents[15], agents[16]),
        Edge(agents[12], agents[15]),
        Edge(agents[11], agents[15]),
        Edge(agents[14], agents[15]),
        Edge(agents[11], agents[14]),
        Edge(agents[10], agents[14]),
    ]
    return Network(agents, edges)
