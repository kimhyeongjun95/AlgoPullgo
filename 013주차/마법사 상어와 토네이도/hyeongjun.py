# 백준 20057 마법사 상어와 토네이도

# A[r][c] : 모래의 양
# 가운데 칸부터 토네이도의 이동 시작

# 토네이도의 양은 1,1까지 이동한 뒤 소멸
# 소멸 뒤, 격자의 밖으로 나간 모래의 양은?

import sys
input = sys.stdin.readline

    #좌, 하, 우, 상 -> 좌회전
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


left = [
    (0, -2, 0.05),# 왼쪽왼쪽
    (1, -1, 0.1), # 아래왼쪽
    (-1, -1, 0.1),# 위왼쪽
    (1, 0, 0.07), # 위
    (-1, 0, 0.07),# 아래
    (-2, 0, 0.02),# 위위
    (2, 0, 0.02), # 아래아래
    (1, 1, 0.01), # 위오른쪽
    (-1, 1, 0.01),# 아래오른쪽
    (0, -1, 1)    # 나머지
]
down = [[-y, x, per] for x, y, per in left]
right = [[x, -y, per] for x, y, per in left]
up = [[y, x, per] for x, y, per in left]

def shark_tornado():
    global answer
    direction = 0
    tx = n//2
    ty = n//2 # 시작점
    visited[tx][ty] = 1                            
    while tx != 0 or ty != 0:

        nx = tx + dx[direction] 
        ny = ty + dy[direction]
        if not visited[nx][ny]:
            tx, ty = nx, ny # 나중에 갈 수 있는 방향인지 확인해야하기 때문이다
            visited[nx][ny] = 1
            count = 0
            # 좌
            if direction == 0:
                for x, y, per in left:
                    if per == 1:
                        rest = arr[nx][ny] - count
                    else:
                        rest = int(arr[nx][ny] * per)
                        count += rest
                    # 만약 범위안이라면
                    if -1 < nx+x < n and -1 < ny+y < n:
                        arr[nx+x][ny+y] += rest
                    # 범위 밖이라면
                    else:
                        answer += rest

            # 하
            elif direction == 1:
                for x, y, per in down:
                    if per == 1:
                        rest = arr[nx][ny] - count
                    else:
                        rest = int(arr[nx][ny] * per)
                        count += rest
                    # 만약 범위안이라면
                    if -1 < nx+x < n and -1 < ny+y < n:
                        arr[nx+x][ny+y] += rest
                    # 범위 밖이라면
                    else:
                        answer += rest

            # 우
            elif direction == 2:
                for x, y, per in right:
                    if per == 1:
                        rest = arr[nx][ny] - count
                    else:
                        rest = int(arr[nx][ny] * per)
                        count += rest
                    # 만약 범위안이라면
                    if -1 < nx+x < n and -1 < ny+y < n:
                        arr[nx+x][ny+y] += rest
                    # 범위 밖이라면
                    else:
                        answer += rest
            
            # 상
            elif direction == 3:
                for x, y, per in up:
                    if per == 1:
                        rest = arr[nx][ny] - count
                    else:
                        rest = int(arr[nx][ny] * per)
                        count += rest
                    # 만약 범위안이라면
                    if -1 < nx+x < n and -1 < ny+y < n:
                        arr[nx+x][ny+y] += rest
                    # 범위 밖이라면
                    else:
                        answer += rest
            arr[nx][ny] = 0
        ###############################
            direction += 1 # 방향전환
            if direction == 4:
                direction = 0
        else: # 방문했다면 -> 즉, 자기쪽으로 돌려고 하기 때문에 직진을 해야한다
            direction -= 1
            if direction < 0:
                direction = 3

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
answer = 0
shark_tornado()
print(answer)