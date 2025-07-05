class hashTableChaining:
    def __init__(self, size = 100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def fixed_hash(self, key):
        return sum(ord(char) for char in key)

    def insert(self, key, value):
        # idx = self.fixed_hash(key) % self.size
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[idx].append([key, value])

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i} : {bucket}")

htc = hashTableChaining(10)

htc.insert("yousef", 1)
htc.insert("abdo", 2)
htc.insert("aiten", 3)
htc.insert("youesf", 1)

htc.display()