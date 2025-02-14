class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        
    def setNextNode(self, node):
        self.nextNode = node
    
    def getNextNode(self):
        return self.nextNode
    
    def getNodeValue(self):
        return self.value
    

istanbul = Node('34')
kmaras = Node('46')
mugla = Node('48')

istanbul.setNextNode(kmaras)
kmaras.setNextNode(mugla)

print(istanbul.getNodeValue())
print(istanbul.nextNode.getNodeValue())
print(kmaras.nextNode.getNodeValue())
print(kmaras.getNodeValue())
print(mugla.getNodeValue())