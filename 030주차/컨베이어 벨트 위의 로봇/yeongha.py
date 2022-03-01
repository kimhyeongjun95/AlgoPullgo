from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
belt = deque(list(map(int, sys.stdin.readline().split())))
print(belt[1:3])

# n = 1
# boxs = deque([0 for _ in range(N)])
# while True:
#     belt.appendleft(belt.pop())
#     boxs.pop()
#     boxs.appendleft(0)
#     boxs[-1] = 0

#     for i in range(N-2, -1, -1):
#         if boxs[i] and not boxs[i+1] and belt[i+1]:
#             boxs[i+1] = 1
#             belt[i+1] -= 1
#             boxs[i] = 0
#     boxs[-1] = 0

#     if belt[0] and not boxs[0]:
#         boxs[0] = 1
#         belt[0] -= 1
  
#     if belt.count(0) >= K :
#         break
    
#     n += 1

# print(n)