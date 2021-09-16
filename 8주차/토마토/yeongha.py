# 토마토
from collections import deque

def bfs(M, N, H):
    dxyz = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)]
    deq = deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[k][i][j] == 1:
                    visited[k][i][j] = 1
                    deq.append([k,i,j])
    day = 0
    while deq:
        flag = False
        for i in range(H):
            for j in range(N):
                if 0 in tomato[i][j]:
                    flag = True
                    break
            if flag:
                break
        else:
            return day

        for _ in range(len(deq)):
            z, x, y = deq.popleft()

            for dx, dy, dz in dxyz:
                nx, ny, nz = x + dx, y + dy, z + dz
                if -1 < nx < N and -1 < ny < M and -1 < nz < H and tomato[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = 1
                    tomato[nz][nx][ny] = 1
                    deq.append([nz, nx, ny])
        day += 1
    return -1


M, N, H = map(int, input().split())

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
tomato = []
for i in range(H):
    tomato.append([list(map(int,input().split())) for _ in range(N)])

print(bfs(M, N, H))