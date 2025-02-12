class Stack():
    def __init__(self):
        self.items = []
        
    #pop len push, top 
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        #stak e eleman ekler
        self.items.append(item)
    
    def pop(self):
        #stack icindeki en son elemani siler
        return self.items.pop()
    
    def top(self):
        #stck icindeki son eleman
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
s = Stack()

s.push('Zis')
s.push('Abd')
print(s.isEmpty())
print(s.top())
print(s.top())
print(s.size())
print(s.pop())
print(s.size())