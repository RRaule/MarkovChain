class Graph:

    nodeList = []

    def __init__(self, name):
        self.name = name

    def addNode(self, node):
        self.nodeList.append(node)

    def removeNode(self,node):
        self.nodeList.remove(node)

    def returnNodes(self):
        return self.nodeList

class Node:

    connections = {}

    def __init__(self,name):
        self.name = name

    def addConntection(self, node, weight):
        self.connections[node] = weight

    def removeConnection(self):

    def returnConnections(self):



class Transition:
    def __init__(self):
        pass

