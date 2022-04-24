import sys
sys.stdin = open('input.txt')

def jegu(y,x,k):
    global min_k
    if y == N-1 and x == N-1:
        if min_k > k:
            min_k = k
        return

    dxy = [(1,0), (0,1), (0,-1), (-1,0)]
    for dx,dy in dxy:
        if 0 <= x+dx < N and 0 <= y+dy < N and visited[y+dy][x+dx] == 0:
            visited[y+dy][x+dx] = 1
            jegu(y+dy, x+dx, k+box[y+dy][x+dx])
            visited[y+dy][x+dx] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = []

    visited = [[0] * N for _ in range(N)]
    for _ in range(N):
        box.append(list(map(int,input().split())))
    min_k = 1216549876455613
    visited[0][0] = 1
    jegu(0, 0, box[0][0])
    print(min_k)