from copy import deepcopy

def dfs_s(i, j, color):
    global N
    dxy = [(0,1), (1,0), (0,-1), (-1,0)]

    if color in 'RG':
        color = 'RG'

    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        matrix_s[x][y] = '0'
        for dx,dy in dxy:
            nx, ny = x+dx, y+dy

            if -1 < nx < N and -1 < ny < N and matrix_s[nx][ny] in color:
                stack.append((nx, ny))
    return

def dfs(i, j, color):
    global N
    dxy = [(0,1), (1,0), (0,-1), (-1,0)]

    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        matrix[x][y] = '0'
        for dx,dy in dxy:
            nx, ny = x+dx, y+dy

            if -1 < nx < N and -1 < ny < N and matrix[nx][ny] == color:
                stack.append((nx, ny))
    return


N = int(input())
matrix = [list(input()) for _ in range(N)]
matrix_s = deepcopy(matrix)
cnt = cnt_s = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] != '0':
            cnt += 1
            c = matrix[i][j]
            dfs(i, j, c)
        
        if matrix_s[i][j] != '0':
            cnt_s += 1
            c = matrix_s[i][j]
            dfs_s(i, j, c)

print(cnt, cnt_s)