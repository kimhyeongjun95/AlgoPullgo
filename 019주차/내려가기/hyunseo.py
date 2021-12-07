# 백준 2096 내려가기

# import sys 
# sys.setrecursionlimit(9999999)

# def dfs(x, y, sum):
#     global min_sum, max_sum
    
#     if x == N-1:
#         min_sum = min(min_sum, sum)
#         max_sum = max(max_sum, sum)
#         return

#     for dx, dy in dxy:
#         nx, ny = x+dx, y+dy

#         if 0 <= nx < N and 0 <= ny < 3:
#             dfs(nx, ny, sum+number[nx][ny])


# N = int(input())
# dxy = [(1, -1), (1, 0), (1, 1)]
# number = [list(map(int, input().split())) for _ in range(N)]

# min_sum = float('inf')
# max_sum = 0

# dfs(0, 0, number[0][0])
# dfs(0, 1, number[0][1])
# dfs(0, 2, number[0][2])

# print(max_sum, min_sum)


N = int(input())

max_sum = min_sum = list(map(int, input().split()))

for _ in range(N-1):
    input_num = list(map(int, input().split()))

    max_sum = [input_num[0] + max(max_sum[:2]), input_num[1] + max(max_sum), input_num[2] + max(max_sum[1:])]
    min_sum = [input_num[0] + min(min_sum[:2]), input_num[1] + min(min_sum), input_num[2] + min(min_sum[1:])]

print(max(max_sum), min(min_sum))