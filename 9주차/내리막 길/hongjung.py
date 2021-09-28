import sys

def dfs(i, j):
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    stack = [[i, j]]
    cnt = 0
    while stack:
        x, y = stack.pop()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < M and 0 <= nj < N:
                if ni == M - 1 and nj == N - 1:
                    cnt += 1
                elif area[x][y] > area[ni][nj]:
                    stack.append([ni, nj])
    return cnt
    

M, N = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

print(dfs(0, 0))