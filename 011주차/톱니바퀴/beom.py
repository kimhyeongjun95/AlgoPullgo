import math


def clock(arr):
    x = arr[:7]
    x.insert(0, arr[-1])
    return x


def opp_clock(arr):
    x = arr[1:]
    x.append(arr[0])
    return x


wheel = [list(map(int, input())) for _ in range(4)]
K = int(input())
rotate = [list(map(int, input().split())) for _ in range(K)]

# 회전확인용
turn = [False] * 4

for i in rotate:
    curr = i[0]-1
    turn[curr] = True
    
    # 오른쪽 확인
    for j in range(curr, 4):
        if j < 3 and wheel[j][2] == wheel[j+1][6]:
            turn[j+1] = False
            break
        elif j < 3:
            turn[j+1] = True
    
    # 왼쪽 확인
    for u in range(curr, -1, -1): 
        if u > 0 and wheel[u][6] == wheel[u-1][2]:
            turn[u-1] = False
            break
        elif u > 0:
            turn[u-1] = True
            
	# 홀수 - 반시계방향, 짝수 - 시계방향
    if (curr % 2 == 0 and i[1] == 1) or (curr % 2 != 0 and i[1] == -1): 
        for check in range(4):
            if turn[check] == False:
                continue
            elif check % 2 == 0:
                wheel[check] = clock(wheel[check])
            else:
                wheel[check] = opp_clock(wheel[check])
    # 홀수 - 시계방향, 짝수 - 반시계방향
    else: 
        for check in range(4):
            if turn[check] == False:
                continue
            elif check % 2 == 0:
                wheel[check] = opp_clock(wheel[check])
            else:
                wheel[check] = clock(wheel[check])

    turn = [False] * 4

# 결과 출력
total = 0
for i in range(4):
    if wheel[i][0] == 1: 
        total += int(math.pow(2,i))

print(total)