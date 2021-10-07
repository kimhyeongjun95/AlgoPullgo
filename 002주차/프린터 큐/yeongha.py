from collections import deque
T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    lst = deque(map(int,input().split()))
    target = deque(0 for _ in range(N))
    target[K]=1
    temp = 0
    while sum(target):
        if lst[0] == max(lst):
            lst.popleft()
            target.popleft()
            temp+=1
        else : 
            lst.append(lst.popleft())
            target.append(target.popleft())
    print(temp)