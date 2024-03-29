# 백준 20055 컨베이어 벨트 위의 로봇
from collections import deque

N, K = map(int, input().split())
powers = deque(map(int, input().split()))
robots = []
answer = 0

while powers.count(0) < K:
    answer += 1
    print(answer)
    # 1
    powers.appendleft(powers.pop())
    print('1:', robots)

    if robots:
        temp = []
        for robot in robots:
            if robot != N - 2:
                temp.append(robot + 1)
        robots = temp
    
    print('2:',robots)
    # 2
    if robots:
        temp = []
        for robot in robots:
            if robot+1 not in robots and powers[robot+1] > 0:
                powers[robot+1] -= 1

                if robot != N - 2:
                    temp.append(robot + 1)
        robots = temp
    print('3:',robots)
    # 3
    if powers[0] > 0:
        powers[0] -= 1
        robots.append(0)
print(answer)