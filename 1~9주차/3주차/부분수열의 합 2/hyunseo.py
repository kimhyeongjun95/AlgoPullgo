# 시간 초과
import sys

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(1<<N):
    temp = []
    for j in range(N):
        if i & (1<<j):
            temp.append(numbers[j])

    if sum(temp) == S:
        if not temp:
            cnt += 1

print(cnt)