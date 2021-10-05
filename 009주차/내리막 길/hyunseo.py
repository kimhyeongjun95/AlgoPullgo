# 백준 1520 내리막 길
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] < arr[x][y]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]
    

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

dp = [[-1 for _ in range(N)] for _ in range(M)]
dp[M-1][N-1] = 1

print(dfs(0, 0))