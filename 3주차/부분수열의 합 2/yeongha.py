from itertools import combinations
from collections import defaultdict

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left_subset = numbers[:N//2]
right_subset = numbers[N//2:]

left_num = defaultdict(int)
right_num = defaultdict(int)

# 왼쪽 오른쪽 부분집합의 합 리스트 만들기
for i in range(N//2+1):
    for subset in combinations(left_subset, i):
        left_num[sum(subset)] += 1

for i in range(N-N//2+1):
    for subset in combinations(right_subset, i):
        right_num[sum(subset)] += 1

left_sum = sorted(left_num.keys())
right_sum = sorted(right_num.keys())

left = 0
right = len(right_sum) - 1
cnt = 0
while left < len(left_sum) and right >= 0:
    if left_sum[left] + right_sum[right] == S:
        cnt += left_num[left_sum[left]]*right_num[right_sum[right]]
        left += 1
        right -= 1
    elif left_sum[left] + right_sum[right] > S:
        right -= 1
    else:
        left += 1

if S == 0 :
    cnt -= 1 # 공집합 + 공집합인 경우 빼주기 위해

print(cnt)

def two_pointer(lst, target):
    left, right = 0,0
    cnt = 0
    total = 0

    while left < len(lst):
        if total == target:
            cnt += 1
            total -= lst[left]
            left += 1
        elif total > target or right >= len(lst): # 이 부분율 유심히 보길 바란다.
            total -= lst[left]
            left += 1
        elif total < target:
            total += lst[right]
            right += 1

    return cnt
