class UndoRedo():
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

        # self.undo_stack.append('zisan')
        # self.undo_stack.append('zisan karsatar')
        # self.undo_stack.append('zisan karsatar caliskan')

    def append_new(self, text):
        self.undo_stack.append(text)
        
    def undo(self):
        if self.undo_stack != []:
            current = self.undo_stack.pop()
            self.redo_stack.append(current)
            print(self.undo_stack[-1])
        else:
            print('finished')
        
    def redo(self):
        if self.redo_stack != []:
            current = self.redo_stack.pop()
            self.undo_stack.append(current)
            print(self.undo_stack[-1])
        else:
            print('finished')

test = UndoRedo()
text = input('Pls write something: ')
test.append_new(text)
text = input('Pls write something: ')
test.append_new(text)
text = input('Pls write something: ')
test.append_new(text)

step = input('Undo or Redo(u/r):' )
if step == 'u':
    test.undo() #geri almak
else:
   test.redo()     