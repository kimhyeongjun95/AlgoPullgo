# 백준 1197 최소 스패닝 트리

def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    
    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if rank[root_x] >= rank[root_y]:
        parents[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1
    else:
        parents[root_x] = root_y


def kruskal():
    total = 0

    for a, b, w in edges:
        if find_set(a) != find_set(b):
            total += w
            union(a, b)

    return total


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

parents = [x for x in range(V+1)]
rank = [0 for _ in range(V+1)]

print(kruskal())