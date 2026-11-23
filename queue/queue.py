# implementing Queue using list
# O(n) linear time complexity
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
#display before removing 
my_queue.display()
my_queue.dequeue()
#display after remvoing
my_queue.display()