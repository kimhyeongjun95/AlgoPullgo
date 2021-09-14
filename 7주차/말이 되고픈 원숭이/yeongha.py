from collections import deque
def bfs(K, W, H):
    horse_dxy = [(2,1),(1,2),(1,-2),(2,-1),(-2,1),(-1,2),(-2,-1),(-1,-2)]
    monkey_dxy = [(1,0),(0,1),(-1,0),(0,-1)]
    deq = deque()
    deq.append([0, 0, 0])
    while deq:
        x, y, c = deq.popleft()
        
        for dx, dy in monkey_dxy:
            nx, ny = x + dx, y + dy
            if -1 < nx < H and -1 < ny < W and matrix[nx][ny] == 0:
                if distance[nx][ny][c] == 0:
                    distance[nx][ny][c] = distance[x][y][c] + 1
                    if nx == H-1 and ny == W-1:
                        return
                    deq.append([nx, ny, c])
        
        if c < K:
            for dx, dy in horse_dxy:
                nx, ny = x + dx, y + dy

                if -1 < nx < H and -1 < ny < W and matrix[nx][ny] == 0:
                    if distance[nx][ny][c+1] == 0:
                        distance[nx][ny][c+1] = distance[x][y][c] + 1
                        if nx == H-1 and ny == W-1:
                            return
                        deq.append([nx, ny , c+1])

K = int(input())
W, H = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]
distance = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
for i in range(K+1):
    distance[0][0][i] = 1

bfs(K, W, H)

if sum(distance[H-1][W-1])==0:
    print(-1)
else:
    answer = 999999
    for cnt in distance[H-1][W-1]:
        if 0 < answer:
            answer = cnt
    print(answer-1)