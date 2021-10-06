import sys
from collections import deque

def bfs(i, j):
    queue = deque([[i, j]])
    temp = [[i, j]]
 
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    if L <= abs(countries[x][y] - countries[ni][nj]) and abs(countries[x][y] - countries[ni][nj]) <= R:
                        visited[ni][nj] = True
                        queue.append([ni, nj])
                        temp.append([ni, nj])
                        
    return temp


N, L, R = map(int, sys.stdin.readline().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

cnt = 0
while True:
    visited = [[False] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                temp = bfs(i, j)
                if len(temp) > 1:
                    flag = True
                    total = 0
                    for t in temp:
                        total += countries[t[0]][t[1]]
                    value = int(total / len(temp))

                    for t in temp:
                        countries[t[0]][t[1]] = value

    if flag == False:
        break

    cnt += 1

print(cnt)




# import sys
# from collections import deque
# import copy

# def search_country():
#     global result
    
#     while True:
#         visited = [[False] * N for _ in range(N)]
#         flag = False
#         for ti in range(N):
#             for tj in range(N):
#                 if visited[ti][tj] == False:
#                     visited[ti][tj] = True
#                     tmp_list = []
#                     if bfs(ti, tj):
#                         tmp_list.append(bfs(ti, tj))
#                         flag = True
#         if flag:
#             result += 1
#             original = copy.deepcopy(countries)
#             for t in tmp_list:
#                 for i in range(N):
#                     for j in range(N):
#                         if original[i][j] != t[i][j]:
#                             countries[i][j] = t[i][j]
#         else:
#             break         


# def bfs(i, j):
#     queue = deque([[i, j]])
#     visited = [[False] * N for _ in range(N)]
#     tmp = copy.deepcopy(countries)

#     while queue:
#         x, y = queue.popleft()
#         for d in range(4):
#             ni = x + di[d]
#             nj = y + dj[d]
#             if 0 <= ni < N and 0 <= nj < N:
#                 if visited[ni][nj] == False:
#                     if abs(tmp[x][y] - tmp[ni][nj]) >= L and abs(tmp[x][y] - tmp[ni][nj]) <= R:
#                         queue.append([ni, nj])
#                         visited[ni][nj] = True
    
#     total = 0
#     cnt = 0
#     for ti in range(N):
#         for tj in range(N):
#             if visited[ti][tj]:
#                 total += tmp[ti][tj]
#                 cnt += 1
#     if total:
#         value = int(total/cnt)
#         for ti in range(N):
#             for tj in range(N):
#                 if visited[ti][tj]:
#                     tmp[ti][tj] = value
#         return tmp
#     else:
#         return 0
    

# N, L, R = map(int, sys.stdin.readline().split())
# countries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
# result = 0

# search_country()

# print(result)