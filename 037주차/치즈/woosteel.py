# Gold 4 치즈
from collections import deque
from pprint import pprint

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

dir_x = [0, 1, -1, 0]
dir_y  =[1, 0, 0, -1]

def check_outside():
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dir_x[i], y + dir_y[i]
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
                if graph[next_x][next_y]:
                    graph[next_x][next_y] += 1
                else:
                    visited[next_x][next_y] = True
                    queue.append([next_x, next_y])

while sum(map(sum, graph)):
    ans += 1
    check_outside()
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
            elif graph[i][j] > 0:
                graph[i][j] = 1
    
print(ans)