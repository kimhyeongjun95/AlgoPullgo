from collections import deque

t = int(input())

for i in range(t):
    # 1 0
    # 5 -> 1
    # 4 2
    # 1 2 3 4
    # 2 -> 2
    n, where = map(int, input().split())
    imp = deque(list(map(int, input().split())))
    
    cnt = 0
    while True:
        if imp[0] == max(imp) and where == 0: # 첫번째가 max이고 key일때
            cnt += 1
            break

        elif imp[0] == max(imp) and where != 0: # 첫번째가 max이지만 key가 아닐때
            imp.popleft()
            where -= 1
            cnt += 1
        
        elif imp[0] != max(imp) and where == 0: # 첫번째가 max가 아니지만 key일때
            popped = imp.popleft()
            imp.append(popped)
            where = len(imp) - 1

        elif imp[0] != max(imp) and where != 0: # 첫번째가 max가 아니고 key도 아닐 때
            popped = imp.popleft()
            imp.append(popped)
            where -= 1
    
    print(cnt)