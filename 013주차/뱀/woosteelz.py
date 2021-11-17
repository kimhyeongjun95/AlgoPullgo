from collections import deque


def go_left(curr, x, y):
    if curr == 'right':
        return 'top', x-1, y
    if curr == 'left':
        return 'down', x+1, y
    if curr == 'top':
        return 'left', x, y-1
    if curr == 'down':
        return 'right', x, y+1


def go_right(curr, x, y):
    if curr == 'right':
        return 'down', x+1, y
    if curr == 'left':
        return 'top', x-1, y
    if curr == 'top':
        return 'right', x, y+1
    if curr == 'down':
        return 'left', x, y-1


def go(curr, x, y):
    if curr == 'right':
        return 'right', x, y+1
    if curr == 'left':
        return 'left', x, y-1
    if curr == 'top':
        return 'top', x-1, y
    if curr == 'down':
        return 'down', x+1, y


N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

commands = deque()
for _ in range(int(input())):
    sec, cmd = list(map(str, input().split()))
    commands.append([int(sec), cmd])

dir = 'right'
snake = deque()
snake.append([0, 0])

ans = 0
while True:
    if commands and ans == commands[0][0]:
        _, cmd = commands.popleft()
        if cmd == 'L':
            dir, x, y = go_left(dir, snake[-1][0], snake[-1][1])
        else:
            dir, x, y = go_right(dir, snake[-1][0], snake[-1][1])
    else:
        dir, x, y = go(dir, snake[-1][0], snake[-1][1])
    if 0 <= x < N and 0 <= y < N and not [x, y] in snake:
        if graph[x][y]:
            graph[x][y] = 0
            snake.append([x, y])
        else:
            snake.append([x, y])
            snake.popleft()
    else:
        ans += 1
        break
    ans += 1

print(ans)
