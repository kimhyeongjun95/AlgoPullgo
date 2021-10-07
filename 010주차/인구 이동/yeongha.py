from collections import deque

def move(lst, avg_list):
    for countrys, avg in zip(lst, avg_list):
        for country in countrys:
            r, c = country
            matrix[r][c] = avg

dxy = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(x, y):
    global total
    deq = deque()
    deq.append((x,y))
    country.append((x, y))
    visited[x][y] = 1

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < N and -1 < ny < N and visited[nx][ny] == 0:
                if L <= abs(matrix[x][y] - matrix[nx][ny]) <= R:
                    deq.append((nx, ny))
                    total += matrix[nx][ny]
                    visited[nx][ny] = 1
                    country.append((nx, ny))

N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

day = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    country_list = []
    avg_list = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                # for dx, dy in dxy:
                #     nx, ny = i + dx, j + dy

                #     if -1 < nx < N and -1 < ny < N and visited[nx][ny] == 0:
                #         if L <= abs(matrix[i][j] - matrix[nx][ny]) <= R:
                #             break
                # else:
                #     continue
                country = []
                total = matrix[i][j]
                bfs(i,j)
                cnt = len(country)
                if cnt > 1:
                    avg = total//cnt
                    avg_list.append(avg)
                    country_list.append(country)
                
    if avg_list:
        move(country_list, avg_list)
    else:
        break
    day += 1
print(day)