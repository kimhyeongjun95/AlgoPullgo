# 백준 1463 1로 만들기

# 메모이제이션
# 1. %3 == 0, //3
# 2. %2 == 0, //2
# 3. -1

# 1로 만들 때 연산을 사용하는 횟수의의 최솟값
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)	

for i in range(2, n+1): # i: 2~10
    # 이거를 먼저하고
    # 이전 숫자보다 + 1
    d[i] = d[i-1] + 1 # d[i]: 1, 2, 2, 3...
    
    # 해당하는 것 중 최솟값 갱신
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)	
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[n])

# print(d)
# for i in range(11):
#     print(d[i], i)