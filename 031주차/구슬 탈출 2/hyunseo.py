# 백준 13460 구슬 탈출2

def move(x, y, dx, dy):
    global board

    origin = (x, y)

    while True:
        x += dx
        y += dy
        if board[x][y] == 'O':
            board[origin[0]][origin[1]] = '.'
            return (0, 0)
        elif board[x][y] != '.':
            if (x-dx, y-dy) != origin:
                board[x-dx][y-dy] = board[origin[0]][origin[1]]
                board[origin[0]][origin[1]] = '.'
            return (x-dx, y-dy)


def restore(red, mr, blue, mb):
    global board

    board[red[0]][red[1]] = 'R'
    if mr != (0, 0) and red != mr:
        board[mr[0]][mr[1]] = '.'
    board[blue[0]][blue[1]] = 'B'
    if mb != (0, 0) and blue != mb and board[mb[0]][mb[1]] != 'R':
        board[mb[0]][mb[1]] = '.'


def game(cnt, red, blue):
    global board, answer

    if cnt >= answer:
        return
    
    for i in range(4):
        # 둘 다 이동할 수 없는 상태
        if board[red[0]+dxy[i][0]][red[1]+dxy[i][1]] not in ('.', 'O') and board[blue[0]+dxy[i][0]][blue[1]+dxy[i][1]] not in ('.', 'O'):
            continue

        # 해당 방향쪽에 있는 공부터 움직이도록
        if (i == 0 and red[0] < blue[0]) or (i == 1 and blue[1] < red[1]) or (i == 2 and blue[0] < red[0]) or (i == 3 and red[1] < blue[1]):
            mb = move(blue[0], blue[1], dxy[i][0], dxy[i][1])
            mr = move(red[0], red[1], dxy[i][0], dxy[i][1])
        else:
            mr = move(red[0], red[1], dxy[i][0], dxy[i][1])
            mb = move(blue[0], blue[1], dxy[i][0], dxy[i][1])

        # 빨간 공은 구멍으로 빠져나가고 파란 공은 빠져나가지 않은 경우
        if mr == (0, 0) and mb != (0, 0):
            answer = min(answer, cnt)
        # 두 공 모두 구멍으로 빠져나가지 못한 경우
        elif mb != (0, 0):
            game(cnt+1, mr, mb)
            
        restore(red, mr, blue, mb)


N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)

dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 아 왼 위 오

answer = 11
game(1, red, blue)

if answer == 11:
    print(-1)
else:
    print(answer)