import sys

def move(a1_i, a1_j, a2_i, a2_j):
    temp = [[0] * C for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    temp[a1_i][a1_j] = -1
    temp[a2_i][a2_j] = -1
    i1 = a1_i
    j1 = a1_j + 1
    i2 = a2_i
    j2 = a2_j + 1
    visited[i1][j1] = 1
    visited[i2][j2] = 1
    visited[a1_i][a1_j] = 1
    visited[a2_i][a2_j] = 1
    flag1 = False
    change1 = False
    flag2 = False
    change2 = False
    while True:
        if flag1 == False:
            if change1 == False:
                for d in range(4):
                    ni = i1 + di[d]
                    nj = j1 + dj[d]
                    if 0 <= ni < R and 0 <= nj < C:
                        if visited[ni][nj] == 0:
                            temp[ni][nj] = house[i1][j1]
                            visited[ni][nj] = 1
                            if ni == 0 and nj == 0:
                                change1 = True
                            i1 = ni
                            j1 = nj
                            break
            else:
                ni = i1 + 1
                if temp[ni][j1] == -1:
                    flag1 = True
                if flag1 == False:
                    temp[ni][j1] = house[i1][j1]
                    visited[ni][j1] = 1
                    i1 += 1

        if flag2 == False:
            if change2 == False:
                for d in range(4):
                    ni = i2 + ri[d]
                    nj = j2 + dj[d]
                    if 0 <= ni < R and 0 <= nj < C:
                        if visited[ni][nj] == 0:
                            temp[ni][nj] = house[i2][j2]
                            visited[ni][nj] = 1
                            if ni == R - 1 and nj == 0:
                                change2 = True
                            i2 = ni
                            j2 = nj
                            break
            else:
                ni = i2 - 1
                if temp[ni][j2] == -1:
                    flag2 = True
                if flag2 == False:
                    temp[ni][j2] = house[i2][j2]
                    visited[ni][j2] = 1
                    i2 -= 1

        if flag1 and flag2:
            break

    for i in range(R):
        for j in range(C):
            if visited[i][j] == 0:
                temp[i][j] = house[i][j]

    return temp


def extension():
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if house[i][j] >= 0:
                cnt = 0
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < R and 0 <= nj < C:
                        if house[ni][nj] != -1:
                            temp[ni][nj] += house[i][j] // 5
                            cnt += 1
                temp[i][j] += house[i][j] - (house[i][j] // 5) * cnt
    return temp


R, C, T = map(int, sys.stdin.readline().split())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

air_cleaner = []
for i in range(R):
    for j in range(C):
        if house[i][j] == -1:
            air_cleaner.append([i, j])

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
ri = [0, 1, 0, -1]
for _ in range(T):
    house = extension()
    house = move(air_cleaner[0][0], air_cleaner[0][1], air_cleaner[1][0], air_cleaner[1][1])

result = 2
for i in range(R):
    for j in range(C):
        result += house[i][j]

print(result)