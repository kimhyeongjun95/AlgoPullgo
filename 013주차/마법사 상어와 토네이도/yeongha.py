lst = [(-1,1,1),(1,1,1),(-2,0,2),(-1,0,7),(1,0,7),(2,0,2),(-1,-1,10),(1,-1,10),(0,-2,5),(0,-1, 0)]
t_lst = [(0,1,[1,1]),(1,0,[-1,-1]), (0,1,[1,-1]), (1,0,[1,1])]

def wind(x, y, t):
    global total
    r = sand
    i, j, txy = t_lst[t]
    for item in lst:
        dx, dy = item[i]*txy[0], item[j]*txy[1]
        nx, ny = x + dx, y + dy

        if item[2] == 0:
            s = r
        else:
            s = (sand*item[2])//100
            r -= s

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            total += s
        else:
            A[nx][ny] += s
    

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
total = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = N//2, N//2
t = 0
for i in range(1, N):
    if i == N-1:
        c = 3
    else:
        c = 2
    for _ in range(c):
        for _ in range(i):
            x, y = x + dx[t], y + dy[t]
            sand = A[x][y]
            A[x][y] = 0
            wind(x, y, t)
        t = (t+1)%4
print(total)
        

        