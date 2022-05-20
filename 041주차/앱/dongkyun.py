import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bytes = list(map(int, input().split()))
costs = list(map(int, input().split()))
result = sum(costs)

dp = [[0 for _ in range(result+1)] for _ in range(n+1)]
for i in range(1, len(costs)):
    for j in range(len(dp[1])):
        if costs[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-costs[i]] + bytes[i], dp[i-1][j])
        
        if dp[i][j] >= m:
            result = min(result, j)
if m != 0:
    print(result)
else:
    print(0)
    