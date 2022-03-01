import sys
from collections import defaultdict

N = int(sys.stdin.readline())
student_dict = defaultdict(list)

for _ in range(N ** 2):
    line = list(map(int, sys.stdin.readline().split()))
    for i in range(1, 5):
        student_dict[line[0]].append(line[i])

seats = [[0] * N for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

for student in student_dict.keys():

    like_dict = defaultdict(list)
    for x in range(N):
        for y in range(N):
            if seats[x][y] == 0:
                tmp = 0
                for d in range(4):
                    nx = x + di[d]
                    ny = y + dj[d]
                    if 0 <= nx < N and 0 <= ny < N and seats[nx][ny] in student_dict[student]:
                        tmp += 1
                like_dict[tmp].append([x, y])

    like_list = like_dict[max(list(like_dict.keys()))]
    like_list.sort(key=lambda x: (x[0], x[1]))

    max_blank = -1           
    for x, y in like_list:
        tmp = 0
        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < N and 0 <= ny < N and seats[nx][ny] == 0:
                tmp += 1

        if tmp > max_blank:
            max_blank = tmp
            seat = [x, y]
            
    seats[seat[0]][seat[1]] = student

answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and seats[ni][nj] in student_dict[seats[i][j]]:
                cnt += 1
        if cnt == 0:
            pass
        elif cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        elif cnt == 4:
            answer += 1000

print(answer)