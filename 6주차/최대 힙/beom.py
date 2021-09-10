import heapq
import sys
input = sys.stdin.readline
 
N = int(input())
result = []

for _ in range(N):
    n = int(input())

    if n == 0 and result:
        print(-heapq.heappop(result))
        
    elif n == 0 and len(result) == 0:
        print(0)
        
    else:
        heapq.heappush(result, -n)
 