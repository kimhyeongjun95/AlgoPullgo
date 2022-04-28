import sys
from collections import deque

sys.stdin = open('input.txt')

i = 0
while True:

    N = int(input())
    if N:
        i += 1
        box = []

        visited = [[False] * N for _ in range(N)]
        score = [[99999] * N for _ in range(N)]

        for _ in range(N):
            box.append(list(map(int,input().split())))
        score[0][0] = box[0][0]
        q = deque()
        q.append((0,0))

        while q:
            b, a = q.popleft()
            visited[0][0] = True

            dxy = [(1, 0), (0, 1),(0, -1),(-1, 0)]
            for dx, dy in dxy:
                if 0 <= b+dy < N and 0 <= a+dx < N and visited[b+dy][a+dx] == 0:
                    if score[b+dy][a+dx] > box[b+dy][a+dx] + score[b][a]:
                        score[b+dy][a+dx] = box[b+dy][a+dx] + score[b][a]
                        q.append((b+dy, a+dx))
        print('Problem {} : {}'.format(i, score[N-1][N-1]))
    elif N == 0:
        break

