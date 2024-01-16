from collections import deque

class FIFOQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage for FIFOQueue
fifo_queue = FIFOQueue()
fifo_queue.enqueue(1)
fifo_queue.enqueue(2)
fifo_queue.enqueue(3)

print("Dequeue:", fifo_queue.dequeue())  # Output: 1
print("Dequeue:", fifo_queue.dequeue())  # Output: 2
print("Size:", fifo_queue.size())        # Output: 1
