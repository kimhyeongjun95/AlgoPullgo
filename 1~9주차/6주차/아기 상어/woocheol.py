# 13236번 아기상어
from collections import deque
import pprint

n = int(input())
place = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dir_x = [-1, 0, 1, 0]
dir_y = [0, -1, 0, 1]

x, y = 0, 0
for i in range(n):
    for j in range(n):
        if place[i][j] == 9:
            x, y = i, j

curr_size = 2
eat = 0
ans = 0
queue = deque()
queue.append([x, y])
visited[x][y] = 1
place[x][y] = 0
temp = []

while True:
    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y] and place[next_x][next_y] <= curr_size:
                visited[next_x][next_y] = visited[curr_x][curr_y] + 1
                queue.append([next_x, next_y])
                if 0 < place[next_x][next_y] < curr_size:
                    temp.append([visited[curr_x][curr_y], next_x, next_y])

    if temp:
        temp.sort()
        ans += temp[0][0]
        eat += 1
        if eat == curr_size:
            curr_size += 1
            eat = 0
        place[temp[0][1]][temp[0][2]] = 0
        queue.append([temp[0][1], temp[0][2]])
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[temp[0][1]][temp[0][2]] = 1
        temp = []
    else:
        break

print(ans)


# while queue:
#     curr_x, curr_y = queue.popleft()
#     for i in range(4):
#         next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
#         if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y] and place[next_x][next_y] <= curr_size:

#             if 0 < place[next_x][next_y] < curr_size:
#                 pprint.pprint(visited)
#                 print(next_x, next_y, curr_size)
#                 eat += 1
#                 ans += visited[curr_x][curr_y]
#                 if eat == curr_size:
#                     curr_size += 1
#                     eat = 0
#                 visited = [[0 for _ in range(n)] for _ in range(n)]
#                 place[next_x][next_y] = 0
#                 queue = deque()
#                 queue.append([next_x, next_y])
#                 visited[next_x][next_y] = 1
#                 break

#             else:
#                 visited[next_x][next_y] = visited[curr_x][curr_y] + 1
#                 queue.append([next_x, next_y])

# print(ans)
