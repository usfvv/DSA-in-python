class GraphList:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def display(self):
        for node in self.graph:
            print(f"{node} --> {self.graph[node]}")

a = GraphList()

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