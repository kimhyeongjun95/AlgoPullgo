import sys
from collections import deque

def search_root(n):
    global root
    queue = deque()
    queue.append(n)

    while queue:
        node = queue.popleft()
        if nodes[node]:
            for i in nodes[node]:
                if root[i] == 0:
                    root[i] = node
                    queue.append(i)
    return


N = int(sys.stdin.readline())
nodes = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

root = [0 for _ in range(N + 1)]
search_root(1)
for i in range(2, N + 1):
    print(root[i])