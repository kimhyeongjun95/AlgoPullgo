# 백준 9935 문자열 폭발

import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
n = len(bomb)

stack = []

for s in string:
    if s == bomb[-1]:
        stack.append(s)

        if len(stack) >= n:
            for i in range(-1, -n-1, -1):
                if stack[i] != bomb[i]:
                    break
            else:
                for _ in range(n):
                    stack.pop()
    else:
        stack.append(s)

answer = ''
if stack:
    for s in stack:
        answer += s
else:
    answer = 'FRULA'

print(answer)