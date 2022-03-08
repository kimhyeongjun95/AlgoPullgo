import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global temp
    temp += 1
    board[i][j] += temp
    deq = deque([(i,j)])
    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
                board[nx][ny] += temp
                deq.append((nx, ny))

def find(i, j, island):
    deq = deque([(i, j)])
    dist = [[0]*N for _ in range(N)]
    dist[i][j] = 1

    while deq:
        x, y = deq.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not dist[nx][ny] and board[nx][ny] != island:
                dist[nx][ny] = dist[x][y] + 1

                if dist[nx][ny] - 2 >= result:
                    return 0
                
                if board[nx][ny]:
                    return dist[nx][ny] - 2

                deq.append((nx, ny))
    return 0

dxy = [(1,0),(0,1),(0,-1),(-1,0)]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

temp = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            bfs(i,j)

result = float('inf')
for i in range(N):
    for j in range(N):
        if board[i][j]:
            island = board[i][j]
            min_dist = find(i, j, island)

            if min_dist:
                result = min(result, min_dist)

print(result)
