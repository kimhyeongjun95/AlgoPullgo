# if 폭발 문자열 in 문자열:
#     모든 폭발 문자열 -> 폭발
#     남은 문자열 새로 이어붙임.
#     새로 생긴 문자열이 폭발 문자열일수도

# 남아 있는 문자가 없으면 'FRULA'

# 방법 
# 1: 리스트로 remove
# 2. 문자열 슬라이싱
# 3. 2중 반복문?

import sys

s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []
for i in s:
    stack.append(i)
    # print(''.join(stack[-len(bomb):]))
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')