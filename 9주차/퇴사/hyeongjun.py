
# 백준 1339 퇴사

# N일동안 최대한 많은 상담


#  	    1일	2일	3일	4일	5일	6일	7일
# Ti	3	5	1	1	2	4	2
# Pi	10	20	10	20	15	40	200

# 1일, 4일, 5일에 상담 : 최적의 해
# 10+20+15 = 45

# 퇴사 전 최대 수익 구하기

import sys
input = sys.stdin.readline

n = int(input())
day = []
income = []
dp = [0] * (n+1)
for _ in range(n):
    how_long, money = map(int, input().split())
    day.append(how_long)
    income.append(money)

for i in range(n-1, -1, -1):
    if i + day[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], income[i] + dp[day[i] + i])

print(dp[0])