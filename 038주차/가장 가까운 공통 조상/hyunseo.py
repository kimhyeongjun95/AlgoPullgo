# 백준 3584 가장 가까운 공통 조상

import sys

def find_parent(c):
    if c in graph.keys():
        return graph[c]
    
    return 0


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    graph = {}
    visited = [0 for _ in range(N+1)]

    for _ in range(N-1):
        p, c = map(int, input().split())
        graph[c] = p
    
    a, b = map(int, input().split())

    while True:
        visited[a] += 1
        visited[b] += 1

        if a and visited[a] == 2:
            print(a)
            break
        elif b and visited[b] == 2:
            print(b)
            break
        
        a = find_parent(a)
        b = find_parent(b)