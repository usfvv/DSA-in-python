class Node :
    def __init__(self, value):
        self.val = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        NewNode = Node(value)
        NewNode.next = self.top
        self.top = NewNode

    def pop(self):
        if not self.top:
            print("stack is empty")
        popped = self.top.val
        self.top = self.top.next
        print("Deleted value : ", popped)
        return popped
    
    def display(self):
        if self.IsEmpty():
            print("Stack is empty")
        else:
            current = self.top
            while current:
                print(current.val)
                current = current.next

    def IsEmpty(self):
        return self.top is None
    
    def peek(self):
        if self.IsEmpty():
            print("Stack is empty") 
        else:
            print(self.top.val)

    def size(self):
        count = 0
        current = self.top
        while current :
            count += 1
            current = current.next
        return count