# 백준 7569 토마토

# 아직 익지 않은 토마토 -> 하루가 지나면 익은 토마토의 영향
# 위/아래/왼쪽/오른쪽/앞/뒤 6방향

# 며칠이 지나면 다 익게 되는지?
# 최소 일수 구하기, 토마토가 들어있지 않을수도

# 익어있으면 1
# 익지 않은 토마토 0
# 토마토가 들어있지 않으면 -1

# 모두 익어있으면 0 출력, 모두 익지 못하는 상황이면 -1

# 입력 : m x n의 사각형 * h

# 델타값으로 구해볼까?

import sys
input = sys.stdin.readline
from collections import deque
# 오른쪽 왼쪽 앞 뒤 위 아래
dxyz = [
    (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)
]

def tomatofarm(queue):
    # cnt = 0
    while queue:
        x, y, z = queue.popleft()

        for dx, dy, dz in dxyz:
            nx = dx + x
            ny = dy + y
            nz = dz + z

            # 0일때 구하기
            if -1 < nx < h and -1 < ny < n and -1 < nz < m:
                if not visited[nx][ny][nz] and not box[nx][ny][nz]:
                    queue.append((nx, ny, nz))
                    box[nx][ny][nz] = box[x][y][z] + 1
                    visited[nx][ny][nz] = 1
                    
                    # cnt += 1
                    # for i in box:
                    #     for j in i:
                    #         print(j, cnt, '번째')
    
m, n, h = map(int, input().split())
box = []
for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(n)])

visited = [[[0] * m for _ in range(n)] for _ in range(h)]

queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k)) # 반례를 통한.. 미리 1의 위치들을 저장해놔야함.
                visited[i][j][k] = 1

tomatofarm(queue) # 함수 실행

answer = 0
result = True
for i in range(h):
    for j in range(n):
        # 며칠 걸렸는지 확인하기
        for k in range(m): # 안익은 부분 있는지 확인하기
            if box[i][j][k] == 0:
                result = False
            answer = max(answer,(box[i][j][k]))

if result:
    print(answer-1)
else: # 안익은 부분이 있다면
    print(-1)

# 반례 :
# 첫번째 케이스를 확인해보면! or
# 3 3 1
# 1 1 0
# 0 0 0
# 0 0 0