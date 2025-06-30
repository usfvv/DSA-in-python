class Node:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node :
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_right(self, y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        y.hight = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.hight = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x
    
    def rotate_left(self, x):
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key :
            root.left = self.insert(root.left, key)
        else :
            root.right = self.insert(root.right, key)
        root.hight = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balace = self.get_balance(root)
        #LL
        if balace > 1 and key < root.left.key:
            return self.rotate_right(root)
        #RR
        if balace < -1 and key > root.right.key:
            return self.rotate_left(root)
        #LR
        if balace > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        #RL
        if balace < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root
    
    def in_order(self, root):
        if root :
            self.in_order(root.left)
            print(root.key, end=" ")
            self.in_order(root.right)

tree = AVLTree()
root = None
for val in [10, 20, 30, 40, 50, 25]:
    root = tree.insert(root, val)

print("In-order Traversal:")
tree.in_order(root)