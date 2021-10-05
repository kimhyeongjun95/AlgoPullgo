# 백준 1010 다리 놓기 : 조합

# def combination(n, r):
#     temp = n-r

#     son = 1
#     while n:
#         son *= n
#         n -= 1
    
#     mom = 1
#     while temp:
#         mom *= temp
#         temp -= 1

#     while r:
#         mom *= r
#         r -= 1
    
#     return son//mom


def combination(n, r):
    temp = r
    if n-r < r:
        temp = n-r

    son = 1
    for _ in range(temp):
        son *= n
        n -= 1
    
    mom = 1
    for _ in range(temp):
        mom *= temp
        temp -= 1
    
    return son//mom


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    print(combination(M, N))