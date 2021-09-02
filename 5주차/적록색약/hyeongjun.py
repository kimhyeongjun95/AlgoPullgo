# 같은 색상이 상하좌우 인접 -> 같은 구역
# 적록색약: R, G 같은 색상으로 보임

# RRRBB 00011
# GGBBB 00111
# BBBRR 11100
# BBRRR 11000
# RRRRR 00000
# 적록색약은 3개로 보이고 아닌사람은 4개로 보임. (구역)
# dfs or bfs
# dfs로 구현해보자 - stack

# 1. visited: R/G/B .. 범위를 벗어나지 않고.. 방문하지 않았고..., 현재 색상과 다르고...
# 1-1. visited: r/b 모든 G를 R로 미리 바꾸어 놓자.

# import sys
# input = sys.stdin.readline.strip()

dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def area_count(x, y):
    stack = []
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        color = arr[x][y]

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] == color: # 방문하지 않았고 같은 색이라면 탐색
                    stack.append((nx, ny))

n = int(input())
arr = [list(input()) for _ in range(n)]
# 2차원 문자열 입력받기 어떻게 하지?
# arr = [list(map(str, input().split())) for _ in range(n)]
answer = [] # 답 모으기

visited = [[0] * n for _ in range(n)]
count = 0
# 비적록색약
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            area_count(i, j)
            count += 1
answer.append(count)

visited = [[0] * n for _ in range(n)]
count = 0
# 적록색약
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R' # 빨간색과 초록색은 같은 색으로

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            area_count(i, j)
            count += 1
answer.append(count)

print(' '.join(map(str, answer)))