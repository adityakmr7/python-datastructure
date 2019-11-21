class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
        
    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

myStack = Stack()
print(myStack.is_empty())
myStack.push("Book A")
myStack.push("Book B")
myStack.push("Book C")
print(myStack.peek())
print(myStack.get_stack())
print(myStack.is_empty())

        





