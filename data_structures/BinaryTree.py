from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.left is None:
                curr.left = new_node
                return
            else:
                queue.append(curr.left)
            if curr.right is None:
                curr.right = new_node
                return
            else:
                queue.append(curr.right)

    def pre_order(self, node):
        if node :
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")

    def level_order(self):
        if not self.root:
            return 
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            print(curr.data, end=" ")
            if curr.left :
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)

print("Pre-order:")
bt.pre_order(bt.root)  #1 2 4 5 3 

print("\nIn-order:")
bt.in_order(bt.root)   #4 2 5 1 3 

print("\nPost-order:")
bt.post_order(bt.root) #4 5 2 3 1 

print("\nLevel-order:")
bt.level_order()      #1 2 3 4 5 