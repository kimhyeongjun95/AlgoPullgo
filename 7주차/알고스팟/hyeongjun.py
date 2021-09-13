# 1261 알고스팟

# 미로 : N * M
# 미로는 1. 빈방
#        2. 벽 -> 부수지 않으면 이동할 수 없음.
# 으로 이루어져 있다.

# (1, 1) -> (N, M)으로 이동할 시에 벽을 최소 몇개 부수어야 하는지?
# 0은 빈 방
# 1은 벽
# 상하좌우로만 이동가능

# 011
# 111
# 110
# -> 3개

# 0001
# 1000
# -> 0개

# 1. 0으로 이동한다.
    # 1-1. 제일 처음 시작 위치를 10으로 시작, 다른 숫자들과 겹치지 않기 위해
    # 1-2. 최단경로를 찾아야 하기 때문에 현재 지나온 길을 += 1로 바꿈.
# 2. 문제점 : 벽을 뚫고 지나가지 않아도 될 곳을 뚫고 지나간걸로 표시됨.
#    해결방법 : BFS 말고 DFS로 해볼까?

dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# def path_finder(maze): # BFS
#     visited = [[0] * M for _ in range(N)]
#     stack = [(0, 0)]
#     while stack:
#         x, y = stack.pop()

#         for dx, dy in dxy:
#             nx = x + dx
#             ny = y + dy

#             if -1 < nx < N and -1 < ny < M: # 범위를 벗어나지 않고

#                 if maze[nx][ny] == 0 and visited[nx][ny] == 0: # 방문하지 않았고 통로일 경우 
#                     maze[nx][ny] = maze[x][y]
#                     stack.append((nx, ny))
#                     visited[nx][ny] = 1

#                 elif maze[nx][ny] == 1 and visited[nx][ny] == 0: # 방문하지 않았고 벽일 경우
#                     maze[nx][ny] = maze[x][y] + 1
#                     stack.append((nx, ny))
#                     visited[nx][ny] = 1
#         for i in visited:
#             print(i, 'def-visited')
#         for i in maze:
#             print(i, 'def-maze')
#     return visited

from collections import deque

def path_finder(maze):
    visited = [[0] * M for _ in range(N)]
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if -1 < nx < N and -1 < ny < M: # 범위를 벗어나지 않고

                if maze[nx][ny] == 0 and visited[nx][ny] == 0: # 방문하지 않았고 통로일 경우 
                    maze[nx][ny] = maze[x][y]
                    queue.appendleft((nx, ny)) # appendleft를 해주고
                    visited[nx][ny] = 1

                if maze[nx][ny] == 1 and visited[nx][ny] == 0: # 방문하지 않았고 벽일 경우
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny)) # append를 해주는 것이 핵심!
                    visited[nx][ny] = 1
    #     for i in visited:
    #         print(i, 'def-visited')
    #     for i in maze:
    #         print(i, 'def-maze')
    return maze[N-1][M-1] - 10

M, N = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
maze[0][0] = 10 # 출발 위치 10으로 시작
answer = path_finder(maze)
# for i in maze:
#     print(i, 'maze')
# for i in visited:
#     print(i, 'visited')
print(answer)