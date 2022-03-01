from collections import deque
def bfs(B_start, R_start):
    dxy = [(1,0), (-1,0), (0,1), (0,-1)]
    B_deq = deque([(B_start[0], B_start[1], 0)])
    R_deq = deque([(R_start[0], R_start[1], 0)])

    while B_deq and R_deq:
        B_x, B_y, d = B_deq.popleft()
        R_x, R_y, d = R_deq.popleft()
        if d == 10:
            return -1
        
        flag = False
        for dx, dy in dxy:
            B_cnt = 0
            B_nx, B_ny = B_x, B_y
            while True:
                B_nx, B_ny = B_nx + dx, B_ny + dy
                if (B_nx, B_ny) == hole:
                    flag = True
                    continue
                if board[B_nx][B_ny] == '#':
                    B_nx, B_ny = B_nx - dx, B_ny - dy
                    break
                B_cnt += 1

            if flag:
                flag = False
                continue

            R_cnt = 0
            R_nx, R_ny = R_x, R_y
            while True:
                R_nx, R_ny = R_nx + dx, R_ny + dy
                if (R_nx, R_ny) == hole:
                    return d + 1
                if board[R_nx][R_ny] == '#':
                    R_nx, R_ny = R_nx - dx, R_ny - dy
                    if (R_nx, R_ny) == (B_nx, B_ny):
                        if B_cnt < R_cnt:
                            R_nx, R_ny = R_nx - dx, R_ny - dy
                        else:
                            B_nx, B_ny = B_nx - dx, B_ny - dy
                    if (R_nx, R_ny) != (R_x, R_y) or (B_nx, B_ny) != (B_x, B_y):
                        R_deq.append((R_nx, R_ny, d+1))
                        B_deq.append((B_nx, B_ny, d+1))
                    break
                R_cnt += 1
    return -1

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            B_start = (i, j)
        elif board[i][j] == 'R':
            R_start = (i, j)
        elif board[i][j] == 'O':
            hole = (i, j)
print(bfs(B_start, R_start))
