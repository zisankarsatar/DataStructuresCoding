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

class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None
    
    def setNextNode(self, node):
        self.nextNode = node
    
    def getNextNode(self):
        return self.nextNode
    
    def setPrevNode(self, node):
        self.prevNode = node
    
    def getPrevNode(self):
        return self.prevNode
    
    def getNodeValue(self):
        return self.value
    
netherlands = DoublyLinkedListNode('ams')
belgium = DoublyLinkedListNode('brussel')
germany = DoublyLinkedListNode('berliin')

netherlands.setNextNode(belgium)
belgium.setPrevNode(netherlands)
belgium.setNextNode(germany)
germany.setPrevNode(belgium)

print(netherlands.getNodeValue())
print(belgium.getNextNode().getNodeValue())
print(germany.getPrevNode().getPrevNode().getNodeValue())