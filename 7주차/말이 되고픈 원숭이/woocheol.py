from collections import deque
k = int(input())

w, h = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0 for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
queue = deque()
horse_dir_x = [-2, -2, -1, 1, 2, 2, 1, -1]
horse_dir_y = [-1, 1, 2, 2, 1, -1, -2, -2]
dir_x = [0, 0, 1, -1]
dir_y = [1, -1, 0, 0]

queue.append([0, 0, k])
visited[0][0][k] = 1
ans = -1

while queue:
    curr_x, curr_y, cnt = queue.popleft()

    if curr_x == h-1 and curr_y == w-1:
        ans = visited[curr_x][curr_y][cnt] - 1
        break

    if cnt:
        for i in range(8):
            next_x, next_y = curr_x + horse_dir_x[i], curr_y + horse_dir_y[i]
            if 0 <= next_x < h and 0 <= next_y < w and not maze[next_x][next_y] and not visited[next_x][next_y][cnt-1]:
                visited[next_x][next_y][cnt -
                                        1] = visited[curr_x][curr_y][cnt] + 1
                queue.append([next_x, next_y, cnt - 1])
    for i in range(4):
        next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
        if 0 <= next_x < h and 0 <= next_y < w and not visited[next_x][next_y][cnt] and not maze[next_x][next_y]:
            visited[next_x][next_y][cnt] = visited[curr_x][curr_y][cnt] + 1
            queue.append([next_x, next_y, cnt])


print(ans)
