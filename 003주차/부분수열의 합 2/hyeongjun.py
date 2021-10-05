import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

result = []

for i in range(1, n+1):
    for j in list(combinations(numbers, i)):
        if sum(j) == s:
            result.append(j)

print(len(result))