# 백준 21608 상어 초등학교

# 교실 N x N
# 학생 수 N^2

# 학생의 자리를 정하려고 한다

# 1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸
# 2. 1 만족 다수 -> 인접한 칸 중 비어있는 칸이 가장 많은 칸
# 3. 2 만족 여러 개 -> 3-1. 행의 번호가 가장 작은 칸, 3-2. 여러 개 -> 열의 번호가 가장 작은 칸

# 학생의 만족도 총합 출력

# 3
# 4 2 5 1 7 // 2
# 3 1 9 4 5 // 3
# 9 8 1 2 3
# 8 1 9 3 4
# 7 2 3 4 8
# 1 9 2 5 7
# 6 5 2 3 4
# 5 1 9 2 8
# 2 9 3 1 4

def contentCheck(room):
    answer = 0
    for i in range(n):
        for j in range(n):
            count = 0

            for dx, dy in dxy:
                nx = dx + i
                ny = dy + j

                if -1 < nx < n and -1 < ny < n:
                    if room[nx][ny][0] in room[i][j][1:]:
                        count += 1
            if count == 1:
                answer += 1
            elif count == 2:
                answer += 10
            elif count == 3:
                answer += 100
            elif count == 4:
                answer += 1000
    return answer

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n = int(input())

room = [[[0] * 5 for _ in range(n)] for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

for student in students:
    val = student[1:]
    # [0]좋아하는 학생 수의 합 [1]빈칸의 합
    seats = [[[0] * 2 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if room[i][j][0] == 0:
                for dx, dy in dxy:
                    nx = i + dx
                    ny = j + dy

                    if -1 < nx < n and -1 < ny < n: 
                        if room[nx][ny][0] == 0:
                            seats[i][j][1] += 1
                        elif room[nx][ny][0] in val:
                            seats[i][j][0] += 1
    temp = []
    for i in range(n):
        for j in range(n):
            if room[i][j][0] == 0:
                # 좋아하는 학생수, 빈칸의 합, 좌표
                temp.append((seats[i][j][0], seats[i][j][1], i, j))
    # 좋아하는 학생수가 제일 많고 > 빈칸의 합이 큼 > 행 > 열
    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    room[temp[0][2]][temp[0][3]] = student

answer = contentCheck(room)
print(answer)