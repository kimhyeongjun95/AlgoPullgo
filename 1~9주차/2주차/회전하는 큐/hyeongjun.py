# 10
# 2 9 5
# 1 2 3 4 5 6 7 8 9 10 -> 2와 9와 5를 빼야한다 (처음 큐에서의 위치)
# /2 3 4 5 6 7 8 9 10 1
# 3 4 5 6 7 8 9 10 1
# /1 3 4 5 6 7 8 9 10
# /10 1 3 4 5 6 7 8 9
# /9 10 1 3 4 5 6 7 8
# 10 1 3 4 5 6 7 8
# /1 3 4 5 6 7 8 10
# /3 4 5 6 7 8 10 1
# /4 5 6 7 8 10 1 3
# /5 6 7 8 10 1 3 4
# 6 7 8 10 1 3 4
# -> 총 8번

from collections import deque
import copy
import sys

n, m = map(int, sys.stdin.readline().split())
finds = map(int, sys.stdin.readline().split())

ready = deque([i for i in range(1, n+1)])
result = 0

for x in finds:
    ready2 = copy.copy(ready) # 제대로 복사하기 위함. (copy.deepcopy)런타임 에러 (copy.copy) 통과
    ready3 = copy.copy(ready)
    count2 = 0
    count3 = 0
    for i in range(len(ready)): # 왼쪽으로 가는 2번
        if ready2[0] == x:
            ready2.popleft()
            # print(ready)
            break
        
        popped = ready2.popleft()
        ready2.append(popped)
        count2 += 1

    for i in range(len(ready)): # 오른쪽으로 가는 3번
        if ready3[0] == x:
            ready3.popleft()
            # print(ready)
            break

        popped = ready3.pop()
        ready3.appendleft(popped)
        count3 += 1

    # 두 가지 경우 수를 생각해야하기 때문에 count가 낮으면 그 ready(숫자) 큐를 ready(기본)에 할당한다. 
    if count2 < count3:
        ready = ready2
        result += count2
    else:
        ready = ready3
        result += count3

    # print(count2)
    # print(count3)
    # print(result)
    
print(result)ㄴ