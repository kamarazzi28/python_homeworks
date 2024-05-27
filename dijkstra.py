class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None

    def add_edge(self, edge):
        self.edges.append(edge)


class Dijkstra:
    def __init__(self):
        self.bases = []

    def createGraph(self, vertexes, edgesToVertexes):
        self.bases = vertexes

        for edge in edgesToVertexes:
            base_vertex = next(vertex for vertex in vertexes if vertex.id == edge.source)
            base_vertex.add_edge(edge)

    def getVertexes(self):
        return self.bases

    def computePath(self, sourceId):
        base_node = next(node for node in self.bases if node.id == sourceId)
        base_node.minDistance = 0

        unvisit_nodes = set(self.bases)

        while unvisit_nodes:
            ongoing_node = min(unvisit_nodes, key=lambda node: node.minDistance)

            unvisit_nodes.remove(ongoing_node)

            for edge in ongoing_node.edges:
                neighbor_node = next(node for node in self.bases if node.id == edge.target)
                new_distance = ongoing_node.minDistance + edge.weight

                if new_distance < neighbor_node.minDistance:
                    neighbor_node.minDistance = new_distance
                    neighbor_node.previousVertex = ongoing_node

    def getShortestPathTo(self, targetId):
        target_node = next(node for node in self.bases if node.id == targetId)
        path = []

        while target_node:
            path.insert(0, target_node)
            target_node = target_node.previousVertex

        return path

    def resetDijkstra(self):
        for node in self.bases:
            node.minDistance = float('inf')
            node.previousVertex = None
