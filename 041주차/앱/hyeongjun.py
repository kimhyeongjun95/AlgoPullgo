# 백준 7579 앱

# 메모리
# 메모리부터 앱 삭제, "비활성화"

# 앱A[i]는 m[i]만큼 메모리 사용
# 비활성화 -> 다시 실행하고자 했을때 비용 c[i]
# 앱 B를 실행, 추가의 M 바이트의 메모리 필요

# N개의 앱
# 앱 비활성화의 최소 비용 계산

n, m = map(int, input().split())
memories = list(map(int, input().split()))
disable = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)]]
cost = -1

while max(dp[cost]) < m:
    dp.append([0 for _ in range(n+1)])
    # 최소 비용
    cost += 1

    for i in range(n):
        if disable[i] <= cost:
            dp[cost][i+1] = max(dp[cost - disable[i]][i] + memories[i], dp[cost][i])
        else:
            dp[cost][i+1] = dp[cost][i]

for i in dp:
    print(i)
print(cost)