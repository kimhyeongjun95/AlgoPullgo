# 백준 14499 주사위 굴리기

# N x M 지도
# 처음 주사위에는 모든 면에 0이 적혀져 있음.
# 0 -> 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
# !0 -> 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사 
#       칸에 쓰여 있는 수는 0이 된다.

# 주사위가 이동할 때마다 상단에 쓰여 있는 값 구하기
# 바깥으로 이동시키려고 하는 경우, 해당 명령 무시

# 동서북남 : 1234

def rotate(order):
    ndice = [0] * 6
    if order == 0: # 동
        ndice[0] = dice[0]
        ndice[5] = dice[1]
        ndice[2] = dice[2]
        ndice[4] = dice[3]
        ndice[1] = dice[4]
        ndice[3] = dice[5]
    elif order == 1: # 서
        ndice[0] = dice[0]
        ndice[4] = dice[1]
        ndice[2] = dice[2]
        ndice[5] = dice[3]
        ndice[3] = dice[4]
        ndice[1] = dice[5]
    elif order == 2: # 북
        ndice[3] = dice[0]
        ndice[0] = dice[1]
        ndice[1] = dice[2]
        ndice[2] = dice[3]
        ndice[4] = dice[4]
        ndice[5] = dice[5]
    elif order == 3: # 남
        ndice[1] = dice[0]
        ndice[2] = dice[1]
        ndice[3] = dice[2]
        ndice[0] = dice[3]
        ndice[4] = dice[4]
        ndice[5] = dice[5]

    for i in range(6):
        dice[i] = ndice[i]

# 동서북남
dxy = [(0 ,1), (0, -1), (-1, 0), (1, 0)]
dice = [0] * 6
n, m, x, y, k = map(int, input().split())
floor = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

for order in orders:
    order -= 1
    nx = x + dxy[order][0]
    ny = y + dxy[order][1]
    if -1 < nx < n and -1 < ny < m:
        rotate(order)

        if floor[nx][ny] == 0:
            floor[nx][ny] = dice[3]
        else:
            dice[3] = floor[nx][ny]
            floor[nx][ny] = 0
        x = nx
        y = ny
        print(dice[1])