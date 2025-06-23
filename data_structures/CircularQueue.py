class CircularQueue:
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = 0
        self.rear = maxsize - 1
        self.lenght = 0

    # assistance function
    def IsEmpty(self):
        return self.lenght == 0
    
    def Isfull(self):
        return self.lenght == self.maxsize
    
    #Basic function
    def enqueue(self, val):
        if self.Isfull():
            print("Queue is full")
            return
        self.rear = (self.rear + 1)% self.maxsize
        self.queue[self.rear] = val
        self.lenght += 1

    def dequeue(self):
        if self.IsEmpty():
            print("Queueu is empty")
            return None
        val = self.queue[self.front]
        self.queue[self.front] = None 
        self.lenght -= 1
        self.front = (self.front + 1)% self.maxsize
        print(f"Done deleted value => {val}")
    
    def display(self):
        if self.IsEmpty():
            print("Queue is empty")
        print("Queue from front to rear: ")
        i = self.front
        for _ in range(self.lenght):
            print(self.queue[i])
            i = (i + 1)% self.maxsize 

    #Find the parties
    def GetFront(self):
        return None if self.IsEmpty() else self.queue[self.front]

    def GetRear(self):
        return None if self.IsEmpty() else self.queue[self.rear]

    #get size
    def GetSize(self):
        return self.lenght

    #clear function
    def __del__(self):
        del self.queue

q = CircularQueue(10)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()