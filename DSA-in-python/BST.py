class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            return Node(val)
        if val < root.data:
            root.left = self.insert(root.left, val)
        elif val > root.data :
            root.right = self.insert(root.right, val)
        return root

    def search(self, root, key):
        if root is None or  root.data == key :
            return root 
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
        
    def find_min(self, root):
        curr = root 
        while curr and curr.left :
            curr = curr.left
        return curr

    def find_max(self, root):
        curr =  root 
        while curr and curr.right :
            curr =  curr.right
        return curr

    def delete(self, root,  key):
        if root is None :
            return root 
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data :
            root.right = self.delete(root.right, key)
        else :
            if root.left is None:
                return root.right
            elif root.right is None :
                return root.left
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root
    
    def in_order(self, root):
        if root :
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

    def find_successor(self, root, key):
        target = self.search(root, key)
        if target is None:
            return None
        if target.right :
            return self.find_min(target.right)
        successor = None
        current = root 
        while current :
            if key < current.data :
                successor = current 
                current = current.left
            elif key > current.data:
                current = current.right 
            else:
                break
        return successor
    
    def find_predecessor(self, root, key):
        target = self.search(root, key)
        if target is None:
            return None
        if target.right :
            return self.find_max(target.left)
        predecessor = None
        current = root 
        while current :
            if key > current.data:
                predecessor = current
                current = current.right
            elif key < current.data:
                current = current.left
            else :
                break
        return predecessor
    
tree = BST()
r = None
for val in [20, 10, 30, 5, 15, 25, 35]:
    r = tree.insert(r, val)

print("In-order Traversal:")
tree.in_order(r)  # 5 10 15 20 25 30 35

print("\nSearch 25:", "Found" if tree.search(r, 25) else "Not found")#Search 25: Found

print("Min:", tree.find_min(r).data)#Min: 5
print("Max:", tree.find_max(r).data)#Max: 35

succ = tree.find_successor(r, 15)
pred = tree.find_predecessor(r, 15)
print("Successor of 15:", succ.data if succ else "None")  #Successor of 15: 20
print("Predecessor of 15:", pred.data if pred else "None")#Predecessor of 15: 10

r = tree.delete(r, 20)
print("In-order after deleting 20:") #In-order after deleting 20:
tree.in_order(r)                     #5 10 15 25 30 35 
