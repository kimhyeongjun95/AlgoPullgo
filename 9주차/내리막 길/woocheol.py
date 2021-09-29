# 1520 내리막 길
import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

visited[0][0] = True
cnt = 0


def dfs(x, y):
    global cnt
    if x == n - 1 and y == m - 1:
        cnt += 1
        return

    for i in range(4):
        next_x, next_y = x + dir_x[i], y + dir_y[i]
        if 0 <= next_x < n and 0 <= next_y < m and graph[x][y] > graph[next_x][next_y] and not visited[next_x][next_y]:
            visited[next_x][next_y] = True
            dfs(next_x, next_y)
            visited[next_x][next_y] = False

# 시간 초과


dp = [[-1 for _ in range(m)] for _ in range(n)]


def dfs_2(x, y):
    if x == n-1 and y == m-1:

        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            next_x, next_y = x + dir_x[i], y + dir_y[i]
            if 0 <= next_x < n and 0 <= next_y < m and graph[x][y] > graph[next_x][next_y]:
                dp[x][y] += dfs_2(next_x, next_y)

    return dp[x][y]


dp[n-1][m-1] = 1
print(dfs_2(0, 0))
