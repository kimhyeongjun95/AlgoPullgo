def solution(n):
    answer = []
    map = [[0 for _ in range(n)] for _ in range(n)]

    curr_x = 0
    curr_y = -1

    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                curr_y += 1
            elif i % 3 == 1:
                curr_x += 1
            elif i % 3 == 2:
                curr_x -= 1
                curr_y -= 1
            map[curr_y][curr_x] = num
            num += 1

    for i in range(n):
        for j in range(n):
            if map[i][j] != 0:
                answer.append(map[i][j])

    return answer
