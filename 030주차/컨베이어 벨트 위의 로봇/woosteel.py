from collections import deque

ans = 1
n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque(0 for _ in range(2 * n))

while True:
    # 1. 한 칸 회전
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    robot[n-1] = 0

    # 2.
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            belt[i+1] -= 1
            if not belt[i+1]:
                k -= 1
            robot[i+1] = robot[i]
            robot[i] = 0
    robot[n-1] = 0

    if belt[0] and not robot[0]:
        belt[0] -= 1
        if not belt[0]:
            k -= 1
        robot[0] = 1

    if k <= 0:
        print(ans)
        break
    ans += 1
