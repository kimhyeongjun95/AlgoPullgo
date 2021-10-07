# 2468번 안전 영역
from collections import deque

N = int(input())
safe_zone = [list(map(int, input().split())) for _ in range(N)]
dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]
ans = float('-inf')
min_hei = min(map(min, safe_zone))
max_hei = max(map(max, safe_zone))

for rain_hei in range(min_hei-1, max_hei):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and safe_zone[i][j] > rain_hei:
                queue.append([i, j])
                visited[i][j] = True
                while queue:
                    curr_x, curr_y = queue.popleft()
                    for k in range(4):
                        next_x, next_y = curr_x + dir_x[k], curr_y + dir_y[k]
                        if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and safe_zone[next_x][next_y] > rain_hei:
                            # queue에 집어넣기 전에 방문처리 해주어야 메모리 사용량을 줄일 수 있음
                            # queue에 중복된 좌표가 들어갈 수 있기 때문
                            visited[next_x][next_y] = True
                            queue.append([next_x, next_y])
                cnt += 1
            ans = max(cnt, ans)

print(ans)
