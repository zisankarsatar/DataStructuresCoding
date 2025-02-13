#Stack Queue Deque
def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)
    
def pop(stack):
    return stack.pop()


#reverse word
def reverse(string):
    n = len(string)
    
    stack1 = createStack()
    
    for i in range(n):
        push(stack1, string[i]) # 'd', 'a', 't', 'a', 'i'
    
    reverse_string=''
    #pop
    for i in range(n):
        reverse_string += pop(stack1)
        
    return reverse_string

print(reverse('zisan'))
print(reverse('abdullah'))
print(reverse('deep learning'))
        
        
    

