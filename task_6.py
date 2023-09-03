n, m = list(map(int, input().split()))

dsu = list(i for i in range(n + 1))
rank = list(0 for i in range(n + 1))
count_list = list(1 for i in range(n + 1))

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
    for vert in range(1, n + 1):
        if CheckSame(vert, root_u) or CheckSame(vert, root_v):
            count_list[vert] += 1

    if rank[root_u] == rank[root_v]:
        rank[root_u] += 1
        dsu[root_v] = root_u
        return root_u
    if rank[root_u] < rank[root_v]:
        dsu[root_u] = root_v
        return root_u
    dsu[root_v] = root_u
    return root_v

def Count(v):
    return count_list[v]

for iter in range(m):
    inp = list(map(int, input().split()))
    command = inp[0]
    if command == 1:
        Union(inp[1], inp[2])
    elif command == 2:
        if CheckSame(inp[1], inp[2]):
            print('YES')
        else:
            print('NO')
    elif command == 3:
        print(Count(inp[1]))

