import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    visited[y][x] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[y][x] == arr[ny][nx] and visited[ny][nx] == 0:
            dfs(nx, ny)

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(j, i)
            answer1 += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] ='R'

answer2 = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(j, i)
            answer2 += 1

print(answer1, answer2)