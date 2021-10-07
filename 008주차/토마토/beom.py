import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = box[x][y][z] + 1
                    queue.append((nx,ny,nz))




M, N, H = map(int, input().split())
box = [[] for _ in range(H)]

for i in range(H):
    for _ in range(N):
        box[i].append(list(map(int, input().split())))

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]
queue = deque()


for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i,j,k))

bfs()
flag = False
answer = 0

for i in range(H):
    for j in range(N):
        for k in range(M):

            if box[i][j][k] == 0:
                flag = True
                break
            answer = max(answer, box[i][j][k])

if flag:
    answer = -1
elif answer == -1:
    answer = 0
else:
    answer -= 1

print(answer)