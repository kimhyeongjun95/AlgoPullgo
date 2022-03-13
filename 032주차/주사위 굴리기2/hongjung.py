import sys
from collections import deque

def move_dice(dice, direc):

    if direc == 0:
        dice[0], dice[3] = dice[3], dice[0]
        dice[0], dice[1] = dice[1], dice[0]
        dice[0], dice[2] = dice[2], dice[0]
    elif direc == 1:
        dice[0], dice[5] = dice[5], dice[0]
        dice[0], dice[1] = dice[1], dice[0]
        dice[0], dice[4] = dice[4], dice[0]
    elif direc == 2:
        dice[0], dice[3] = dice[3], dice[0]
        dice[1], dice[2] = dice[2], dice[1]
        dice[2], dice[3] = dice[3], dice[2]
    else:
        dice[0], dice[5] = dice[5], dice[0]
        dice[1], dice[5] = dice[5], dice[1]
        dice[1], dice[4] = dice[4], dice[1]

def rotate(i, j):
    global dice, area, di, dj, direction

    if dice[1] > area[i][j]:
        direction += 1
    elif dice[1] < area[i][j]:
        direction += 3
    
    direction = direction % 4

    if 0 <= i + di[direction] < N and 0 <= j + dj[direction] < M:
        pass
    else:
        direction = (direction + 2) % 4


def move(i, j, direc):
    global N, M, di, dj, area, dice

    ni = i + di[direc]
    nj = j + dj[direc]
    
    move_dice(dice, direc)

    return ni, nj


def find(i, j, num):
    global di, dj, area

    tmp = 1
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    queue = deque([[i, j]])

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False and area[ni][nj] == num:
                visited[ni][nj] = True
                tmp += 1
                queue.append([ni, nj])
    
    return tmp


N, M, K = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

direction = 0
dice = [1, 6, 4, 3, 2, 5]
score = 0
i = j = 0
for _ in range(K):
    i, j = move(i, j, direction)
    score += (find(i, j, area[i][j]) * area[i][j])
    rotate(i, j)
    
print(score)