X = int(input())
dp = [0] + [i for i in range(X)]

for n in range(1, X+1):
    dp[n] = min(dp[n], dp[n-1]+1)  # 3
    if not n % 3:
        dp[n] = min(dp[n], dp[n//3]+1)  # 1
    if not n % 2:
        dp[n] = min(dp[n], dp[n//2]+1)  # 2

print(dp[X])
