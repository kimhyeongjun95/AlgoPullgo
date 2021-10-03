import sys
from collections import deque


def bfs():
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + dir[i][0]
            dy = y + dir[i][1]
            if 0 <= dx < n and 0 <= dy < m and not vis[dx][dy]:
                vis[dx][dy] = True
                if miro[dx][dy] == 1:
                    q.append([dx, dy])
                    count[dx][dy] = count[x][y] + 1
                else:
                    q.appendleft([dx, dy])
                    count[dx][dy] = count[x][y]

    print(count[n - 1][m - 1])


m, n = map(int, input().split())

miro = []
for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
vis = [[False] * m for _ in range(n)]
count = [[0] * m for _ in range(n)]
q = deque()
bfs()