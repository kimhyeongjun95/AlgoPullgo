# 17144번 미세먼지 안녕!
from collections import deque

dir_x = [0, 1, -1, 0]
dir_y = [1, 0, 0, -1]


def spread():
    queue = []
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                temp = room[i][j] // 5
                for k in range(4):
                    next_x, next_y = i + dir_x[k], j + dir_y[k]
                    if 0 <= next_x < R and 0 <= next_y < C and room[next_x][next_y] >= 0:
                        queue.append([next_x, next_y, temp])
                        queue.append([i, j, -temp])

    for i, j, temp in queue:
        room[i][j] += temp


def activate():
    x, y = air_cleaner[0]
    for i in range(x-2, -1, -1):
        room[i+1][0] = room[i][0]
    for j in range(1, C):
        room[0][j-1] = room[0][j]
    for i in range(1, x+1):
        room[i-1][-1] = room[i][-1]
    for j in range(C-2, 0, -1):
        room[x][j+1] = room[x][j]
    room[x][1] = 0

    x, y = air_cleaner[1]
    for i in range(x+2, R):
        room[i-1][0] = room[i][0]
    for j in range(1, C):
        room[-1][j-1] = room[-1][j]
    for i in range(R-2, x-1, -1):
        room[i+1][-1] = room[i][-1]
    for j in range(C-2, 0, -1):
        room[x][j+1] = room[x][j]
    room[x][1] = 0


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
air_cleaner = []

for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            air_cleaner.append([i, j])

while T:
    spread()
    activate()
    T -= 1

print(sum(map(sum, room)) + 2)
