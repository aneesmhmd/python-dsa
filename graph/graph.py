class Graph:
    def __init__(self):
        self.graph = {}
    
    def insert(self, vertex):
        self.graph[vertex] = []
    
    def add_edge(self, v1, v2):
        if not v1 in self.graph or not v2 in self.graph:
            return None
        self.graph[v1].append(v2)
    
    def dfs(self, start,visited):
        if start not in self.graph:
            print(f'Vertes {start} not present in graph')
            return
        if start not in visited:
            print(start)
            visited.add(start)
            for i in self.graph[start]:
                self.dfs(i, visited)
    
    def bfs(self, start, visited):
        queue = [start]
        visited.add(start)
        while queue:
            m = queue.pop(0)
            print(m, end=", ")

            if start in self.graph:
                for neighbhour in self.graph[m]:
                    if not neighbhour in visited:
                        visited.add(neighbhour)
                        queue.append(neighbhour)



graph = Graph()

nums = [1,2,3,4,5,6]
for num in nums:
    graph.insert(num)

graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(1,4)
graph.add_edge(2,6)
graph.add_edge(3,4)
graph.add_edge(4,1)
graph.add_edge(4,5)
graph.add_edge(5,3)
print(graph.graph)
graph.dfs(5,set())
graph.bfs(1,set())
# 5,3,4,1,2
# 1,2,3,4,