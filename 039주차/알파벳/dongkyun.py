import sys
sys.stdin = open('input.txt')
from collections import deque





R, C = map(int,input().split())
box = []
for _ in range(R):
    box.append(list(map(str,input())))

visited = [[0] * C for _ in range(R)]

q = set([(0, 0, box[0][0])])
answer = 1

# def dfs(y, x, count):
#     global answer
#     dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     count = max(answer,count)
#     for dx, dy in dxy:
#         nx = x + dx
#         ny = y + dy
#         if 0 <= ny < R and 0 <= nx < C and not (box[ny][nx] in imposter) and not visited[ny][nx]:
#             visited[ny][nx] = 1
#             dfs(ny, nx, count + 1)
#             visited[ny][nx] = 0
#
# dfs(0, 0, 1)
# print(answer)

while q:
    y, x, alphamon = q.pop()
    answer = max(answer, len(alphamon))
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= ny < R and 0 <= nx < C and not (box[ny][nx] in alphamon):
            q.add((ny, nx, alphamon + box[ny][nx]))



print(answer)