def row(x, n):
    if n in board[x][:]:
        return False
    else:
        return True

def col(y, n):
    for i in range(9):
        if board[i][y] == n:
            return False
    return True

def rectangle(x, y, n):
    nx, ny = x // 3 * 3, y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[nx+i][ny+j] == n:
                return False
    return True

def sudoku(m):
    global board, find

    if find:
        return

    if m == N:
        find = 1
        for i in range(9):
            print(*board[i])
        return

    x, y = blank[m]
    for n in range(1, 10):
        if row(x, n) and col(y, n) and rectangle(x, y, n):
            board[x][y] = n
            sudoku(m+1)
            board[x][y] = 0
    

board = [list(map(int, input().split())) for _ in range(9)]
blank = []
for x in range(9):
    for y in range(9):
        if not board[x][y]:
            blank.append([x, y])

N = len(blank)
find = 0
sudoku(0)
