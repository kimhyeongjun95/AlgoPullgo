from collections import deque


N = int(input())

land = []
for _ in range(N):
    land.append(list(map(int, input().split())))

dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]
visited = [[False for _ in range(N)] for _ in range(N)]
queue = deque()


def land_dfs(cnt):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dir_x[i]
            next_y = y + dir_y[i]
            if 0 <= next_x < N and 0 <= next_y < N and land[next_x][next_y] and not visited[next_x][next_y]:
                queue.append([next_x, next_y])
                land[next_x][next_y] += cnt
                visited[next_x][next_y] = True


cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and land[i][j]:
            queue.append([i, j])
            visited[i][j] = True
            land[i][j] += cnt
            land_dfs(cnt)
            cnt += 1

ans = float('inf')

for k in range(1, cnt + 2):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if land[i][j] == k:
                queue.append([i, j])
                temp[i][j] = 1
    flag = False
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dir_x[i], y + dir_y[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if land[next_x][next_y] and land[next_x][next_y] != k:
                    ans = min(ans, temp[x][y])
                    flag = True
                    if flag:
                        break
                if not land[next_x][next_y] and not temp[next_x][next_y]:
                    temp[next_x][next_y] = temp[x][y] + 1
                    queue.append([next_x, next_y])
        if flag:
            queue = deque()
            break

print(land)
print(ans - 1)
