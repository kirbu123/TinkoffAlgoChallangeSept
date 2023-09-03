n, m = list(map(int, input().split()))
edges = list()

for i in range(m):
    u, v, w = list(map(int, input().split()))
    edges.append([u, v, w])
    edges.append([v, u, w])

dsu = list(i for i in range(n + 1))
rank = list(0 for i in range(n + 1))

def FindSet(v):
    if dsu[v] == v:
        return v
    dsu[v] = FindSet(dsu[v])
    return dsu[v]

def CheckSame(u, v):
    return FindSet(u) == FindSet(v)


def Union(u, v):
    root_u, root_v = FindSet(u), FindSet(v)
    if root_u == root_v:
        return root_u
    if rank[root_u] == rank[root_v]:
        rank[root_u] += 1
        dsu[root_v] = root_u
        return root_u
    if rank[root_u] < rank[root_v]:
        dsu[root_u] = root_v
        return root_u
    dsu[root_v] = root_u
    return root_v

edges = sorted(edges, key=lambda x: x[-1], reverse=True)

results = []

for edge in edges:
    if not CheckSame(edge[0], edge[1]):
        Union(edge[0], edge[1])
        results.append(edge[2] - 1)

print(min(results))