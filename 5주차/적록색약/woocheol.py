# 10026번 적록색약
from collections import deque

n = int(input())
picture_normal = [list(input()) for _ in range(n)]
visited_normal = [[False for _ in range(n)] for _ in range(n)]
picture_dis = [[' ' for _ in range(n)] for _ in range(n)]
visited_dis = [[False for _ in range(n)] for _ in range(n)]

# 적록색약을 위한 새로운 그림 생성
for i in range(n):
    for j in range(n):
        picture_dis[i][j] = picture_normal[i][j] if not picture_normal[i][j] == 'R' else 'G'

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

cnt_normal = 0
cnt_dis = 0

normal_queue = deque()
dis_queue = deque()

for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            cnt_normal += 1
            normal_queue.append([i, j])
            visited_normal[i][j] = True
            while normal_queue:
                curr_x, curr_y = normal_queue.popleft()
                curr_normal = picture_normal[curr_x][curr_y]
                for k in range(4):
                    next_x, next_y = curr_x + dir_x[k], curr_y + dir_y[k]
                    if 0 <= next_x < n and 0 <= next_y < n and not visited_normal[next_x][next_y] and picture_normal[next_x][next_y] == curr_normal:
                        visited_normal[next_x][next_y] = True
                        normal_queue.append([next_x, next_y])

        if not visited_dis[i][j]:
            cnt_dis += 1
            dis_queue.append([i, j])
            visited_dis[i][j] = True
            while dis_queue:
                curr_x, curr_y = dis_queue.popleft()
                curr_dis = picture_dis[curr_x][curr_y]
                for k in range(4):
                    next_x, next_y = curr_x + dir_x[k], curr_y + dir_y[k]
                    if 0 <= next_x < n and 0 <= next_y < n and not visited_dis[next_x][next_y] and picture_dis[next_x][next_y] == curr_dis:
                        visited_dis[next_x][next_y] = True
                        dis_queue.append([next_x, next_y])

print(cnt_normal, cnt_dis)
