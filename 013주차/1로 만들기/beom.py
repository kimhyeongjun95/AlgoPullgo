# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)


# def make_one(N):
#     if N == 1:
#         return 0

#     if dp[N] > 0:
#         return dp[N]
#     dp[N] = make_one(N-1) + 1

#     if N % 2 == 0:
#         temp = make_one(N//2) + 1 
#         if dp[N] > temp:
#             dp[N] = temp

#     if N % 3 == 0:
#         temp = make_one(N//3) + 1
#         if dp[N] > temp:
#             dp[N] = temp

#     return dp[N]


# N = int(input())
# dp = [0 for _ in range(N + 1)]
# print(make_one(N))

N = int(input())
dp = [0 for _ in range(N + 1)]
dp[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
print(dp[N])

