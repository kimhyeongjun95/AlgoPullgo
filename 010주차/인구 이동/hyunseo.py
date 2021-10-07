# 백준 16234 인구 이동
from collections import deque

def move(unit, total):   
    for i, j in unit:
        country[i][j] = total // len(unit)


def find_unit(i, j):
    unit = [(i, j)]
    total = country[i][j]

    queue = deque()
    queue.append((i, j))

    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                diff = abs(country[x][y] - country[nx][ny])
                if L <= diff <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

                    unit.append((nx, ny))
                    total += country[nx][ny]
    
    return unit, total


N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    units = []

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                unit, total = find_unit(i, j)

                if len(unit) > 1:
                    units.append((unit, total))

    if units:
        for unit, total in units:
            move(unit, total)
        cnt += 1
    else:
        break

print(cnt)