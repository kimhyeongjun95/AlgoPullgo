# 백준 17144 미세먼지 안녕!

def spread():
    global arr

    dust = [[0 for _ in range(C)] for _ in range(R)]

    dij = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                cnt = 0
                move_dust = arr[i][j] // 5

                for di, dj in dij:
                    ni, nj = i+di, j+dj

                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        dust[ni][nj] += move_dust
                        cnt += 1
                
                dust[i][j] -= move_dust*cnt
    
    for i in range(R):
        for j in range(C):
            arr[i][j] += dust[i][j]


def clean(m, dxy):
    i = 0
    nx = m
    ny = 0
    temp = 0
    while i < 4:
        nx += dxy[i][0]
        ny += dxy[i][1]

        if nx == m and ny == 0:
            return

        if 0 <= nx < R and 0 <= ny < C:
            temp, arr[nx][ny] = arr[nx][ny], temp
        else:
            nx -= dxy[i][0]
            ny -= dxy[i][1]
            i += 1


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

machine = 0
for i in range(R):
    if arr[i][0] == -1:
        machine = i
        break

for _ in range(T):
    spread()
    
    # 반시계방향
    dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 오위왼아
    clean(machine, dxy)

    # 시계방향
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오아왼위
    clean(machine+1, dxy)

print(sum(map(sum, arr)) + 2)