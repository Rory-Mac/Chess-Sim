graph = {
  '0' : ['1','2'],
  '1' : ['3'],
  '2' : ['4'],
  '3' : ['5'],
  '4' : ['6'],
  '5' : ['7'],
  '6' : ['8'],
  '7' : [],
  '8' : []
}

def bfs(graph, node): #function for BFS
  visited = [node]
  queue = [node]
  while queue:        # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(graph, '0')    # function calling