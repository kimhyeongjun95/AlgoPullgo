import sys

def dfs(start, end):
    stack = [[start, 0]]
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    
    while stack:
        x, d = stack.pop()
        for i in graph[x]:
            if i:
                if i[0] == end:
                    d += i[1]
                    return d
                elif visited[i[0]] == 0:
                    visited[i[0]] = 1
                    stack.append([i[0], d+i[1]])
                

N, M = map(int, sys.stdin.readline().split())
nodes = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
want = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

graph = [[] * (N+1) for _ in range(N+1)]

for node in nodes:
    graph[node[0]].append([node[1], node[2]])
    graph[node[1]].append([node[0], node[2]])

for w in want:
    print(dfs(w[0], w[1]))