class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, val):
        new_node = Node(val)
        if self.rear is None :
            self.front = self.rear = new_node
        else :
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        val = self.front.data
        self.front = self.front.next
        if self.front is None :
            self.raer = None
        print(f"Deleted value :{val}")
        return val

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return 
        print("Queue from front to rear: ")
        current = self.front
        while current:
            print(current.data)
            current = current.next
        print("None")

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data


q = LinkedQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek()) #10

print("#" * 10)

q.dequeue()

q.enqueue(40)
q.enqueue(50)

q.display()   # 20 30 40 50