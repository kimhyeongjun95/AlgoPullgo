import sys
input = sys.stdin.readline
from collections import deque
 
n, l, r = map(int, input().split())
maps = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
check = [[False for j in range(n)] for i in range(n)]
for j in range(n):
    maps.append(list(map(int, input().split())))
 
 
# def bfs(y, x):
#     queue = deque()
#     queue.append((y, x))
#     tmp = deque()
#     val, cnt = 0, 0
#     while queue:
#         y, x = queue.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or nx < 0 or ny >= n or nx >= n:
#                 continue
          
#             if l <= abs(maps[y][x] - maps[ny][nx]) <= r and check[ny][nx] == False:
#                 queue.append((ny, nx))
#                 tmp.append((ny, nx))
#                 val += maps[ny][nx]
#                 cnt += 1
#                 check[ny][nx] = True
 




