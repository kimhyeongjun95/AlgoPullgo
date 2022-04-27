# 백준 1987 알파벳

# 세로 r 가로 c
# 1, 1에는 말이 있고 각각 알파벳이 있음.
# 각각 다른 알파벳을 지나가야함
# 최대 몇칸 갈 수 있는지?

import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1
def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)

BFS(0, 0)
print(answer)

import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs():
    global answer
    check = set([(0, 0, arr[0][0])])
    while check:
        x, y, count = check.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < r and -1 < ny < c:
                if (arr[nx][ny] not in count):
                    check.add((nx, ny, count + arr[nx][ny]))
                    answer = max(answer,len(count) +1)

r, c = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
answer = 0
bfs()
print(answer)