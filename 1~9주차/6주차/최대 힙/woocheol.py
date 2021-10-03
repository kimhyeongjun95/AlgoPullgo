# 11279번 최대 힙
import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp:
        heapq.heappush(heap, (-temp, temp))
    else:
        print(heapq.heappop(heap)[1]) if heap else print(0)
