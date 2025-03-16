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

g = Graph()

g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)

g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(1,3)
g.addEdge(2,5)
g.addEdge(5,7)
g.addEdge(3,6)
g.addEdge(2,4)


# for v in g:
#     print(v)
    
# print(g.getVertex(1))


graph = { "A" : set(["B", "C"]),
        "B" : set(["A","D","E"]),
        "C" : set(["A","F"]),
        "D" : set(["B"]),
        "E" : set(["B", "F"]),
        "F" : set(["C", "E"]),
        }

#print(graph)
#Deepth First Search
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
        print(visited)
    return visited

#print(dfs(graph, "A"))

#Breadth First Search 
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
        print(visited)
    return visited

#bfs(graph, "A")

def vertexCoverting(a):
    vertices = a[2][1:-1].split(',')
    graph = a[1][1:-1].split(',')
    failed = []
    
    if len(vertices[0]) == 0:
        return a[1]

    for i in graph:
        flag = True
        for x in vertices:
            if x in i:
                flag = False
        if flag:
            failed.append(i)   
    if len(failed) > 0:
        return "(" + ",".join(failed) + ")"
    return "yes" 

#result = vertexCoverting(["(A,B,C,D)","(A-B,A-D,B-D,A-C)", "(A,B)"])
#result2 = vertexCoverting(["(A,B,C,D)","(A-B,A-D,B-D,A-C)", "(C)"])
#result3 = vertexCoverting(["(A,B,C,D)","(A-B,A-D,B-D,A-C)", "(C,B)"])
result4 = vertexCoverting(["(A,B,C,D)","(A-B,A-D,B-D,A-C)", "(A)"])
print(result4)