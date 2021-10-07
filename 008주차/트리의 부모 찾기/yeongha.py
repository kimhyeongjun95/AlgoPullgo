import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

stack = [1]
while stack:
    v = stack.pop()
    for i in tree[v]:
        if parents[i] == 0:
            parents[i] = v
            stack.append(i)

for i in range(2, N+1):
    print(parents[i])
