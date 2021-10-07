# 백준 16234 인구 이동

# N x N 크기의 땅, 각각의 땅에는 나라가 하나씩 존재
# 국경 공유 나라의 인구차이가
# -> L <= 차이 <= R 이라면 국경선 하루 동안 연다.
# 이동할 수 있으면 그 나라를 하루 동안은 '연합'이라고 부른다.
# 연합 = 연합의 인구수 / 연합을 이루고 있는 칸의 개수
# 연합 해체하고 국경선 닫기.

# 인구 이동이 며칠동안 발생하는가?

import sys
input = sys.stdin.readline
from collections import deque

dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def spreader(temp):
    count = 0
    for x, y in temp:
        count += arr[x][y]

    for x, y in temp:
        arr[x][y] = count // len(temp)

def migration(i, j):
    global happened
    union = False
    queue = deque([(i, j)])
    count = 0
    total = 0
    temp = []
    while queue:
        x, y = queue.popleft()
        count += 1
        total += arr[x][y]
        temp.append((x, y))

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if -1 < nx < n and -1 < ny < n:
                if l <= abs(arr[nx][ny]-arr[x][y]) <= r and not visited[nx][ny]:
                    happened = True
                    union = True
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    
    return union, happened, temp
    
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
happened = False
places = [[0] * n for _ in range(n)]
answer = 0

while True:
    forth = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union, happened, temp = migration(i, j)
                if union:
                    spreader(temp)
                    forth = True
    if not forth:
        break
   
    answer += 1

if happened:  
    print(answer)
else:
    print(0)