# 백준 14502 연구소
from itertools import combinations
from collections import deque

def bfs(arr):
    queue = deque(virus)

    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i, j in virus:
        visited[i][j] = 1

    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0<= nx < N and 0 <= ny < M and not arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                arr[nx][ny] = 2
                queue.append((nx, ny))
    
    return arr


def safe_area(lab, empty):
    arr = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            arr[i][j] = lab[i][j]

    for i, j in empty:
        arr[i][j] = 1

    arr = bfs(arr)

    cnt = 0
    for k in range(N):
        for l in range(M):
            if arr[k][l] == 0:
                cnt += 1

    return cnt


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

place = []
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            place.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

max_cnt = 0
for combo in combinations(place, 3):
    cnt = safe_area(lab, combo)
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)