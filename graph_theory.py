class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
    def addNeighbor(self, neighbor, weight = 0):
        self.connectedTo[neighbor] = weight
    
    def __str__(self):
        return str(self.id) + "connected to " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        newVertx = Vertex(key)
        self.vertList[key] = newVertx
        self.numVertices += 1
        return newVertx
   
    def getVertex(self, n):
        if n is self.vertList:
           return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
#addVertex(vert) -> graph icerisine node(vertex) ekler
#addEdge(fromVert, toVert) -> iki node birbinine baglayan directed edge ekler 
#addEdge(fromVert, toVert, weight) -> iki node birbinine baglayan weighted and directed edge ekler 
#getVertex(vertexKey) -> graph icerisinde node bulur
#getVertices() -> node lari return eder 

