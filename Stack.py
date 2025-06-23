class Stack:
    def __init__(self, maxsize = 100):
        self.stack = [None] * maxsize
        self.MAXSIZE = maxsize
        self.top = -1

    def push(self, element):
        if self.top >= self.MAXSIZE -1 :
            return "Stack is full"
        else:
            self.top += 1
            self.stack[self.top] = element

    def pop(self):
        if not self.IsEmpty():
            self.stack.pop()
            self.top -= 1
        else:
            return "Stack is empty"       

    def peek(self):
        return self.stack[self.top]
    
    def display(self):
        if self.IsEmpty():
            return "Stack is empty"
        else:
            for i in range(self.top, -1 , -1):
                print(f"[{i}] => {self.stack[i]}")
    
    def IsEmpty(self):
        return self.top == -1
    
    def size(self):
        return self.top +1