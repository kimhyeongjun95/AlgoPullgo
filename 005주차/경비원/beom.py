import sys
input = sys.stdin.readline

def go_store(direction, store):
    # 북쪽
    if direction == 1:
        return store
    
    # 남쪽
    elif direction == 2:
        return 2*r + c - store

    # 서쪽
    elif direction == 3:
        return 2*(r+c) - store
    
    # 동쪽
    else:
        return r + store 

    

r, c = map(int, input().split())
N = int(input())

go_d = []
for i in range(N+1):
    direction, store = map(int, input().split())
    go_d.append(go_store(direction, store))

result = 0
for i in range(N):
    m = abs(go_d[i] - go_d[-1])
    result += min(m, (2 * (r+c)-m))

print(result)