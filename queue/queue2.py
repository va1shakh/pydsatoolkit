#implementing Queue using deque module
# O(1) constant time complexity
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()
    def display(self):
        print(self.queue)

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.display()
my_queue.dequeue()
#display after removing
my_queue.display()