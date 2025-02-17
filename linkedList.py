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


class linkedList(object):
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        
        new_node.nextNode = self.head
        
        self.head = new_node
        
    def insertAfter(self,prev_node, new_data):
        
        #prev node var mi ?
        if prev_node is None:
            print('boyle bi data yok')
            return
    
        # yeni node yarat ve icine yerlestir
        new_node = Node(new_data)
        
        # new_node next in prev yap
        new_node.nextNode = prev_node.nextNode
        
        #prev node nextin new node yap
        prev_node.nextNode = new_node
        
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.nextNode
            
linked_list = linkedList() 
linked_list.push('son eleman')
linked_list.push(25)
linked_list.push(15)
linked_list.push(5)
linked_list.push('ilk eleman')

linked_list.printLinkedList()

linked_list.insertAfter(linked_list.head.nextNode, 35)
linked_list.insertAfter(linked_list.head, 45)

linked_list.printLinkedList()