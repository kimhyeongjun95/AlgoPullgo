import sys
from collections import deque

def bfs(i, j):
    di = [1, 0, 0, -1]
    dj = [0, 1, -1, 0]
    queue = deque([])
    queue.append([i, j])
    visited = [[-1] * N for _ in range(M)] # 방문체크(1이면 벽 부순 수로 체크)
    visited[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < M and 0 <= nj < N:
                if visited[ni][nj] == -1:
                    if maze[ni][nj] == 0:
                        queue.appendleft([ni, nj]) # 여기서 왜 appendleft인지? 그래야 벽을 부수지 않고 빨리 갈 수 있으므로
                        visited[ni][nj] = visited[x][y] # 벽을 부수지 않았기 때문에 전 경로의 방문체크를 그대로 써줌
                    else:
                        queue.append([ni, nj])
                        visited[ni][nj] = visited[x][y] + 1 # 벽을 부쉈기 때문에 전 경로의 방문체크 + 1을 해줌
    return visited[M-1][N-1] # 벽을 가장 덜 부수고 온 경로가 가장 빨리 오고 그 주위를 -1이 아닌 숫자로 방문체크 해놓기 때문에 끝만 반환해줘도 됨

N, M = map(int, sys.stdin.readline().split())

maze = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(M)]

ti = tj = 0
print(bfs(ti, tj))