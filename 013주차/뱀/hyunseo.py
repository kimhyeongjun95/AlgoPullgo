from collections import deque

# 백준 3190 뱀

def dummy(i, j):
    snake = deque()
    snake.append((i, j))
    arr[i][j] = 2

    # 0 : 왼 / 1: 오
    turn = {
        (0, 1) : [(-1, 0), (1, 0)], (1, 0) : [(0, 1), ((0, -1))],
        (0, -1) : [(1, 0), (-1, 0)], (-1, 0) : [(0, -1), (0, 1)]
    }
    dxy = (0, 1) # 오른쪽

    time = 0

    while True:
        time += 1

        x, y = snake[-1][0], snake[-1][1]

        nx, ny = x+dxy[0], y+dxy[1]

        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 0:
                tx, ty = snake.popleft()
                arr[tx][ty] = 0
                snake.append((nx, ny))
                arr[nx][ny] = 2
            elif arr[nx][ny] == 1:
                snake.append((nx, ny))
                arr[nx][ny] = 2
            else:
                return time
        else:
            return time
        
        if time in command.keys():
            if command[time] == 'L':
                dxy = turn[dxy][0]
            else:
                dxy = turn[dxy][1]


N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(int(input())):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

command = {}
for _ in range(int(input())):
    X, C = input().split()
    command[int(X)] = C

print(dummy(0, 0))