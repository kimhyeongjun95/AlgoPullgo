import sys
from collections import deque

def bfs(N, tunnel):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    max_num = N * N * 9
    visited = [[max_num] * N for _ in range(N)]
    visited[0][0] = tunnel[0][0]
    queue = deque([[0, 0]])

    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and visited[i][j] + tunnel[ni][nj] < visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + tunnel[ni][nj]
                queue.append([ni, nj])
    
    return visited[N-1][N-1]


cnt = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    tunnel = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    answer = bfs(N, tunnel)
    print(f'Problem {cnt}: {answer}')
    cnt += 1
    