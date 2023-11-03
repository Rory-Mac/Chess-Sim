class Graph():
    # initialise graph of size 'size' with edges stored as tuple list [(v, w), ... ] for vertices v and w
    def __init__(self, size, edges):
        self.size = size
        self.adjacency_lists = [[] for _ in range(size)]
        for edge in edges:
            self.insertEdge(edge)

    def insertEdge(self, edge):
        v, w = edge[0], edge[1]
        self.adjacency_lists[v].append(w)

    def removeEdge(self, edge):
        v, w = edge[0], edge[1]
        self.adjacency_lists[v].remove(w)

    # return array of values in order of a breadth first traversal
    def bfs(self, v):
        results = []
        stack = []
        visited = [False for _ in range(self.size)]
        stack.append(v)
        while stack:
            v = stack.pop(0)
            visited[v] = True
            results.append(v)
            for w in self.adjacency_lists[v]:
                if not visited[w]:
                    stack.append(w)
        return results

    # return array of values in order of a depth first traversal
    def dfs(self, v):
        results = []
        stack = []
        visited = [False for _ in range(self.size)]
        stack.append(v)
        while stack:
            v = stack.pop()
            visited[v] = True
            results.append(v)
            for w in self.adjacency_lists[v]:
                if not visited[w]:
                    stack.append(w)
        return results
    
if __name__ == "__main__":
    size = 10
    #graph_edges = [(0,1),(0,2),(2,3),(2,4),(4,5),(4,6)]
    graph_edges = [(0,1),(0,2),(1,3),(2,4),(3,5),(4,6),(5,7),(6,8)]
    graph = Graph(size, graph_edges)
    print("BFS: ", end="")
    for item in graph.bfs(0):
        print(f"{item} ", end="")
    print("\nDFS: ", end="")
    for item in graph.dfs(0):
        print(f"{item} ", end="")
    print()