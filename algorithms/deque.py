class Deque():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        # add in front
        self.items.append(item)
        
    def addRear(self, item):
        # add in rare
        self.items.insert(0, item)
        
    def removeFront(self):
        # remove from front
        return self.items.pop()
        
    def removeRare(self):
        # remove from rare
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def getFirstItem(self):
        return self.items[0]
    
    def getItems(self):
        return self.items
    
d = Deque()
d.addFront('zis')
d.addFront('abd')
d.addRear('fat')
print(d.getItems())
print(d.size())
d.removeRare()
d.removeRare()
print(d.size())
print(d.getItems())