# 시간제한 1초 / 시간초과
# break 추가

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

answer = []

for i in range(len(numbers)-1): # 1. 마지막은 무조건 -1이기에
    result = []

    for x in numbers[i+1:]: # 2.  len(numbers)-1을 안하면 인덱싱 에러
        if x > numbers[i]:
            result.append(x)
            break
    
    if len(result) == 0:
        answer.append(-1)
    else:
        answer.append(result[0]) # 가장 numbers[i]와 가까운 값에 있는걸 append하게 됌

    # idx = 0 # 인덱스로 비교해보면
    # while i + idx < len(numbers): # 오른쪽과 비교해서 가장 가까운 큰 숫자를 result 리스트에 append
    #     if numbers[i] < numbers[i+idx]:
    #         result.append(numbers[i])
    #         break
    #     idx += 1

answer.append(-1) # 마지막 인덱스는 무조건 -1

print(*answer)