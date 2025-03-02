class DoubleLinked:
    def __init__(self) -> None:
        self.count : int = 0
        self.head: Node = None
        self.tail: Node = None
        
    def __len__(self) -> int:
        return self.count
    
    
    def __add__(self, val: any) -> None:
        self.append(val)
        
        
    # def __iter__(self):
        
    
        
    def append(self, val: any):
        n = Node(val)
        if self.count == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n #onceki node un nexti olmali  ???
            n.before = self.tail
            self.tail = n
            
            
        self.count +=1
        
    def __str__(self) -> str:
        if self.count == 0:
            return "[]"
        msg = "["
        
        current = self.head
    
        while current is not None:
            msg += "{}, ".format(current.value)
            current = current.next
        
        msg = msg.rstrip(", ")
        msg += "]"
        return msg
    
    def insert(self, position: int, val: any):
        current = self.head
        newNode = Node(val)
        
        if position >= self.count:
            self.append(val)
            return 
        
        if position <= 0:
            newNode.next = self.head
            self.head.before = newNode
            self.head = newNode
            return
            
            
        for i in range(self.count):
            if i == position:
                newNode.before = current.before
                current.before.next = newNode
                newNode.next = current
                current.before = newNode
                break
            current = current.next
    
    def delete(self, position: int):
        i = 0
        current = self.head
        
        if position == 0:
            self.head  = current.next
            current.next.before = None
            return     
        
        if position == self.count:
            self.tail = self.tail.before
            self.tail.next = None  
            return     

        while current.next is not None:
            if i == position:
                current.before.next = current.next
                current.next.before = current.before
            current = current.next
            i += 1
            
    def search(self, value: any) -> any:
        i = 0
        current = self.head
        
        while current.next is not None:
            if current.value == value:
                return "position is {}".format(i)
            current = current.next
            i += 1
        
        if self.tail.value == value:
            return "position is {}".format(self.count-1)    
        
        return 'Nothing'       
        
    def get(self, position: int):
        if position >= (self.count / 2): 
            return self.get_reverse((self.count - position + 1))
        return self.get_forward(position)
            
    def get_forward(self, position: int):
        return self.__get_item(position)
           
    def get_reverse(self, position: int):
        #print("get reverse worked  for {}".format(position))
        return self.__get_item(position, isForward=False)
    
    def __get_item(self, position: int, isForward: bool = True):
        current = self.head
        direction = current.next
        
        if not isForward:
            current = self.tail 
            direction = current.before
            
        i = 0 
        while direction is not None:
            if i == position:
                return current.value
            current = direction
            i += 1
        return None
        
class Node:
    def __init__(self, val: any) -> None:
        self.before: Node = None
        self.value: any = val
        self.next: Node = None


z = DoubleLinked()
print(len(z))
print(z)
z + 'asd'
print(z)

# for a in z:
#     print(a)
# z.append(1)
# z.append(2)
# z.append(3)
# z.append(4)
# z.append(5)
# z.append(6)
# z.append(7)
# z.insert(-77,8)


# print(z.get(1))
# # print(z.get(3))
# # print(z.get_reverse(1))

# z.delete(3)
# print(z)
# print(z.search(7))