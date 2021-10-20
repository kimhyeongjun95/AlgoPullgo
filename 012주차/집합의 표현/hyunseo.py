# 백준 1717 집합의 표현
import sys
sys.setrecursionlimit(9999999) # 재귀 깊이를 어떻게 계산?
input = sys.stdin.readline

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


n, m = map(int, input().split())
parents = [x for x in range(n+1)]
rank = [0 for _ in range(n+1)]

for _ in range(m):
    command, a, b = map(int, input().split())

    if command:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)