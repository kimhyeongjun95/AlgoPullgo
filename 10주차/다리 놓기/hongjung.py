import sys

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    up = factorial(M)
    down = factorial(N) * factorial(M-N)

    cnt = up // down
    print(cnt)





# import sys 시간초과
# from itertools import combinations

# T = int(sys.stdin.readline())

# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split())

#     M_list = combinations(list(range(M)), N)
#     cnt = 0
#     for i in M_list:
#         for j in range(N-1):
#             if i[j] > i[j+1]:
#                 break
#         else:
#             cnt += 1
    
#     print(cnt)
                


# import sys 시간초과

# def bridge(n):
#     global M_list
#     global result

#     if sum(M_list) == N:
#         result += 1
#         return
#     for i in range(n, M):
#         M_list[i] = 1
#         bridge(i+1)
#         M_list[i] = 0
        

# T = int(sys.stdin.readline())

# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split())

#     M_list = [0 for _ in range(M)]
#     result = 0
#     bridge(0)
#     print(result)