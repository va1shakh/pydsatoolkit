class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def display(self):
        print(self.stack)
        
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.display()
