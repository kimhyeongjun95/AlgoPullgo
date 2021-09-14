# 최대힙

import sys
import heapq as hq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X :
        hq.heappush(heap,(-X,X))
    else:
        if len(heap)>=1:print(hq.heappop(heap)[1])
        else:print(0)