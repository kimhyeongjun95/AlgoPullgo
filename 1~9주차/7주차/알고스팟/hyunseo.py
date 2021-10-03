# 백준 1261 알고스팟

from collections import deque

def bfs(x, y):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[x][y] = 1
    
    queue = deque()
    queue.append((arr[x][y], x, y))
    
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        # 우선 순위 고려해주기
        for i in range(len(queue)):
            if queue[i][0]:
                _, curr_x, curr_y = queue[i]
                queue.remove(queue[i])
                break
        else:
            _, curr_x, curr_y = queue.popleft()

        # 도착점에 오면 반복문 끝!
        if curr_x == N-1 and curr_y == M-1:
            break
            
        for dx, dy in dxy:
            nx, ny = curr_x+dx, curr_y+dy

            if nx in range(N) and ny in range(M) and not visited[nx][ny]:
                queue.append((1-arr[nx][ny], nx, ny))

                if arr[nx][ny] == 0:
                    visited[nx][ny] = visited[curr_x][curr_y]
                # 1일 경우 벽을 부수는 개수 카운팅
                else:
                    visited[nx][ny] = visited[curr_x][curr_y] + 1
    
    # 시작점에서 벽을 안 부쉈는데 방문체크 +1 을 해줬으므로 -1
    return visited[curr_x][curr_y] - 1


M, N = map(int, input().split())
arr = []

for _ in range(N):
    temp = []
    for num in input():
        temp.append(int(num))
    arr.append(temp)

print(bfs(0, 0))