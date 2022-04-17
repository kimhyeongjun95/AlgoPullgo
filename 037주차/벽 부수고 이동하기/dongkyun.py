import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    Y, X = map(int,input().split())
    box = []
    for _ in range(Y):
        box.append(list(map(int, input())))
    visited = [[0] * X for _ in range(Y)]



    def bts():
        queue = deque([(0, 0, 0)])
        visited[0][0] = 1
        dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        # BFS로 탐색하면서 돌건데 갈데없고 아이템있으면 하나깰꺼임
        while queue:
            ny, nx, wall = queue.popleft()
            if ny == Y-1 and nx == X-1:
                return visited[ny][nx]

            for dx,dy in dxy:
                if 0 <= nx + dx < X and 0 <= ny + dy < Y and visited[ny+dy][nx+dx] == 0 :
                    if box[ny+dy][nx+dx] == 0:
                        queue.append((ny + dy, nx + dx, wall))
                        visited[ny+dy][nx+dx] = visited[ny][nx] + 1
                    # 아이템있네?
                    if wall == 0 and box[ny+dy][nx+dx] == 1:
                        queue.append((ny+dy, nx+dx, 1))
                        visited[ny+dy][nx+dx] = visited[ny][nx] + 1


        return -1
    print(bts())




