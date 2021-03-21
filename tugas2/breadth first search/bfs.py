graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []
found = []
x = input("Enter element for search:")


def bfs(visited, graph, node, x):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        if s == x:
            found.append(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited, graph, 'A', x)

if not found:
    print("Element not found")
else:
    print(found)
    print("Element found")