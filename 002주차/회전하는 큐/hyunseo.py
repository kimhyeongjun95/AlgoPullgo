import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
index = list(map(int, sys.stdin.readline().split()))

que = deque(n for n in range(1, N+1))

def left(que) :
    temp = que.popleft()
    que.append(temp)
    return que

def right(que) :
    temp = que.pop()
    que.appendleft(temp)
    return que

cnt = 0
i = 0
while i < len(index) :

    if que[0] == index[i] :
        que.popleft()
    else :
        if que.index(index[i]) <= len(que)//2 :
            while que[0] != index[i] :
                left(que)
                cnt += 1
            que.popleft()
        else :
            while que[0] != index[i] :
                right(que)
                cnt +=1
            que.popleft()
            
    i += 1

print(cnt)