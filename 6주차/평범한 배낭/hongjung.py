import sys

N, K = map(int, sys.stdin.readline().split()) # 물품 수, 무게

bag = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 무게, 가치 순서

check = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = bag[i][0] # 무게
        v = bag[i][1] # 가치
        if w <= j:
            check[i][j] = max(check[i-1][j], v + check[i-1][j-w])
        else:
            check[i][j] = check[i-1][j]

print(max(max(check)))






# import sys
# from itertools import combinations

# N, K = map(int, sys.stdin.readline().split()) # 물품 수, 무게

# bag = [] # 무게, 가치 순서
# for _ in range(N):
#     tmp = list(map(int, sys.stdin.readline().split()))
#     if tmp[0] <= K and tmp[1] != 0:
#         bag.append(tmp)

# result = 0
# for i in range(1, len(bag)+1):
#     for j in combinations(bag, i):
#         tmp1 = 0
#         tmp2 = 0
#         for k in j:
#             tmp1 += k[0]
#             tmp2 += k[1]
#         if tmp1 <= K and tmp2 > result:
#             result = tmp2

# print(result)