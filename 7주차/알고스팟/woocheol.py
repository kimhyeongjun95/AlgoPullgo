# BOJ 1261번 알고스팟
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    temp = []
    k = str(input())
    for i in range(m):
        temp.append(int(k[i]))
    graph.append(temp)

dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

queue = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]
queue.append([0, 0])
visited[0][0] = 1
cnt = 0
while queue:
    curr_x, curr_y = queue.popleft()
    if visited[n-1][m-1]:
        break
    for i in range(4):
        next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
        if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
            # next_x, next_y의 비용이 0라면 먼저 탐색하도록 queue의 맨 앞에 삽입
            if graph[next_x][next_y] == 0:
                queue.appendleft([next_x, next_y])
                visited[next_x][next_y] = visited[curr_x][curr_y]
            # next_x, next_y의 비용이 1이라면 비용이 0인 경로보다 나중에 탐색하도록 queue의 맨 뒤에 삽입
            else:
                queue.append([next_x, next_y])
                visited[next_x][next_y] = visited[curr_x][curr_y]+1
print(visited[n-1][m-1]-1)
