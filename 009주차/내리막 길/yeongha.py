import sys
sys.setrecursionlimit(10000)

dxy = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs(n):
    global ans
    x, y = n
    if x == M-1 and y == N-1: 
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if -1 < nx < M and -1 < ny < N:
                if matrix[nx][ny] < matrix[x][y]:
                    dp[x][y] += dfs((nx, ny))
    return dp[x][y]

            
M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
ans = 0
print(dfs((0,0)))