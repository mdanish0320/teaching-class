class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None # 
        self.next = None # older value

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node # self.head is an older node and .prev will have the new node 
        else:
            self.tail = new_node
        self.head = new_node

    def forward_traversal(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def backward_traversal(self):
        current_node = self.tail
        while current_node:
            print(current_node.data, end=" <-> ")
            
            current_node = current_node.prev
        print("None")

# Example usage:
my_doubly_list = DoublyLinkedList()
my_doubly_list.add(1)
my_doubly_list.add(2)
my_doubly_list.add(3)
my_doubly_list.forward_traversal()  # Output: 3 <-> 2 <-> 1 <-> None
my_doubly_list.backward_traversal()  # Output: 1 <-> 2 <-> 3 <-> None
