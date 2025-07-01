class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0 
    
    def get_length(self):
        return self.length
    
    def insert_first(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert_last(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def insert_at_position(self, pos, val): 
        if (pos < 0 or pos > self.length):  
            print("Index out of range")     
            return                          
        if pos == self.length:              
            self.insert_last(val)           
        elif pos == 0:                      
            self.insert_first(val)          
        else:                               
            current = self.head             
            for _ in range(pos - 1):        
                current = current.next      
            new_node = Node(val)            
            new_node.next = current.next    
            new_node.prev = current         
            current.next.prev = new_node    
            current.next = new_node         
            self.length += 1                

    def remove_first(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

    def remove_last(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.head == self.tail :
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

    def remove_at_position(self, pos):
        if self.is_empty():
            print("List is empty")
            return
        if (pos < 0 or pos >= self.length):
            print("Index out of range")
            return
        if pos == 0 :
            self.remove_first()
        elif pos == self.length - 1 :
            self.remove_last()
        else:
            current = self.head             
            for _ in range(pos):        
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.length -= 1
    
    def reverse(self):
        current = self.head
        prev_node = None
        while current is not None:
            current.prev, current.next = current.next, current.prev
            prev_node = current
            current = current.prev
        # Swap head and tail
        self.head, self.tail = self.tail, self.head

    def search(self, val):
        current = self.head
        index = 0
        while current:
            if current.data == val:
                return index
            current = current.next
            index += 1
        return -1
    
    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        print("Linked list : ", end="None <-> ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


dll = DoublyLinkedList()

dll.insert_first(40)
dll.insert_first(30)
dll.insert_first(20)
dll.insert_first(10)

dll.display()          #Linked list : None <-> 10 <-> 20 <-> 30 <-> 40 <-> None

dll.reverse()

dll.display()          #Linked list : None <-> 40 <-> 30 <-> 20 <-> 10 <-> None

print(dll.search(60))  #-1
