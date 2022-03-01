import sys
from collections import deque

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j

    queue.append((rx, ry, bx, by, 1))
    check[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0
    while graph[x+dx][y+dy] != "#" and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    init()
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for d in range(4):
            nrx, nry, rcnt = move(rx, ry, di[d], dj[d])
            nbx, nby, bcnt = move(bx, by, di[d], dj[d])
            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(depth)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= di[d]
                        nry -= dj[d]
                    else:
                        nbx -= di[d]
                        nby -= dj[d]

                if not check[nrx][nry][nbx][nby]:
                    check[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth + 1)) 
    print(-1)


n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
queue = deque()
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

bfs()