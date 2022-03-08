import sys

def move(i, j, direction, cnt):
    global N, di, dj

    # while cnt:
    #     cnt -= 1
    #     ni = i + di[direction-1]
    #     nj = j + dj[direction-1]
    #     if ni == -1:
    #         ni = N - 1
    #     if ni == N:
    #         ni = 0
    #     if nj == -1:
    #         nj = N - 1
    #     if nj == N:
    #         nj = 0
    #     i = ni
    #     j = nj

    ni = (N + i + (di[direction-1] * cnt)) % N
    nj = (N + j + (dj[direction-1] * cnt)) % N
    
    result = [ni, nj]
    return result


N, M = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]
point = [N-1, 0]

cloud = []
for m in range(M):
    if m == 0:
        visited = [[False] * N for _ in range(N)]
        direction, cnt = commands[0]
        point = move(point[0], point[1], direction, cnt)
        tmp = [point]
        up_x = 0
        right_y = 0
        if point[0] - 1 == -1:
            up_x = N - 1
        else:
            up_x = point[0] - 1
        if point[1] + 1 == N:
            right_y = 0
        else:
            right_y = point[1] + 1
        tmp.append([point[0], right_y])
        tmp.append([up_x, point[1]])
        tmp.append([up_x, right_y])
        for i, j in tmp:
            visited[i][j] = True
            area[i][j] += 1
        for i, j in tmp:
            plus = 0
            if 0 <= i - 1 < N and 0 <= j - 1 < N and area[i-1][j-1]:
                plus += 1
            if 0 <= i + 1 < N and 0 <= j + 1 < N and area[i+1][j+1]:
                plus += 1
            if 0 <= i - 1 < N and 0 <= j + 1 < N and area[i-1][j+1]:
                plus += 1
            if 0 <= i + 1 < N and 0 <= j - 1 < N and area[i+1][j-1]:
                plus += 1
            area[i][j] += plus

        for i in range(N):
            for j in range(N):
                if visited[i][j] == False and area[i][j] >= 2:
                    area[i][j] -= 2
                    cloud.append([i, j])
    else:
        visited = [[False] * N for _ in range(N)]
        direction, cnt = commands[m]
        for i in range(len(cloud)):
            location = move(cloud[i][0], cloud[i][1], direction, cnt)
            cloud[i] = location
            area[cloud[i][0]][cloud[i][1]] += 1
        for i, j in cloud:
            visited[i][j] = True
            plus = 0
            if 0 <= i - 1 < N and 0 <= j - 1 < N and area[i-1][j-1]:
                plus += 1
            if 0 <= i + 1 < N and 0 <= j + 1 < N and area[i+1][j+1]:
                plus += 1
            if 0 <= i - 1 < N and 0 <= j + 1 < N and area[i-1][j+1]:
                plus += 1
            if 0 <= i + 1 < N and 0 <= j - 1 < N and area[i+1][j-1]:
                plus += 1
            area[i][j] += plus

        tmp = []
        for i in range(N):
            for j in range(N):
                if visited[i][j] == False and area[i][j] >= 2:
                    area[i][j] -= 2
                    tmp.append([i, j])
        cloud = tmp

water = 0
for i in range(N):
    for j in range(N):
        water += area[i][j]

print(water)