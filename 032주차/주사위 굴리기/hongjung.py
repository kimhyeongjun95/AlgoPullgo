import sys

def up():
    global dice
    dice[0], dice[1] = dice[1], dice[0]
    dice[0], dice[4] = dice[4], dice[0]
    dice[4], dice[5] = dice[5], dice[4]

def down():
    global dice
    dice[1], dice[5] = dice[5], dice[1]
    dice[0], dice[5] = dice[5], dice[0]
    dice[4], dice[5] = dice[5], dice[4]

def left():
    global dice
    dice[0], dice[3] = dice[3], dice[0]
    dice[0], dice[2] = dice[2], dice[0]
    dice[2], dice[5] = dice[5], dice[2]

def right():
    global dice
    dice[3], dice[5] = dice[5], dice[3]
    dice[0], dice[5] = dice[5], dice[0]
    dice[2], dice[5] = dice[5], dice[2]

N, M, x, y, K = map(int, sys.stdin.readline().split())
area = [[0] * M for _ in range(N)]

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        area[i][j] = tmp[j]

commands = list(map(int, sys.stdin.readline().split()))

dice = [0] * 6

for command in commands:
    if command == 1:
        if 0 <= y + 1 < M:
            y += 1
            right()
            if area[x][y] == 0:
                area[x][y] = dice[5]
                print(dice[0])
            else:
                dice[5] = area[x][y]
                area[x][y] = 0
                print(dice[0])
    elif command == 2:
        if 0 <= y - 1 < M:
            y -= 1
            left()
            if area[x][y] == 0:
                area[x][y] = dice[5]
                print(dice[0])
            else:
                dice[5] = area[x][y]
                area[x][y] = 0
                print(dice[0])
    elif command == 3:
        if 0 <= x - 1 < N:
            x -= 1
            up()
            if area[x][y] == 0:
                area[x][y] = dice[5]
                print(dice[0])
            else:
                dice[5] = area[x][y]
                area[x][y] = 0
                print(dice[0])
    elif command == 4:
        if 0 <= x + 1 < N:
            x += 1
            down()
            if area[x][y] == 0:
                area[x][y] = dice[5]
                print(dice[0])
            else:
                dice[5] = area[x][y]
                area[x][y] = 0
                print(dice[0])