import sys

def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])


n, m = map(int, sys.stdin.readline().split())

parents = list(range(n+1))
ranks = [0 for _ in range(n+1)]

for _ in range(m):
    method, a, b = map(int, sys.stdin.readline().split())
    if method:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
    else: 
        set_a = find_set(a)
        set_b = find_set(b)
        if ranks[set_a] > ranks[set_b]:
            parents[set_b] = set_a
        elif ranks[set_a] < ranks[set_b]:
            parents[set_a] = set_b
        else:
            parents[set_a] = set_b
            ranks[set_b] += 1