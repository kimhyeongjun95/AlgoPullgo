# 14501 퇴사
N = int(input())

days = []
cost = []

for _ in range(N):
    a, b = map(int, input().split())
    days.append(a)
    cost.append(b)

dp = [0 for _ in range(N)]

for i in range(N):
    # 지금 날짜부터 주어진 상담을 진행할 수 있다면
    if i + days[i] <= N:
        dp[i] = cost[i]
        for j in range(i):
            if j + days[j] <= i:
                dp[i] = max(dp[i], dp[j] + cost[i])

print(max(dp))
