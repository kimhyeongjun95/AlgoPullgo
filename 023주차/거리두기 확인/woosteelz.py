from collections import deque


def check_distance(place, x, y):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    dir_x = [0, 1, -1, 0]
    dir_y = [1, 0, 0, -1]

    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < 5 and 0 <= next_y < 5 and not visited[next_x][next_y] and (place[next_x][next_y] == "O" or place[next_x][next_y] == "P"):
                queue.append([next_x, next_y])
                visited[next_x][next_y] = visited[curr_x][curr_y] + 1
                if place[next_x][next_y] == "P" and visited[next_x][next_y] <= 3:
                    return False

    return True


def solution(places):
    answer = []

    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    flag = check_distance(place, i, j)
                if not flag:
                    break
            if not flag:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer
