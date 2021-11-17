# 2688번 줄어들지 않아
dp = []
dp.append([1 for _ in range(10)])
dp.append([10-i for i in range(10)])

for n in range(2, 64):
    temp = [sum(dp[n-1])]
    for i in range(10):
        temp.append(temp[-1] - dp[n-1][i])
    dp.append(temp)


for _ in range(int(input())):
    N = int(input())
    print(sum(dp[N-1]))
