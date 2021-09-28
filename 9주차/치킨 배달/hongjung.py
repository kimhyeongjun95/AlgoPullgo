import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])

result = []
for i in combinations(chicken, M):
    temp_result = []
    for h in house:
        temp_list = []
        for c in i:
            temp = (abs(h[0] - c[0]) + abs(h[1] - c[1]))
            temp_list.append(temp)
        temp_result.append(min(temp_list))
    result.append(sum(temp_result))

print(min(result))



# 처음에는 bfs로 풀었음. 바로 시간초과!
# import sys
# from itertools import combinations
# from collections import deque

# def bfs(start):
#     queue = deque([start])
#     visited = [[-1] * N for _ in range(N)]
#     visited[start[0]][start[1]] = 0
    
#     while queue:
#         x, y = queue.popleft()
#         for d in range(4):
#             ni = x + di[d]
#             nj = y + dj[d]
#             if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
#                 if temp[ni][nj] == 0 or temp[ni][nj] == 1:
#                     queue.append([ni, nj])
#                     visited[ni][nj] = visited[x][y] + 1
#                 elif temp[ni][nj] == 2:
#                     return visited[x][y] + 1
                

# N, M = map(int, sys.stdin.readline().split())

# city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# temp = [[0] * N for _ in range(N)]
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]

# chicken = []
# house = []
# for i in range(N):
#     for j in range(N):
#         if city[i][j] == 2:
#             chicken.append([i, j])
#         if city[i][j] == 1:
#             house.append([i, j])
#             temp[i][j] = 1

# result = []
# for i in combinations(chicken, M):
#     for j in i:
#         temp[j[0]][j[1]] = 2
#     tmp_result = 0
#     for h in house:
#         tmp_result += bfs(h)
#     result.append(tmp_result)
#     for j in i:
#         temp[j[0]][j[1]] = 0

# print(min(result))