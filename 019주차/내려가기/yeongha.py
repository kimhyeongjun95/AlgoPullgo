import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
numbers = list(map(int, input().split()))
max_dp[0], max_dp[1], max_dp[2] = numbers[0], numbers[1], numbers[2]
min_dp[0], min_dp[1], min_dp[2] = numbers[0], numbers[1], numbers[2]
for _ in range(1, N):
    numbers = list(map(int,input().split()))
    max_dp[0], max_dp[1], max_dp[2] = numbers[0] + max(max_dp[0], max_dp[1]), numbers[1] + max(max_dp[0], max_dp[1], max_dp[2]), numbers[2] + max(max_dp[1], max_dp[2])
    min_dp[0], min_dp[1], min_dp[2] = numbers[0] + min(min_dp[0], min_dp[1]), numbers[1] + min(min_dp[0], min_dp[1], min_dp[2]), numbers[2] + min(min_dp[1], min_dp[2])

print(max(max_dp), min(min_dp))