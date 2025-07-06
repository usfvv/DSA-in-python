import numpy as np

class GrapghMatrix:
    def __init__(self, node):
        self.node = node
        self.size = len(node)
        self.node_index = {node : i for i, node in enumerate(node)}
        self.matrix = np.zeros((self.size, self.size), dtype=int)

    def add_edge(self, u, v):
        i = self.node_index[u]
        j = self.node_index[v]
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def display(self):
        print("  ", " ".join(self.node))
        for i, node in enumerate(self.node):
            row = " ".join(map(str, self.matrix[i]))
            print(f"{node}: {row}")

nodes = ["A", "B", "C", "D", "E"]

a = GrapghMatrix(nodes)

a.add_edge("A", "B")
a.add_edge("A", "C")
a.add_edge("B", "A")
a.add_edge("B", "D")
a.add_edge("B", "E")
a.add_edge("C", "A")
a.add_edge("C", "D")
a.add_edge("D", "C")
a.add_edge("D", "B")
a.add_edge("D", "E")
a.add_edge("E", "B")
a.add_edge("E", "D")

a.display()     #A --> ['B', 'C', 'B', 'C']
                #B --> ['A', 'A', 'D', 'E', 'D', 'E']
                #C --> ['A', 'A', 'D', 'D']
                #D --> ['B', 'C', 'C', 'B', 'E', 'E']
                #E --> ['B', 'D', 'B', 'D']