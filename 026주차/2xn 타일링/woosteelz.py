# 프로그래머스 2 X n 타일링 (Level 3)
def solution(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] % 1000000007+dp[i-2] % 1000000007
    return dp[n] % 1000000007
