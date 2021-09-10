# 백준 11279 최대 힙

import sys
import heapq

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    num = int(sys.stdin.readline())
    
    if num:
        heapq.heappush(arr, -num) # heapq는 최소힙을 지원하므로 -num
    else:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)