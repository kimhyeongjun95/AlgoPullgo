# 프로그래머스 게임 맵 최단거리 (Level 2)
from collections import deque


def solution(maps):
    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]
    N = len(maps)
    M = len(maps[0])
    visited = [[0 for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            temp_x = x + dir_x[i]
            temp_y = y + dir_y[i]
            if 0 <= temp_x < N and 0 <= temp_y < M and not visited[temp_x][temp_y] and maps[temp_x][temp_y] == 1:
                queue.append([temp_x, temp_y])
                visited[temp_x][temp_y] = 1 + visited[x][y]
    if not visited[N-1][M-1]:
        return -1

    return visited[N-1][M-1]


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
        1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))
