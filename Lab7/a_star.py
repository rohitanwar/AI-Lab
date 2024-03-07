# Implement A* algorithm to find shortest path in graph

def A_star(graph,heuristics,start,end):
    # Return the shortest path from start to end using A* algorithm
    open_list = [start]
    closed_list = []
    g = [float('inf')]*len(graph)
    g[start] = 0
    f = [float('inf')]*len(graph)
    f[start] = heuristics[start]
    parent = [None]*len(graph)
    while open_list:
        current = open_list[0]
        for i in open_list:
            if f[i] < f[current]:
                current = i
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        open_list.remove(current)
        closed_list.append(current)
        for i in range(len(graph[current])):
            if graph[current][i] != 0 and i not in closed_list:
                if i not in open_list:
                    open_list.append(i)
                if g[current] + graph[current][i] < g[i]:
                    parent[i] = current
                    g[i] = g[current] + graph[current][i]
                    f[i] = g[i] + heuristics[i]
    return None

nodes = ['A','B','C','D','E','F','G','H','I','J']
heuristics = [10, 8, 5, 7, 3, 6, 5, 3, 1, 0]
graph = [
    [0,6,0,0,0,3,0,0,0,0], #A
    [6,0,3,2,0,0,0,0,0,0], #B
    [0,3,0,1,5,0,0,0,0,0], #C
    [0,2,1,0,8,0,0,0,0,0], #D
    [0,0,5,8,0,0,0,0,5,5], #E
    [3,0,0,0,0,0,1,7,0,0], #F
    [0,0,0,0,0,1,0,0,3,0], #G
    [0,0,0,0,0,7,0,0,2,0], #H
    [0,0,0,0,5,0,3,2,0,3], #I
    [0,0,0,0,5,0,0,0,3,0]  #J
]

print(list(map(lambda x: nodes[x], A_star(graph,heuristics,0,9))))
