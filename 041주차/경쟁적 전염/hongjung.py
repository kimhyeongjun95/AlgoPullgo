import sys
from collections import defaultdict

def bfs(num, i, j):
    global N, area, next_loca

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0] 

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and area[ni][nj] == 0:
            next_loca[num].append([ni, nj])
            area[ni][nj] = num
    

N, K = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())

num_loca = defaultdict(list)
next_loca = defaultdict(list)
for i in range(1, K + 1):
    for j in range(N):
        for k in range(N):
            if area[j][k] == i:
                next_loca[i].append([j, k])

for _ in range(S):
    for i in range(1, K + 1):
        num_loca[i] = next_loca[i][:]
        next_loca[i] = []

    for i in range(1, K + 1):
        for j, k in num_loca[i]:
            bfs(i, j, k)

print(area[X-1][Y-1])