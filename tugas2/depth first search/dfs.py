# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C','D'],
    'B' : ['E', 'F'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'B')