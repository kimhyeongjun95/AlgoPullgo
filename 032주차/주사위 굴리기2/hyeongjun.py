# 백준 23288 주사위 굴리기 2

# 크기 N x M
#  2   0
# 413 415
#  5   2
#  6   3

# 4 5 1
# 4 1 2 3 3
# 6 1 1 3 3
# 5 6 1 3 2
# 5 5 6 5 5

# 주사위 지도 윗면 1 동쪽 3
# 처음 이동방향 동쪽

# 1. 주사위가 이동 방향으로 한 칸
#    if 방향에 칸 x, 반대로 한 칸

# 2. 도착한 칸에 대한 점수 획득
    # (x, y)있는 정수 B
    # 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C 모두 구한다.
    # 이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다.
    # 여기서 점수는 B와 C를 곱한다.

# 3. 아랫면에 있는 정수 A, 주사위가 있는 칸 B 비교해 이동 방향 결정
#    A > B : 90도 시계 방향
#    A < B : 90도 반시계 방향
#    A = B인 경우 이동 방향에 변화는 없다.


# 이동 횟수 K, 이동에서 획득하는 점수의 합 구하기

# 동남서북
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def rotate(dice, dir):
    ndice = [0] * 6
    
    # 동
    if dir == 0:
        ndice[0] = dice[0]
        ndice[5] = dice[1]
        ndice[2] = dice[2]
        ndice[4] = dice[3]
        ndice[1] = dice[4]
        ndice[3] = dice[5]
    # 남
    elif dir == 1:
        ndice[1] = dice[0]
        ndice[2] = dice[1]
        ndice[3] = dice[2]
        ndice[0] = dice[3]
        ndice[4] = dice[4]
        ndice[5] = dice[5]
    # 서
    elif dir == 2:
        ndice[0] = dice[0]
        ndice[4] = dice[1]
        ndice[2] = dice[2]
        ndice[5] = dice[3]
        ndice[3] = dice[4]
        ndice[1] = dice[5]
    # 북
    elif dir == 3:
        ndice[3] = dice[0]
        ndice[0] = dice[1]
        ndice[1] = dice[2]
        ndice[2] = dice[3]
        ndice[4] = dice[4]
        ndice[5] = dice[5]

    for i in range(6):
        dice[i] = ndice[i]
    return dice

def dfs(x, y):
    stack = [(x, y)]
    count = 1
    visited = [[0] * m for _ in range(n)]
    visited[x][y] =1

    while stack:
        x, y = stack.pop()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if -1 < nx < n and -1 < ny < m:
                if arr[x][y] == arr[nx][ny]:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        stack.append((nx, ny))
                        count += 1
    return count

def toMove(i, j):
    answer = 0
    dir = 0
    dice = [2, 1, 5, 6, 4, 3]
    x, y = i, j
    for _ in range(k):
        nx = x + dxy[dir][0]
        ny = y + dxy[dir][1]
        # 1. 칸이 없으면 반대로
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            dir = (dir + 2) % 4
            # print('방향전환-------------', nx, ny, dir)
            nx = x + dxy[dir][0]
            ny = y + dxy[dir][1]
        # print(nx, ny, dir)
        dice = rotate(dice, dir)
        # 2.
        count = dfs(nx, ny)
        answer += arr[nx][ny] * count
        # 3.
        A = dice[3]
        B = arr[nx][ny]
        # print(A, B, "AB", dir)
        # 시계방향
        if A > B:
            dir = (dir + 1) % 4
        # 반시계방향
        elif A < B:
            dir = (dir - 1) % 4

        x, y = nx, ny

    return answer

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = toMove(0, 0)
print(answer)