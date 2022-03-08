# 백준 2146 다리 만들기

# 여러 섬
# 한 섬과 다른 섬을 잇는 다리 하나만을 만들고 짧게 하기

# n X n
# 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리

# 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법

# 0 바다 1 육지

from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 섬을 각각 2부터 시작해서 indexing
def idxing(x, y, count):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1
    arr[x][y] = count

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if -1 < nx < n and -1 < ny < n and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                arr[nx][ny] = count
                queue.append((nx, ny))

# 거리 구하기
def bfs(count):
    global answer
    dist = [[-1] * n for _ in range(n)]
    queue = deque([])

    for i in range(n):
        for j in range(n):
            if arr[i][j] == count:
                queue.append((i, j))
                dist[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if -1 < nx < n and -1 < ny < n:
                # 바다를 만나면
                if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                # 다른 다리와 만나면 최소값
                if arr[nx][ny] > 1 and arr[nx][ny] != count:
                    answer = min(answer, dist[x][y])
                    return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
count = 2

for i in range(n):
    for j in range(n):
        visited = [[0] * n for _ in range(n)]
        if arr[i][j] == 1 and not visited[i][j]:
            idxing(i, j, count)
            count += 1

for i in range(2, count):
    bfs(i)

print(answer)