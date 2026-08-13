# Implementation of Queue using a Python list

class Queue:
    def __init__(self):
        # Create an empty list to store queue elements
        self.items = []
        
    def isempty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        # Add an element to the REAR of the queue
        self.items.append(item)

    def dequeue(self):
        # Check if the queue is empty before removing an element
        if len(self.items) == 0:
            return "Dequeue from empty queue"

        # Remove and return the element from the FRONT
        x = self.items.pop(0)
        return x

    def front(self):
        # Check if the queue is empty
        if len(self.items) == 0:
            return "Queue is empty"

        # Return the FRONT element without removing it
        return self.items[0]

    def rear(self):
        # Check if the queue is empty
        if len(self.items) == 0:
            return "Queue is empty"

        # Return the REAR element without removing it
        return self.items[-1]

    def size(self):
        # Return the number of elements in the queue
        return len(self.items)
    
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)

print(f"Queue is empty: {q.isempty()}")
print(f"Element at the fornt of queue: {q.front()}")
print(f"Element at the rear of queue: {q.rear()}")
print("content of queue:", q.items)
print(f"Dequeuing: {q.dequeue()}")
print("content of queue:", q.items)
print(f"Dequeuing: {q.dequeue()}")
print(f"Dequeuing: {q.dequeue()}")
print("content of queue:", q.items)
print(f"Size of the queue: {q.size()}")
print(f"Dequeuing: {q.dequeue()}")
print(f"Queue is empty: {q.isempty()}")