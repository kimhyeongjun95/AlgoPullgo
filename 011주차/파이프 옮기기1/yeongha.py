dxy = [[(0,1),(1,1)],[(1,0),(1,1)],[(0,1),(1,0),(1,1)]]
# 가로:0, 세로:1, 대각선:2

def dfs(x,y,d):
    if x == y == N-1:
        return 1

    if dp[x][y][d] == -1:
        dp[x][y][d] = 0
        for dx, dy in dxy[d]:
            nx, ny = x + dx, y + dy
            nd = dx*(dy+1)

            if -1 < nx < N and -1 < ny < N and not matrix[nx][ny]:
                if nd == 2 and (matrix[nx-1][ny] or matrix[nx][ny-1]):
                    continue
                dp[x][y][d] += dfs(nx, ny, nd)
    
    return dp[x][y][d]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-1]*3 for _ in range(N)] for _ in range(N)]
dfs(0,1,0)
print(dp[0][1][0])