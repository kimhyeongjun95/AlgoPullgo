# 백준 17471 게리맨더링
from collections import deque
from itertools import combinations

def diff_pop(A, B):
    global min_pop

    A_pop = 0
    B_pop = 0

    for a in A:
        A_pop += population[a]
    
    for b in B:
        B_pop += population[b]
    
    min_pop = min(min_pop, abs(A_pop-B_pop))


def bfs(group):
    queue = deque()
    queue.append(group[0])

    visited = [0 for _ in range(N+1)]
    visited[group[0]] = 1

    while queue:
        v = queue.popleft()

        for w in section[v]:
            if w in group and visited[w] == 0:
                visited[w] = 1
                queue.append(w)
    
    for g in group:
        if visited[g] == 0:
            return False
    return True


N = int(input())
population = [0] + list(map(int, input().split()))

section = [[] for _ in range(N+1)]
for i in range(N):
    temp = list(map(int, input().split()))
    section[i+1] = temp[1:]

min_pop = float('inf')
for n in range(1, N//2 + 1):
    for combo in combinations([x for x in range(1, N+1)], n):
        A = combo
        B = [y for y in range(1, N+1) if y not in A]

        if bfs(A) and bfs(B):
            diff_pop(A, B)

if min_pop == float('inf'):
    min_pop = -1

print(min_pop)