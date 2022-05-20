import sys
from collections import deque
sys.stdin = open("input.txt")

N, K = map(int,input().split())
box = []
virus = []
for _ in range(N):
    box.append(list(map(int,input().split())))
S, Y ,X  = map(int,input().split())


s = 0
for y in range(N):
    for x in range(N):
        if box[y][x]:
            n = box[y][x]
            virus.append((n,y,x,s))
virus.sort()
q = deque(virus)


while q:
    n,y,x,s = q.popleft()
    if s == S:
        break
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in dxy:
        if 0 <= x + dx < N and 0 <= y + dy < N:
            if box[y + dy][x + dx] == 0:
                box[y + dy][x + dx] = n
                q.append((n,y+dy,x+dx,s+1))


print(box[Y-1][X-1])