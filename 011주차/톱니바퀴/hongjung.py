import sys

# 12 1 3 5 6 7 9 11, 3시와 9시가 포인트
wheels = [[]] + [[i for i in sys.stdin.readline().rstrip()] for _ in range(4)]
N = int(sys.stdin.readline())
methods = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for num, dir in methods:
    check = [0, 0, 0, 0, 0]
    check[num] = dir
    if num == 1:
        if wheels[1][2] != wheels[2][6]:
            check[2] = 0 - check[1]
            if wheels[2][2] != wheels[3][6]:
                check[3] = 0 - check[2]
                if wheels[3][2] != wheels[4][6]:
                    check[4] = 0 - check[3]
    elif num == 2:
        if wheels[1][2] != wheels[2][6]:
            check[1] = 0 - check[2]
        if wheels[2][2] != wheels[3][6]:
            check[3] = 0 - check[2]
            if wheels[3][2] != wheels[4][6]:
                check[4] = 0 - check[3]
    elif num == 3:
        if wheels[3][2] != wheels[4][6]:
            check[4] = 0 - check[3]
        if wheels[2][2] != wheels[3][6]:
            check[2] = 0 - check[3]
            if wheels[2][6] != wheels[1][2]:
                check[1] = 0 - check[2]
    elif num == 4:
        if wheels[4][6] != wheels[3][2]:
            check[3] = 0 - check[4]
            if wheels[3][6] != wheels[2][2]:
                check[2] = 0 - check[3]
                if wheels[2][6] != wheels[1][2]:
                    check[1] = 0 - check[2]
    
    for i in range(1, 5):
        if check[i] == -1:
            wheels[i].append(wheels[i].pop(0))
        elif check[i] == 1:
            wheels[i].insert(0, wheels[i].pop())

score = 0
for i in range(1, 5):
    if wheels[i][0] == '1':
        score += 2 ** (i - 1)

print(score)