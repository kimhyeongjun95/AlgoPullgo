# 백준 18405 경쟁적 전염

# N x N 시험관
# 특정한 위치 바이러스 존재

# 모든 바이러스는 1번 ~ K번 까지의 종류 중 하나
# 1초마다 상하좌우로 증식
# 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
# 증식 과정 중 특정한 칸에 이미 다른 바이러스 존재
# -> 들어갈 수 없음

# S초가 지난 후 (X, Y)에 존재하는 바이러스의 종류 출력
# 해당 위치에 바이러스 존재 X => return 0
# 가장 왼쪽 위 (1, 1)

# 1. K개의 바이러스 위치 저장
# 2. time caculate
# 3. 각각 방향 spread
# 4. S초 후 (X, Y) 출력

# import sys
# input = sys.stdin.readline
# from collections import deque

# dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# n, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# S, target_x, target_y = map(int, input().split())

# # 2
# for _ in range(S):
    
#     for virus in range(1, k+1):
#         location = deque([])
#         for i in range(n):
#             for j in range(n):
#                 if arr[i][j] == virus:
#                     # 1
#                     location.append((i, j))
#         while location:
#             x, y = location.popleft()
#             # 3
#             for dx, dy in dxy:
#                 nx = x + dx
#                 ny = y + dy
#                 if -1 < nx < n and -1 < ny < n and arr[nx][ny] == 0:
#                     arr[nx][ny] = arr[x][y]
# # 4
# print(arr[target_x-1][target_y-1])


# 1. deque location [종류, 시간, 위치x, 위치y] 저장
# 2. nx ny 중 0이면 append
# 3. 시간 == S에 도달하면 멈춤
# 4. 마지막 x, y 위치 구하기

import sys
input = sys.stdin.readline
from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
S, target_x, target_y = map(int, input().split())

location = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            # 1
            location.append((arr[i][j], 0, i, j))

location.sort()
location = deque(location)

while location:
    virus, time, x, y = location.popleft()
    if time == S:
        break

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if -1 < nx < n and -1 < ny < n:
            if arr[nx][ny] == 0:
                arr[nx][ny] = virus
                location.append((virus, time + 1, nx, ny))

print(arr[target_x-1][target_y-1])