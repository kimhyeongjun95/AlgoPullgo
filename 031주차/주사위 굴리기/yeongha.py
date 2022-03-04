N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0, 0, 0, 0, 0, 0]

for m in move:
    dx, dy = dxy[m-1]
    x += dx
    y += dy
    if not 0 <= x < N or not 0 <= y < M:
        x -= dx
        y -= dy
        continue
    if m == 1:
        temp, dice[0] = dice[0], dice[2]
        temp, dice[3] = dice[3], temp
        temp, dice[5] = dice[5], temp
        dice[2] = temp
    elif m == 2:
        temp, dice[2] = dice[2], dice[0]
        temp, dice[5] = dice[5], temp
        temp, dice[3] = dice[3], temp
        dice[0] = temp
    elif m == 3:
        temp, dice[4] = dice[4], dice[0]
        temp, dice[5] = dice[5], temp
        temp, dice[1] = dice[1], temp
        dice[0] = temp
    else:
        temp, dice[0] = dice[0], dice[4]
        temp, dice[1] = dice[1], temp
        temp, dice[5] = dice[5], temp
        dice[4] = temp

    if not board[x][y]:
        board[x][y] = dice[0]
    else:
        dice[0] = board[x][y]
        board[x][y] = 0
        
    print(dice[5])


