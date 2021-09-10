# 12865번 평범한 배낭
import pprint

N, K = map(int, input().split())
weight, price = [], []
for _ in range(N):
    w, p = map(int, input().split())
    weight.append(w)
    price.append(p)

ans = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(1, K+1):
        if weight[i-1] <= w:
            ans[i][w] = max(price[i-1] + ans[i-1]
                            [w - weight[i-1]], ans[i-1][w])
        else:
            ans[i][w] = ans[i-1][w]

pprint.pprint(ans)

print(ans[N][K])


'''
# pseudo code
for w = 0 to W
    b[0, w] = 0
for i = 0 to N
    b[i, 0] = 0
    for w = 0 to W
        if w_i <= w
            if b_i + b[i-1, w-w_i] > b[i - 1, w]
                b[i, w] = b_i + b[i-1, w-w_i]
            else
                b[i, w] = b[i-1, w]
        else
            b[i, w] = b[i-1, w]
'''
