# 내려가기
import sys
input = sys.stdin.readline
N = int(input())

max_dp = []
min_dp = []
for i in range(N):
    temp = list(map(int, input().split()))
    if i == 0:
        max_dp = [temp[0], temp[1], temp[2]]
        min_dp = [temp[0], temp[1], temp[2]]
        continue
    max_one = temp[0] + max(max_dp[:2])
    min_one = temp[0] + min(min_dp[:2])

    max_two = temp[1] + max(max_dp)
    min_two = temp[1] + min(min_dp)

    max_three = temp[2] + max(max_dp[1:])
    min_three = temp[2] + min(min_dp[1:])

    max_dp = [max_one, max_two, max_three]
    min_dp = [min_one, min_two, min_three]


print(max(max_dp), min(min_dp))
