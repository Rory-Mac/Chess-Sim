class Graph:
    def __init__(self, size, edges):
        self.size = size
        self.adjacency_lists = {}
        for i in range(size):
            self.adjacency_lists[i] = [] 
        for edge in edges:
            self.insertEdge(edge)
            
    def insertEdge(self, edge):
        v, w = edge[0], edge[1]
        self.adjacency_lists[v].append(w)

    def removeEdge(self, edge):
        v, w = edge[0], edge[1]
        self.adjacency_lists[v].remove(w)
    
    def bfs(self, v):
        discovered = []
        queue = []
        visited = [False for _ in range(self.size)]
        queue.append(v)
        while queue:
            v = queue.pop(0)
            discovered.append(v)
            for w in self.adjacency_lists[v]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
        return discovered
    
    def dfs(self, v):
        discovered = []
        queue = []
        visited = [False for _ in range(self.size)]
        queue.append(v)
        while queue:
            v = queue.pop()
            discovered.append(v)
            for w in self.adjacency_lists[v]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
        return discovered

if __name__ == "__main__":
    size = 7
    #graph_edges = [(0,1),(0,2),(2,3),(2,4),(4,5),(4,6)]
    #graph_edges = [(0,1),(0,2),(1,3),(2,4),(3,5),(4,6),(5,7),(6,8)]
    #graph_edges = [(0,1),(0,2),(1,12),(2,3),(2,4),(3,4),(4,5),(4,6),(4,7),(5,8),(6,9),(7,10),(8,11),(9,11),(10,11),(11,12)]
    graph_edges = [(0,1),(0,2),(1,2),(2,1),(1,4),(4,1),(2,3),(3,2),(3,6),(6,3),(4,5),(5,4),(5,6),(6,5)]
    graph = Graph(size, graph_edges)
    print("BFS: ", end="")
    for item in graph.bfs(0):
        print(f"{item} ", end="")
    print("\nDFS: ", end="")
    for item in graph.dfs(0):
        print(f"{item} ", end="")
    print()