class Node:
    def __init__(self, data):
        self.data = data # current data
        self.next = None # older data

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.display()  # Output: 3 -> 2 -> 1 -> None


# drawback
# 1. Random Access Time (search capability): requires traversing the list from the head or tail, resulting in O(n) time complexity
# 2. Memory Overhead: Linked lists require additional memory for storing pointers/references along with the actual data