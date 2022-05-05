# 백준 6087 레이저 통신

# W x H 지도
# 'c'의 두 칸 레이저 통신
# 설치해야 하는 거울 개수의 최솟값 return

# . : 빈칸
# * : 벽

# 1. 직선으로 나아가기
# 2. turn 마다 + 1
# 3. 만나면 return

from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1 ,0)]
w, h = map(int, input().split())
arr = [list(input()) for _ in range(h)]
visited = [[float('inf')] * w for _ in range(h)]
sx, sy = -1, -1
ex, ey = -1, -1
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            if sx >= 0 and sy >= 0:
                ex, ey = i, j
            else:
                sx, sy = i, j
def find():
    queue = deque([(sx, sy)])
    # 출발점 방문처리
    visited[sx][sy] = 0

    while queue:

        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            while True:
                if nx >= h or nx < 0 or ny >= w or ny < 0:
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                if arr[nx][ny] == '*':
                    break
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                # 직선
                nx = nx + dx 
                ny = ny + dy

find()
answer = visited[ex][ey] - 1
print(answer)