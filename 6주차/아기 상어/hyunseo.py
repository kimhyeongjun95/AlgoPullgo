# 백준 16263 아기 상어
from collections import deque

def find_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                # 상어의 위치도 다시 지나갈 수 있도록 0으로 바꿔주기
                arr[i][j] = 0
                return i, j


def eat_fish(x, y):
    global eat, time
    
    visited = [[0]*N for _ in range(N)]

    queue = deque()
    queue.append((x, y))
    
    # 거리가 같으면, 위/왼쪽이 우선 : 위/왼쪽/오른쪽/아래
    dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    fish = []
    while queue:
        curr_x, curr_y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = curr_x+dx, curr_y+dy

            if nx in range(N) and ny in range(N):
                # 방문하지 않았고, 상어 크기보다 같거나 작은 숫자라면 이동 가능
                if visited[nx][ny] == 0 and arr[nx][ny] <= size:
                    visited[nx][ny] = visited[curr_x][curr_y] + 1
                    queue.append((nx, ny))

                    # 0이 아니고, 상어 크기보다 작다면 잡아먹을 수 있음
                    if arr[nx][ny] and arr[nx][ny] < size:
                        fish.append((nx, ny, visited[nx][ny]))
            
    if fish:
        fish.sort(key=lambda x: (x[2], x[0], x[1]))
        fish_x, fish_y, distance = fish[0]

        arr[fish_x][fish_y] = 0       # 잡아먹었으니까 물고기가 없는 것! 0으로 바꾸기
        eat += 1                      # 잡아먹은 물고기 수 체크
        time += distance              # 지금까지 움직인 거리(=시간) 더해주기
        return fish_x, fish_y
    
    return 99, 99


N = int(input())
arr = [[i for i in map(int, input().split())] for _ in range(N)]

x, y = find_shark()
size = 2
eat = 0
time = 0

while x < 99 and y < 99:
    x, y = eat_fish(x, y)

    if eat == size:
        size += 1
        eat = 0

print(time)