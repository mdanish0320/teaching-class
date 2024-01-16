from collections import deque

class LIFOStack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage for LIFOStack
lifo_stack = LIFOStack()
lifo_stack.push(1)
lifo_stack.push(2)
lifo_stack.push(3)

print("Pop:", lifo_stack.pop())  # Output: 3
print("Pop:", lifo_stack.pop())  # Output: 2
print("Size:", lifo_stack.size())  # Output: 1
