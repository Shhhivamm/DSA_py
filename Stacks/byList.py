# Implementation of Stack using a Python list

class Stack:
    def __init__(self):
        # Create an empty list to store stack elements
        self.items = []

    def is_empty(self):
        # Return True if the stack contains no elements
        return len(self.items) == 0

    def push(self, item):
        # Add an element to the top of the stack
        self.items.append(item)

    def pop(self):
        # Check if the stack is empty before removing an element
        if len(self.items) == 0:
            return "Cannot be popped, stack is empty"

        # Remove and return the top element
        x = self.items.pop()
        return x

    def top(self):
        # Check if the stack is empty before accessing the top element
        if len(self.items) == 0:
            return "Cannot be topped, stack is empty"

        # Return the top element without removing it
        return self.items[-1]

    def size(self):
        # Return the number of elements currently in the stack
        return len(self.items)
    
    def __str__(self):
        #Used to print the stack content
        return str(self.items)
    
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print(f"Stack Content= {stack}")
print(f"Poped Item= {stack.pop()}")
print(f"Top item at after popping= {stack.top()}")
print(f"Stack is empty= {stack.is_empty()}")
print(f"Size of stack = {stack.size()}")

