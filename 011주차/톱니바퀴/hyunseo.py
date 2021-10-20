# 백준 14891 톱니바퀴
from collections import deque

def turn_left(wheel_num):
    global wheels

    check[wheel_num] = True

    if wheel_num - 1 >= 1 and not check[wheel_num-1]:
        if wheels[wheel_num-1][2] != wheels[wheel_num][6]:
            turn_right(wheel_num-1)
    
    if wheel_num + 1 <= 4 and not check[wheel_num+1]:
        if wheels[wheel_num][2] != wheels[wheel_num+1][6]:
            turn_right(wheel_num+1)
    
    wheel = wheels[wheel_num]
    wheel.append(wheel.popleft())
    wheels[wheel_num] = wheel


def turn_right(wheel_num):
    global wheels

    check[wheel_num] = True

    if wheel_num - 1 >= 1 and not check[wheel_num-1]:
        if wheels[wheel_num-1][2] != wheels[wheel_num][6]:
            turn_left(wheel_num-1)
    
    if wheel_num + 1 <= 4 and not check[wheel_num+1]:
        if wheels[wheel_num][2] != wheels[wheel_num+1][6]:
            turn_left(wheel_num+1)

    wheel = wheels[wheel_num]
    wheel.appendleft(wheel.pop())
    wheels[wheel_num] = wheel


wheels = {}
for i in range(1, 5):
    wheels[i] = deque(list(input()))

K = int(input())
for _ in range(K):
    # command : 1(시계방향, 오른쪽), -1(반시계방향, 왼쪽)
    wheel_num, command = map(int, input().split())
    check = [False for _ in range(5)]

    if command == 1:
        turn_right(wheel_num)
    elif command == -1:
        turn_left(wheel_num)

score = 0
for key, value in wheels.items():
    if value[0] == '1':
        score += 2**(key-1)

print(score)