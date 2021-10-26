N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2

L = int(input())
snake = []
for _ in range(L):
    snake.append(input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x, y = 0, 0
dir = 0
tail = []
tail.append([0,0])
board[0][0] = 1
time = 0

while True:
    if len(snake) != 0:
        if time == int(snake[0][0]):
            C = snake.pop(0)[1]
            if C == "L":
                dir = (dir - 1) % 4
            else:
                dir = (dir + 1) % 4

    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 1:
        time += 1
        break

    else:
        # 사과가 있으면 꼬리 두기
        if board[nx][ny] == 2: 
            board[nx][ny] = 1
            tail.append([nx, ny])
        
        # 사과가 없으면 이동 후에 꼬리 제거
        else:
            tx, ty = tail.pop(0)
            board[tx][ty] = 0
            board[nx][ny] = 1
            tail.append([nx,ny])
    x,y = nx, ny
    time += 1


print(time)


