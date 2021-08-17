import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(1, 1 << N):
    result = []
    
    for j in range(N):
        if i & (1 << j):
            result.append(arr[j])
    if sum(result) == S:
        count += 1

print(count)