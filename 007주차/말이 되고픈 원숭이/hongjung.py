import sys
from collections import deque

def bfs(i, j, k):
    queue = deque([])
    visited = [[[0] * (k+1) for _ in range(W)] for _ in range(H)]
    # 현재 이동할 수 있는 방법이 2가지다. 하나의 경로를 중복해서 갈 수도 있어야 한다!
    # 따라서, 말처럼 이동할 수 있는 경우를 중심으로 방문체크를 해나간다.
    # 이것을 구현하기 위해서는 3차 배열을 사용해야 하는데
    # 쉽게 생각하면, 이렇다 [0][0]에 [0, 0]의 방문체크 리스트가 들어있다.
    queue.append([i, j, k])
    di = [1, 0, 0, -1]
    dj = [0, 1, -1, 0]
    hi = [1, 2, 2, 1, -1, -2, -2, -1]
    hj = [2, 1, -1, -2, 2, 1, -1, -2]    
    while queue:
        x, y, c = queue.popleft()
        if x == H - 1 and y == W - 1:
            return visited[x][y][c]
        if c: # 말처럼 이동할 수 있는 횟수가 남아있을 경우
            for h in range(8):
                ni = x + hi[h]
                nj = y + hj[h]
                if 0 <= ni < H and 0 <= nj < W:
                    if visited[ni][nj][c-1] == 0 and maze[ni][nj] == 0:
                        # ex. 만약 이동할 수 있는 횟수가 4번이라면 각 위치 안에 [0, 0, 0, 0, 0]의 방문리스트가 들어있다.
                        # 그리고 여기에서 만약 한번씩 사용한다면 이 방문체크는 이렇게 변화한다.
                        # ex. [0, 0, 0, 0, 1] -> [0, 0, 0, 2, 1] -> [0, 0, 3, 2, 1] -> [0, 4, 3, 2, 1] 
                        queue.append([ni, nj, c-1])
                        visited[ni][nj][c-1] = visited[x][y][c] + 1
            else: # 횟수는 남아있지만, 말처럼 움직일 수 없는 경우
                for d in range(4):
                    ni = x + di[d]
                    nj = y + dj[d]
                    if 0 <= ni < H and 0 <= nj < W:
                        if visited[ni][nj][c] == 0 and maze[ni][nj] == 0:
                            queue.append([ni, nj, c])
                            visited[ni][nj][c] = visited[x][y][c] + 1
        else: # 말처럼 이동할 수 있는 횟수가 남아있지 않을 경우
            for d in range(4):
                    ni = x + di[d]
                    nj = y + dj[d]
                    if 0 <= ni < H and 0 <= nj < W:
                        if visited[ni][nj][c] == 0 and maze[ni][nj] == 0:
                            queue.append([ni, nj, c])
                            visited[ni][nj][c] = visited[x][y][c] + 1
    return -1



K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

print(bfs(0, 0, K))