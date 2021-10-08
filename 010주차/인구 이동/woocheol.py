# 16234번 인구이동
from collections import deque

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

dir_x = [0, 1, -1, 0]
dir_y = [1, 0, 0, -1]
ans = 0


def bfs(x, y):
    global flag
    queue = deque()
    visited[x][y] = True
    temp, cnt = population[x][y], 1
    queue.append([x, y])
    change = [[x, y]]
    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and L <= abs(population[next_x][next_y] - population[curr_x][curr_y]) <= R:
                temp += population[next_x][next_y]
                cnt += 1
                queue.append([next_x, next_y])
                change.append([next_x, next_y])
                visited[next_x][next_y] = True

    if cnt > 1:
        flag = False
        for i, j in change:
            population[i][j] = temp // cnt


cnt = 0

while True:
    flag = True
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                for k in range(4):
                    if 0 <= i + dir_x[k] < N and 0 <= j + dir_y[k] < N and L <= abs(population[i][j] - population[i + dir_x[k]][j + dir_y[k]]) <= R:
                        bfs(i, j)
                        break

    if flag:
        break
    else:
        cnt += 1

print(cnt)
