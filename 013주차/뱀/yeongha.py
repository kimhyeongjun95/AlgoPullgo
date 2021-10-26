from collections import deque

N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
directions = deque([input().split() for _ in range(L)])

i = 0
dx, dy = 0, 1
t, c = directions.popleft()
t = int(t)
snakes = deque([(1,1)])  # 뱀의 몸이 위치한 좌표가 들어갈 deque
while True:
    i += 1
    nx, ny = snakes[0][0] + dx, snakes[0][1] + dy

    if nx < 1 or nx >= N+1 or ny < 1 or ny >= N+1 or (nx, ny) in snakes:  # 벽처리
        break
    else:
        snakes.appendleft((nx, ny))

    if (nx, ny) in apples:  # 그 자리에 사과가 있다면 사과 삭제
        apples.remove((nx, ny))
    else:
       snakes.pop()  # 없다면 꼬리 있던 좌표 삭제

    if i == t:  # 방향을 바꿀 시간이 됬다면
        if c == 'L':
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
        if directions:  # 방향을 바꿀게 아직 남아있다면 t, c 변경
            t, c = directions.popleft()
            t = int(t)
print(i)



    
