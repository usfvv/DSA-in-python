class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def insert_first(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node

    def insert_last(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, val, position):
        new_node = Node(val)
        if position < 0 or self.is_empty():
            self.insert_first(val)
            return 
        current = self.head
        count = 0
        while current.next and count < position - 1:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def display(self):
        if self.is_empty():
            print("List is empty")
            return 
        current = self.head
        print("Linked list: ", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


l = SinglyLinkedList()

l.insert_last(10)
l.insert_last(30)

l.insert_at_position(20,1)

l.insert_last(40)

l.insert_first(0)

l.display()