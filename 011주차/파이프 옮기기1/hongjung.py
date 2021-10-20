import sys

def dfs(i, j, d):
    # 0, 1, 2 == 가로, 세로, 대각 순서
    global cnt

    if i == N - 1 and j == N - 1:
        cnt += 1
        return

    if i + 1 < N and j + 1 < N:
        if house[i][j+1] == 0 and house[i+1][j+1] == 0 and house[i+1][j] == 0:
            dfs(i + 1, j + 1, 2)

    if d == 0 or d == 2:
        if j + 1 < N:
            if house[i][j+1] == 0:
                dfs(i, j + 1, 0)

    if d == 1 or d == 2:
        if i + 1 < N:
            if house[i+1][j] == 0:
                dfs(i + 1, j, 1)


N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0
dfs(0, 1, 0)

print(cnt)






# import sys 90%에서 시간초과(pypy)

# def dfs(i, j, d):
#     stack = [[i, j, d]]
 
#     cnt = 0
#     while stack:
#         x, y, d = stack.pop()
#         if x == N - 1 and y == N - 1:
#             cnt += 1
#             continue
#         for k in range(3):
#             ni = x + di[k]
#             nj = y + dj[k]
#             if ni < N and nj < N:
#                 if d == 0 and k != 1:
#                     if k == 0 and house[ni][nj] == 0:
#                         stack.append([ni, nj, k])
#                     elif k == 2:
#                         if house[x+di[0]][y+dj[0]] == 0 and house[x+di[1]][y+dj[1]] == 0 and house[x+di[2]][y+dj[2]] == 0:
#                             stack.append([ni, nj, k])

#                 elif d == 1 and k != 0:
#                     if k == 1 and house[ni][nj] == 0:
#                         stack.append([ni, nj, k])
#                     elif k == 2:
#                         if house[x+di[0]][y+dj[0]] == 0 and house[x+di[1]][y+dj[1]] == 0 and house[x+di[2]][y+dj[2]] == 0:
#                             stack.append([ni, nj, k])

#                 elif d == 2:
#                     if k == 0 and house[ni][nj] == 0:
#                         stack.append([ni, nj, k])
#                     elif k == 1 and house[ni][nj] == 0:
#                         stack.append([ni, nj, k])
#                     elif k == 2:
#                         if house[x+di[0]][y+dj[0]] == 0 and house[x+di[1]][y+dj[1]] == 0 and house[x+di[2]][y+dj[2]] == 0:
#                             stack.append([ni, nj, k])
#     return cnt
                    

# N = int(sys.stdin.readline())

# house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# di = [0, 1, 1] # 가로 세로 대각선
# dj = [1, 0, 1]

# print(dfs(0, 1, 0))