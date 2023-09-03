n, m = list(map(int, input().split()))
all_graph = dict()

for i in range(1, n + 1):
    all_graph[i] = []

for i in range(m):
    u, v, w = list(map(int, input().split()))
    all_graph[u].append([v, w]) # [0] - vertex, [1] - weight
    all_graph[v].append([u, w]) # [0] - vertex, [1] - weight

def DFS(v, border = -1): # returns list of vertexes
    global all_graph, n, m
    touched = list(False for i in range(n + 1))
    stack = [v]
    all_touched = [v]
    touched[v] = True
    edges = set()
    while len(stack) > 0:
        v = stack.pop()
        for edge in all_graph[v]:
            edges.add(edge[1])
            if border == -1:
                u = edge[0]
                if not touched[u]:
                    touched[u] = True
                    all_touched.append(u)
                    stack.append(u)
            elif border < edge[1]:
                u = edge[0]
                if not touched[u]:
                    touched[u] = True
                    all_touched.append(u)
                    stack.append(u)
    return all_touched, list(edges)

condensate = list()
touched = list(False for i in range(n + 1))
edges = list()

for v in range(1, n + 1):
    if not touched[v]:
        mas, edge = DFS(v)
        condensate.append(mas)
        edges.append(edge)
        for i in mas:
            touched[i] = True

results = []

for i in range(len(condensate)):
    comp = condensate[i]
    edge_list = sorted(edges[i])
    count_vertexes = len(DFS(comp[0])[0])
    for w in edge_list:
        arr, _ = DFS(comp[0], w)
        if len(arr) < count_vertexes:
            results.append(w - 1)
            break
print(min(results))

