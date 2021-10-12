# 로봇 청소기
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def clean(r, c, d):
    area = (r, c, d)
    visited[r][c] = 1

    while area:
        x, y, d = area
        area = 0

        if d % 2:
            temp = (d + 2) % 4
        else:
            temp = d

        for i in range(4):
            nx, ny = x + dx[(temp + i) % 4], y + dy[(temp + i) % 4]
            d = (d + 3) % 4

            if -1 < nx < N and -1 < ny < M and not visited[nx][ny] and not matrix[nx][ny]:
                visited[nx][ny] = 1
                area = (nx, ny, d)
                break
        else:
            if d % 2:
                idx = d - 1
            else:
                idx = d + 1
            nx, ny = x + dx[idx], y + dy[idx]
            if -1 < nx < N and -1 < ny < M and not matrix[nx][ny]:
                area = (nx, ny, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
clean(r, c, d)
ans = 0
for i in range(N):
    ans += sum(visited[i])
print(ans)