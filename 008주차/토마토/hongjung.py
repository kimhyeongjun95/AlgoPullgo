import sys
from collections import deque

def bfs(list1):
    dj = [1, -1, 0, 0]
    dk = [0, 0, -1, 1]
    di = [1, 0, -1]
    queue = deque([])
    for l in list1:
        queue.append(l)
    visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
    for q in queue:
        visited[q[0]][q[1]][q[2]] = 0
    while queue:
        i, j, k = queue.popleft()
        for d in range(4): # 상 하 좌 우 체크
            nj = j + dj[d]
            nk = k + dk[d]
            if 0 <= nj < N and 0 <= nk < M:
                if tomatoes[i][nj][nk] == 0 and visited[i][nj][nk] == -1:
                    queue.append([i, nj, nk])
                    visited[i][nj][nk] = visited[i][j][k] + 1
                    tomatoes[i][nj][nk] = 1

        for t in range(3): # 위 아래 체크
            ni = i + di[t]
            if 0 <= ni < H:
                if tomatoes[ni][j][k] == 0 and visited[ni][j][k] == -1:
                    queue.append([ni, j, k])
                    visited[ni][j][k] = visited[i][j][k] + 1
                    tomatoes[ni][j][k] = 1

    flag = False
    result = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 0:
                    flag = True
                    break
                else:
                    if visited[i][j][k] > result:
                        result = visited[i][j][k]
    if flag:
        return -1
    else:
        return result

M, N, H = map(int, sys.stdin.readline().split())
# 3차원 배열 입력 받기
tomatoes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N*i, N*i+N)] for i in range(H)]

ripen = []
# 익은 감 리스트 찾아주기
for ti in range(H):
    for tj in range(N):
        for tk in range(M):
            if tomatoes[ti][tj][tk] == 1:
                ripen.append([ti, tj, tk])

print(bfs(ripen))