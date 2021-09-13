# 0이 들어오면 가장 큰값 출력, 배열에서 제거 // 0배열이 비어있으면 0 출력
# x가 자연수라면 배열에 x라는 값을 넣는 연산. 

# n = int(input())
# arr = []
# for _ in range(n):
#     x = int(input())

#     if x > 0:
#         arr.append(x)
#     else: # 0이라면
#         if arr:
#             print(arr)
#             print(arr.pop(arr.index(max(arr))))
#         else:
#             print(0)

# 힙을 구현해야되나보다

import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap: # 가장 큰값 출력하고 배열에서 제거하기
            print(heapq.heappop(heap)[1]) # (x, x)
        else: 
            print(0)
    else: # 0이 아닐때
        heapq.heappush(heap, (-x, x))
    # heapq.heappush(heap, (-x, x))
    # print(heap)
