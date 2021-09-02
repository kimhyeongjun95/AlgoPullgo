from collections import deque

def bfs(arr, x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        curr_x, curr_y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = curr_x+dx, curr_y+dy

            if nx in range(N) and ny in range(N) and visited[nx][ny] == 0 and arr[curr_x][curr_y] == arr[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))


def cnt(arr):
    cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(arr, i, j)
                cnt += 1
    
    return cnt


N = int(input())

normal_arr = []
rg_arr = []
for _ in range(N):
    temp = []
    rg_temp = []
    for s in input():
        temp.append(s)
        if s == 'G':
            rg_temp.append('R')
        else:
            rg_temp.append(s)

    normal_arr.append(temp)
    rg_arr.append(rg_temp)

visited = [[0]* N for _ in range(N)]
normal_cnt = cnt(normal_arr)

visited = [[0]* N for _ in range(N)]
rg_cnt = cnt(rg_arr)

print(normal_cnt, rg_cnt)