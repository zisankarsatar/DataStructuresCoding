class Queue:
    def __init__(self):
        self.items = []
        
    #size getitem add delete
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        #first IN - last OUT
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def getFirstItem(self):
        return self.items[0]
    
    def getLastItem(self):
        return self.items[len(self.items)-1]
    
q = Queue()

print(q.isEmpty())
q.enqueue('zis')
q.enqueue('abd')
print(q.size())
print(q.getFirstItem())
print(q.getLastItem())
q.dequeue()
print(q.getLastItem())
