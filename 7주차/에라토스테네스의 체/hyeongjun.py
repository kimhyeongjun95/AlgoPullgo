# 2960 에라토스테네스의 체

# 7 3
# 2 3 4 5 6 7
# 2, 4, 6 -> 3번째
# -> 6

# 15 12
# 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 2, 4, 6, 8, 10, 12, 14 -> 7개 나감
# 3, 9, 15 -> 3개 나감 총 10개
# 5, 7 -> 12개째

import sys
# 헤맨 이유: 에라토스테네스 체를 이용해소수를 찾는 문제라기보다
#            이용해 숫자를 지워주는 문제..
def eratos(n, k):
    count = 0
    idx = 0
    for i in range(2, n+1): # 제곱근만큼만 해주면 됨

        if arr[i]: # True라면(소수라면)
            j = 1 # 배수
            while i * j <= n:
                idx = i*j
                if arr[idx]: # 배수지만 중복방지
                    arr[idx] = False
                    count += 1
                    if count == k:
                        return idx
                j += 1
       
n, k = map(int, sys.stdin.readline().split())

arr = [True for i in range(n+1)]
answer = eratos(n, k)
print(answer)