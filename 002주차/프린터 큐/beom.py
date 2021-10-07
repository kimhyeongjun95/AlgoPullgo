import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    imp_list = deque(list(map(int, input().split())))
    check = deque([i for i in range(N)])
    checked = check[M]
    count = 0
    
    while True:
        if imp_list[0] == max(imp_list):
            count += 1

            if check[0] == checked:
                print(count)
                break
            imp_list.popleft()
            check.popleft()
        else:
            imp_list.append(imp_list.popleft())
            check.append(check.popleft())
