import sys
input = sys.stdin.readline


N = int(input())
T_lst = []
P_lst = []
dp = [0] * (N + 1)

for i in range(N):
    T, P = map(int, input().split())
    T_lst.append(T)
    P_lst.append(P)

for i in range(N - 1, -1, -1):
    if T_lst[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(P_lst[i] + dp[i + T_lst[i]], dp[i + 1])
        # 일을 맡았을 때 들어오는 보상 + 일을 끝낸 다음에 쌓여있는 보상
        # 일을 맡지 않았을 때 그 다음의 보상
print(dp[0])
