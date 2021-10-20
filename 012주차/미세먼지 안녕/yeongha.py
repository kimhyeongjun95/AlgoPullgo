R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
dxy = [(1,0),(0,1),(-1,0),(0,-1)]

for _ in range(T):
    dust = [[0 for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if matrix[x][y] > 0:
                dustwind = matrix[x][y]//5
                cnt = 0
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if -1 < nx < R and -1 < ny < C and matrix[nx][ny] != -1:
                        dust[nx][ny] += dustwind
                        cnt += 1
                dust[x][y] -= dustwind*cnt
 
    cleaner_x = 0
    for x in range(R):
        for y in range(C):
            matrix[x][y] += dust[x][y]
            if matrix[x][y] == -1 and cleaner_x == 0:
                cleaner_x = x

    # 공기청정기 줄 이동
    temp1 = matrix[cleaner_x].pop()
    temp2 = matrix[cleaner_x + 1].pop()
    matrix[cleaner_x].insert(1,0)
    matrix[cleaner_x + 1].insert(1,0)

    # 맨 오른쪽 이동
    for i in range(cleaner_x-1, -1, -1):
        matrix[i][-1], temp1 = temp1, matrix[i][-1]
    for i in range(cleaner_x+2, R):
        matrix[i][-1], temp2 = temp2, matrix[i][-1]

    # 맨위, 맨아래 줄 이동
    for j in range(C-2, -1 , -1):
        matrix[0][j], temp1 = temp1, matrix[0][j]
        matrix[R-1][j], temp2 = temp2, matrix[R-1][j]

    # 맨 왼쪽 이동
    for i in range(1, cleaner_x):
        matrix[i][0], temp1 = temp1, matrix[i][0]
    for i in range(R-2, cleaner_x + 1, -1):
        matrix[i][0], temp2 = temp2, matrix[i][0]

ans = 0
for x in range(R):
    ans += sum(matrix[x])
print(ans+2)








