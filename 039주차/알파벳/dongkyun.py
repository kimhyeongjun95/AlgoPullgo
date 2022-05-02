import sys
sys.stdin = open('input.txt')
from collections import deque

R, C = map(int,input().split())
box = []
for _ in range(R):
    box.append(list(map(str,input())))

# visited = [[0] * C for _ in range(R)]

q = set([(0, 0, box[0][0])])
answer = 1

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