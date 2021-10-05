# 평범한 배낭

def dp(bag,N,K):
    for i in range(1, N):
        for j in range(1, K+1):
            if j >= lst[i][0]:
                bag[i][j] = max(lst[i][1]+bag[i-1][j-lst[i][0]], bag[i-1][j])
            else:
                bag[i][j] = bag[i-1][j]
    
    ans = 0
    for i in range(N):
        if bag[i][K] > ans:
            ans = bag[i][K]
    return ans

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
bag = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(lst[0][0], K+1):
    bag[0][i] = lst[0][1]

print(dp(bag,N,K))
