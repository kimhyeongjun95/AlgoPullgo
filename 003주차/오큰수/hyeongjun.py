# 백준 17298 오큰수
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
result = [-1 for _ in range(n)]
stack = []
for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i]:
        result[stack.pop()] = numbers[i]
    stack.append(i)
print(*result)