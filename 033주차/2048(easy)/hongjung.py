import sys
import copy

def up(puzzle):
    global di, dj

    visited = [[False] * N for _ in range(N)]
    for i in range(1, N):
        for j in range(N):
            ti = i
            tj = j
            while True:
                ni = ti + di[0]
                nj = tj + dj[0]
                if 0 <= ni < N and 0 <= nj < N:
                    if puzzle[ni][nj] == 0:
                        puzzle[ni][nj] = puzzle[ti][tj]
                        puzzle[ti][tj] = 0
                        visited[ni][nj] = visited[ti][tj]
                        visited[ti][tj] = False
                        ti = ni
                        tj = nj
                    elif puzzle[ni][nj] == puzzle[ti][tj] and visited[ni][nj] == False and visited[ti][tj] == False:
                        puzzle[ti][tj] = 0
                        puzzle[ni][nj] *= 2
                        visited[ni][nj] = True
                        ti = ni
                        tj = nj
                    else:
                        break
                else:
                    break
    return puzzle


def down(puzzle):
    global di, dj

    visited = [[False] * N for _ in range(N)]
    for i in range(N - 2, -1, -1):
        for j in range(N):
            ti = i
            tj = j
            while True:
                ni = ti + di[1]
                nj = tj + dj[1]
                if 0 <= ni < N and 0 <= nj < N:
                    if puzzle[ni][nj] == 0:
                        puzzle[ni][nj] = puzzle[ti][tj]
                        puzzle[ti][tj] = 0
                        ti = ni
                        tj = nj
                    elif puzzle[ni][nj] == puzzle[ti][tj] and visited[ni][nj] == False and visited[ti][tj] == False:
                        puzzle[ti][tj] = 0
                        puzzle[ni][nj] *= 2
                        visited[ni][nj] = True
                        ti = ni
                        tj = nj
                    else:
                        break
                else:
                    break
    return puzzle               


def left(puzzle):
    global di, dj
    
    visited = [[False] * N for _ in range(N)]
    for j in range(1, N):
        for i in range(N):
            ti = i
            tj = j
            while True:
                ni = ti + di[2]
                nj = tj + dj[2]
                if 0 <= ni < N and 0 <= nj < N:
                    if puzzle[ni][nj] == 0:
                        puzzle[ni][nj] = puzzle[ti][tj]
                        puzzle[ti][tj] = 0
                        ti = ni
                        tj = nj
                    elif puzzle[ni][nj] == puzzle[ti][tj] and visited[ni][nj] == False and visited[ti][tj] == False:
                        puzzle[ti][tj] = 0
                        puzzle[ni][nj] *= 2
                        visited[ni][nj] = True
                        ti = ni
                        tj = nj
                    else:
                        break
                else:
                    break
    return puzzle


def right(puzzle):
    global di, dj

    visited = [[False] * N for _ in range(N)]
    for j in range(N - 2, -1, -1):
        for i in range(N):
            ti = i
            tj = j
            while True:
                ni = ti + di[3]
                nj = tj + dj[3]
                if 0 <= ni < N and 0 <= nj < N:
                    if puzzle[ni][nj] == 0:
                        puzzle[ni][nj] = puzzle[ti][tj]
                        puzzle[ti][tj] = 0
                        ti = ni
                        tj = nj
                    elif puzzle[ni][nj] == puzzle[ti][tj] and visited[ni][nj] == False and visited[ti][tj] == False:
                        puzzle[ti][tj] = 0
                        puzzle[ni][nj] *= 2
                        visited[ni][nj] = True
                        ti = ni
                        tj = nj
                    else:
                        break
                else:
                    break
    return puzzle


def move(puzzle, num):
    global max_num
    
    if num == 0:
        for i in range(N):
            for j in range(N):
                if puzzle[i][j] > max_num:
                    max_num = puzzle[i][j]
        return

    for i in range(4):
        tmp = copy.deepcopy(puzzle)
        if i == 0:
            move(up(tmp), num - 1)
        elif i == 1:
            move(down(tmp), num - 1)
        elif i == 2:
            move(left(tmp), num - 1)
        else:
            move(right(tmp), num - 1)

N = int(sys.stdin.readline())
puzzle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 5
max_num = 0
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
move(puzzle, cnt)
print(max_num)