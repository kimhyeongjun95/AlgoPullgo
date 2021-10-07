import sys
from collections import deque
import copy

def bfs(i, j, c, list1):
    path = deque([[i, j]])
    while path:
        x, y = path.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
                if c == list1[ni][nj]:
                    path.append([ni, nj])
                    list1[ni][nj] = 'X'
    return

N = int(sys.stdin.readline())
colors = [[i for i in input()] for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

colors1 = copy.deepcopy(colors)
n_cnt = 0
for i in range(N):
    for j in range(N):
        if colors1[i][j] != 'X':
            c = colors1[i][j]
            n_cnt += 1
            bfs(i, j, c, colors1)

for i in range(N):
    for j in range(N):
        if colors[i][j] == 'R':
            colors[i][j] = 'G'

ab_cnt = 0
for i in range(N):
    for j in range(N):
        if colors[i][j] != 'X':
            c = colors[i][j]
            ab_cnt += 1
            bfs(i, j, c, colors)

print(n_cnt, ab_cnt)




# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# colors = [[i for i in input()] for _ in range(N)]

# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]

# n_cnt = 0
# for i in range(N):
#     for j in range(N):
#         if colors[i][j] != 'X' and colors[i][j] != 'Y':
#             c = colors[i][j]
#             n_cnt += 1
#             path = deque([[i, j]])
#             while path:
#                 x, y = path.popleft()
#                 if colors[x][y] == 'R' or colors[x][y] == 'G':
#                     colors[x][y] = 'Y'
#                 elif colors[x][y] == 'B':
#                     colors[x][y] = 'X'
#                 for d in range(4):
#                     ni = x + di[d]
#                     nj = y + dj[d]
#                     if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
#                         if c == colors[ni][nj]:
#                             path.append([ni, nj])

# ab_cnt = 0
# for i in range(N):
#     for j in range(N):
#         if colors[i][j] != 'Z':
#             c = colors[i][j]
#             ab_cnt += 1
#             path = deque([[i, j]])
#             while path:
#                 x, y = path.popleft()
#                 colors[x][y] = 'Z'
#                 for d in range(4):
#                     ni = x + di[d]
#                     nj = y + dj[d]
#                     if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
#                         if c == colors[ni][nj]:
#                             path.append([ni, nj])

# print(n_cnt, ab_cnt)




# import sys
# from collections import deque
# import copy

# def bfs(i, j, c, list1):
#     path = deque([[i, j]])
#     while path:
#         x, y = path.popleft()
#         list1[x][y] = 'X'
#         for d in range(4):
#             ni = x + di[d]
#             nj = y + dj[d]
#             if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
#                 if c == list1[ni][nj]:
#                     path.append([ni, nj])
#     return

# N = int(sys.stdin.readline())
# colors = [[i for i in input()] for _ in range(N)]

# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]

# colors1 = copy.deepcopy(colors)
# n_cnt = 0
# for i in range(N):
#     for j in range(N):
#         if colors1[i][j] != 'X':
#             c = colors1[i][j]
#             n_cnt += 1
#             bfs(i, j, c, colors1)

# for i in range(N):
#     for j in range(N):
#         if colors[i][j] == 'R':
#             colors[i][j] = 'G'

# ab_cnt = 0
# for i in range(N):
#     for j in range(N):
#         if colors[i][j] != 'X':
#             c = colors[i][j]
#             ab_cnt += 1
#             bfs(i, j, c, colors)

# print(n_cnt, ab_cnt)