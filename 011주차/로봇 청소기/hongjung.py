import sys

def cleaning(i, j, d):
    global cnt

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    if area[i][j] == 0:
        area[i][j] = 2
        cnt += 1

    for _ in range(4):
        nd = (d + 3) % 4
        ni = i + di[nd]
        nj = j + dj[nd]
        if area[ni][nj] == 0:
            cleaning(ni, nj, nd)
            return
        d = nd

    nd = (d + 2) % 4
    ni = i + di[nd]
    nj = j + dj[nd]
    if area[ni][nj] == 1:
        return
    cleaning(ni, nj, d)


N, M = map(int, sys.stdin.readline().split())
r, c, direction = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0
cleaning(r, c, direction)

print(cnt)