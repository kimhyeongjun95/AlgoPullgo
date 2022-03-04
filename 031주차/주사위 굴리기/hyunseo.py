# 백준 14499 주사위 굴리기

N, M, x, y, K = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))
dxy = [(1, 0), (0, 1), (0, -1), (-1, 0)] # 남(4) 동(1) 서(2) 북(3)

dise = [0 for _ in range(6)] # 바닥면 인덱스 : 5

for c in cmd:
    # 맵에서 주사위 이동
    dx, dy = dxy[c%4]
    nx, ny = x+dx, y+dy
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
    else:
        continue

    # 바닥면 갱신
    if c == 1: # 동
        dise[0], dise[5], dise[3], dise[2] = dise[3], dise[2], dise[5], dise[0]
    elif c == 2: # 서
        dise[0], dise[5], dise[3], dise[2] = dise[2], dise[3], dise[0], dise[5]
    elif c == 3: # 북
        dise[1], dise[0], dise[4], dise[5] = dise[0], dise[4], dise[5], dise[1]
    elif c == 4: # 남
        dise[1], dise[0], dise[4], dise[5] = dise[5], dise[1], dise[0], dise[4]

    if grid[x][y]:
        dise[5] = grid[x][y]
        grid[x][y] = 0
    else:
        grid[x][y] = dise[5]

    print(dise[0])