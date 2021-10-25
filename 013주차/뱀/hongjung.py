import sys

def dummy(i, j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 2
    time = 0
    d = 0
    snake = [[0, 0]]
    for dir in dirs:
        while time < int(dir[0]):
                i += di[d]
                j += dj[d]
                time += 1
                if i > N - 1 or j > N - 1 or i < 0 or j < 0:
                    return time
                elif visited[i][j] == 2:
                    return time
                elif board[i][j] == 1:
                    board[i][j] = 0
                    visited[i][j] = 2
                    snake.append([i, j])
                elif board[i][j] == 0:
                    visited[i][j] = 2
                    x, y = snake.pop(0)
                    visited[x][y] = 0
                    snake.append([i, j])

        if dir[1] == 'L':
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4

    while True:
        i += di[d]
        j += dj[d]
        time += 1
        if i > N - 1 or j > N - 1 or i < 0 or j < 0:
            return time
        elif visited[i][j] == 2:
            return time
        elif board[i][j] == 1:
            board[i][j] = 0
            visited[i][j] = 2
            snake.append([i, j])
        elif board[i][j] == 0:
            visited[i][j] = 2
            x, y = snake.pop(0)
            visited[x][y] = 0
            snake.append([i, j])


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())
dirs = [list(map(str, sys.stdin.readline().split())) for _ in range(L)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
board = [[0] * N for _ in range(N)]
for apple in apples:
    board[apple[0]-1][apple[1]-1] = 1

print(dummy(0, 0))