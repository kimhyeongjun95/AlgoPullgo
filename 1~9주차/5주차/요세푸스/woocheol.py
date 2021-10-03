# 백준 문제번호 1158번 요세푸스 문제

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = deque([i+1 for i in range(N)])
k = 1
ans = []
while arr:
    if k == M:
        k = 1
        ans.append(arr.popleft())
    else:
        k += 1
        arr.append(arr.popleft())
print("<", ", ".join(map(str, ans)), end=">", sep="")
