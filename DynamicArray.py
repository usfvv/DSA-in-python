class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.data = [None] * self.capacity

    def size(self):
        return self.length
    
    def is_empty(self):
        return self.length == 0
    
    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, item):
        if self.length == self.capacity :
            self._resize(2 * self.capacity)
        self.data[self.length] = item
        self.length += 1

    def get(self, index):
        if not (0 <= index < self.length):
            raise IndexError("Index out of range")
        return self.data[index]
    
    def set(self, index, item):
        if not (0 <= index < self.length):
            raise IndexError("Index out of range")
        self.data[index] = item 

    def remove(self, index):
        if not (0 <= index < self.length):
            raise IndexError("Index out of range")
        removed = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.length - 1] = None
        self.length -= 1
        return removed
    
    def __str__(self):
        return "["+", ".join(repr(self.data[i]) for i in range(self.length)) + "]"