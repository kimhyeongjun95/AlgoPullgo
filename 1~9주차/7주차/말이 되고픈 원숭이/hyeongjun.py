from collections import deque
import sys

# 말의 이동범위
hx = [1, 2, 2, 1, -1, -2, -2, -1]
hy = [-2, -1, 1, 2, 2, 1, -1, -2]
# 원숭이의 이동범위
mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]
    
def monkey_rider(x, y, k):
    visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]
    queue = deque([])
    queue.append([0, 0, k])

    while queue:
        x, y, cnt = queue.popleft()

        if x == h-1 and y == w-1:
            return visited[x][y][cnt] 
            # return visited

        # 만약 cnt가 있다면
        if cnt:
            for i in range(8):
                nx = hx[i] + x
                ny = hy[i] + y
                if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == 0 and visited[nx][ny][cnt-1] == 0:
                    visited[nx][ny][cnt-1] = visited[x][y][cnt] + 1
                    queue.append([nx, ny, cnt-1])

            else: # 장애물
                for i in range(4):
                    nx = mx[i] + x
                    ny = my[i] + y
                    if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                        visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                        queue.append([nx, ny, cnt])
    
        else:# cnt가 0이라면
            for i in range(4):
                nx = mx[i] + x
                ny = my[i] + y
                if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    queue.append([nx, ny, cnt])
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1

    return -1


k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
print(monkey_rider(w, h, k))