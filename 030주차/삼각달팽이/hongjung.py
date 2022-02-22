def solution(n):
    answer = []
    pyramid = [[0] * n for _ in range(n)]
    di = [1, 0, -1]
    dj = [0, 1, -1]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    pyramid[0][0] = 1
    i = j = 0
    idx = 0
    cnt = 0
    while cnt < 2:
        if idx == 0:
            if 0 <= i + di[0] < n and 0 <= j + dj[0] < n and pyramid[i+di[0]][j+dj[0]] == 0:
                pyramid[i+di[0]][j+dj[0]] = pyramid[i][j] + 1
                i = i + di[0]
                j = j + dj[0]
                cnt = 0
            else:
                idx = 1
                cnt += 1
        elif idx == 1:
            if 0 <= i + di[1] < n and 0 <= j + dj[1] < n and pyramid[i+di[1]][j+dj[1]] == 0:
                pyramid[i+di[1]][j+dj[1]] = pyramid[i][j] + 1
                i = i + di[1]
                j = j + dj[1]
                cnt = 0
            else:
                idx = 2
                cnt += 1
        elif idx == 2:
            if 0 <= i + di[2] < n and 0 <= j + dj[2] < n and pyramid[i+di[2]][j+dj[2]] == 0:
                pyramid[i+di[2]][j+dj[2]] = pyramid[i][j] + 1
                i = i + di[2]
                j = j + dj[2]
                cnt = 0
            else:
                idx = 0
                cnt += 1

    for i in range(n):
        for j in range(n):
            if pyramid[i][j] != 0:
                answer.append(pyramid[i][j])
            else:
                break
    return answer

print(solution(4))
print(solution(5))
print(solution(6))