import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allYears=DAO.getAllYears()
        self._allTeams=DAO.getAllTeams()
        self._grafo = nx.Graph()
        self._idMapTeams = {}
        for f in self._allTeams:
            self._idMapTeams[f.ID] = f

    def addEdges(self, n):
        allEdges = DAO.getAllEdgesv1(n, self._idMapTeams)
        for a in allEdges:
            if a.id in self._grafo and a.id2 in self._grafo:
                self._grafo.add_edge(a.id, a.id2, weight=a.peso)


    def buildGraphPesato(self, n):
        self._grafo.clear()
        nodes = DAO.getAllNodes(n, self._idMapTeams)
        self._grafo.add_nodes_from(nodes)
        self.addEdges(n)

    def getNodesAnno(self, anno):
        return DAO.getAllNodes(anno, self._idMapTeams)

    def getTop5Edges(self, nodo):
        archi = []

        for vicino in self._grafo.neighbors(nodo):
            peso = self._grafo[nodo][vicino]["weight"]
            archi.append((nodo, vicino, peso))

        archi.sort(key=lambda x: x[2], reverse=True)

        return archi[:5]

    def getNumNodi(self):
        return len(self._grafo.nodes)
    def getNumArchi(self):
        return len(self._grafo.edges)