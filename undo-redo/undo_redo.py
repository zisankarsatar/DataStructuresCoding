class UndoRedo():
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

        self.undo_stack.append('zisan')
        self.undo_stack.append('zisan karsatar')
        self.undo_stack.append('zisan karsatar caliskan')

    def append_new(self, text):
        self.undo_stack.append(text)
        
    def undo(self):
        if self.undo_stack != []:
            current = self.undo_stack.pop()
            self.redo_stack.append(current)
            print(self.undo_stack[-1])
            
    def redo(self):
        if self.redo_stack != []:
            current = self.redo_stack.pop()
            self.undo_stack.append(current)
            print(self.undo_stack[-1])

test = UndoRedo()
test.append_new('canim')
test.append_new('traveller')
test.undo() #geri almak
test.undo() #geri almak
test.undo() #geri almak
test.undo() #geri almak
test.redo()
test.redo()
test.redo()
test.redo()