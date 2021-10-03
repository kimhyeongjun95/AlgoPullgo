from collections import deque

N, K = map(int,input().split())
lst = deque(map(int,input().split()))
deq = deque(i+1 for i in range(N))
temp = 0

while lst :
    if deq[0] == lst[0]:
        deq.popleft()
        lst.popleft()
    else:
        if deq.index(lst[0]) <= len(deq)//2:
            deq.append(deq.popleft())
        else: 
            deq.appendleft(deq.pop())
        temp += 1
        
print(temp)