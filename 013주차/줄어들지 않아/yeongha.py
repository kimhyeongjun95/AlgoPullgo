T = int(input())
dp = [[1 for _ in range(10)] for _ in range(64)]

for i in range(1, 64):
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]

for _ in range(T):
    N = int(input())
    print(sum(dp[N-1]))

