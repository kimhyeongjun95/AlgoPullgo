# 백준 20057 마법사 상어와 토네이도

def spread(x, y, sand):
    global arr, result

    if 0 <= x < N and 0 <= y < N:
        arr[x][y] += sand
    else:
        result += sand


def tornado(x ,y):
    # (x, y) : 그림 상의 x

    dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 왼 아 오 위
    cnt = 2
    i = 4

    while True:
        for _ in range(cnt//2):
            nx = x + dxy[i%4][0]
            ny = y + dxy[i%4][1]
            # (nx, ny) : 그림 상의 y

            temp = arr[nx][ny]
            # 1%
            spread(x + dxy[(i-1)%4][0], y + dxy[(i-1)%4][1], int(temp*0.01))
            spread(x + dxy[(i+1)%4][0], y + dxy[(i+1)%4][1], int(temp*0.01))
            # 7%
            spread(nx + dxy[(i-1)%4][0], ny + dxy[(i-1)%4][1], int(temp*0.07))
            spread(nx + dxy[(i+1)%4][0], ny + dxy[(i+1)%4][1], int(temp*0.07))
            # 2%
            spread(nx + dxy[(i-1)%4][0]*2, ny + dxy[(i-1)%4][1]*2, int(temp*0.02))
            spread(nx + dxy[(i+1)%4][0]*2, ny + dxy[(i+1)%4][1]*2, int(temp*0.02))
            # 10%
            spread(nx + dxy[i%4][0] + dxy[(i-1)%4][0], ny + dxy[i%4][1] + dxy[(i-1)%4][1], int(temp*0.1))
            spread(nx + dxy[i%4][0] + dxy[(i+1)%4][0], ny + dxy[i%4][1] + dxy[(i+1)%4][1], int(temp*0.1))
            # 5%
            spread(nx + dxy[i%4][0]*2, ny + dxy[i%4][1]*2, int(temp*0.05))
            # a
            left = temp - int(temp*0.01)*2 - int(temp*0.07)*2 - int(temp*0.02)*2 - int(temp*0.1)*2 - int(temp*0.05)
            spread(nx + dxy[i%4][0], ny + dxy[i%4][1], left)

            arr[nx][ny] = 0

            if nx == 0 and ny == 0:
                return
            else:
                x, y = nx, ny

        i += 1
        cnt += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
tornado(N//2, N//2)

print(result)