from collections import deque

def move(n, d):
    if d == -1:
        temp = gear[n].popleft()
        gear[n].append(temp)
    else:
        temp = gear[n].pop()
        gear[n].appendleft(temp)

gear = [0] + [deque(list(input())) for _ in range(4)]
N = int(input())
for _ in range(N):
    must_move = [[0, 1] for _ in range(5)]

    n, d = map(int, input().split())
    must_move[n][0], must_move[n][1] = 1, d

    for i in range(n, 1, -1):
        if gear[i][6] != gear[i-1][2]:
            if must_move[i][1] == 1:
                must_move[i-1][0], must_move[i-1][1]= 1, -1
            else:
                must_move[i-1][0], must_move[i-1][1]= 1, 1
        else:
            break
    
    for i in range(n, 4):
        if gear[i][2] != gear[i+1][6]:
            if must_move[i][1] == 1:
                must_move[i+1][0], must_move[i+1][1] = 1, -1
            else:
                must_move[i+1][0], must_move[i+1][1] = 1, 1
        else:
            break

    for i in range(1, 5):
        if must_move[i][0] == 1:
            move(i, must_move[i][1])
    
ans = 0
for i in range(1, 5):
    if gear[i][0] == '1':
        ans += 2**(i-1)
print(ans)


