class LinkedList:
    def __init__(self, items: list = []) -> None:
        self.count: int = 0
        self.head: Node = None
        self.tail: Node = None
    
    def append(self, val: any):
        n = Node(val)
        if self.count == 0:
            self.head = n 
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.count += 1
        
    def __str__(self) -> str:
        if self.count == 0:
            return "[]"
        msg = "["
        current = self.head 
        while current is not None:
            msg += "{}, ".format(current.val)
            current = current.next
        
        msg = msg.rstrip(", ")
        msg += "]"
        return msg
          
class Node:
    def __init__(self, val: any) -> None:
        self.val: any = val
        self.next: Node = None
    
l = LinkedList()
l.append(1)
l.append(2)
print(l)

print(l.count)