# 14502번 연구소
from collections import deque
from itertools import combinations


def bfs(graph, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    wide = 0
    dir_x = [0, 0, 1, -1]
    dir_y = [1, -1, 0, 0]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append([i, j])
                visited[i][j] = True
            if graph[i][j] == 1:
                visited[i][j] = True

    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y] and graph[next_x][next_y] == 0:
                queue.append([next_x, next_y])
                visited[next_x][next_y] = True

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                wide += 1

    return wide


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

walls = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            walls.append([i, j])

walls = combinations(walls, 3)
ans = 0

for a, b, c in walls:
    lab[a[0]][a[1]] = 1
    lab[b[0]][b[1]] = 1
    lab[c[0]][c[1]] = 1

    ans = max(ans, bfs(lab, n, m))

    lab[a[0]][a[1]] = 0
    lab[b[0]][b[1]] = 0
    lab[c[0]][c[1]] = 0

print(ans)
