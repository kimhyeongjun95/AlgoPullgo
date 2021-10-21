import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y

        if ranks[root_x] == ranks[root_y]:
            ranks[root_y] += 1

N, M = map(int, input().split())

nodes = [i for i in range(N + 1)]
parents = [i for i in range(N + 1)]
ranks = [0] * (N + 1)

for i in range(M):
    c, a, b = map(int, input().split())
    if c :
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)