import sys
input = sys.stdin.readline
from collections import deque

def bfs(sy, sx, safe_area):
    queue = deque([(sy, sx)])
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))


    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1  # 방문 체크

        # 현재 위치(y,x)에서 갈 수 있는 곳 탐색
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if visited[ny][nx] == 0 and area[ny][nx] >= safe_area:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))



N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]


max_area = 0
min_area = 101
for i in range(N):
    for j in range(N):
        if area[i][j] > max_area:
            max_area = area[i][j]
        elif area[i][j] < min_area:
            min_area = area[i][j]

max_safe_area = min_area
for safe_area in range(min_area, max_area+1):
    visited = [[0] * N for _ in range(N)]
    count =0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] >= safe_area:
                bfs(i,j,safe_area)
                count += 1
    
    if count > max_safe_area:
        max_safe_area = count
print(max_safe_area)