# 백준 14503 로봇 청소기

def dfs(x, y, d):
    global cnt

    # 현재 위치 청소
    if place[x][y] == 0:
        place[x][y] = 2
        cnt += 1

    left = d
    for _ in range(4):
        # 왼쪽 방향부터 차례로 인접한 칸 탐색
        left = (left+3)%4
        nx, ny = x+dxy[left][0], y+dxy[left][1]

        # 청소할 공간이 있다면,
        if place[nx][ny] == 0:
            dfs(nx, ny, left)
            return

    # 네 방향 모두 청소할 수 없다면,
    bx, by = x-dxy[left][0], y-dxy[left][1]

    if place[bx][by] != 1:
        dfs(bx, by, left)


N, M = map(int, input().split())
# d -> 0 : 북(-서) , 1 : 동쪽(-북), 2 : 남쪽(-동), 3 : 서쪽(-남)
r, c, d = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]

# 북동남서
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
dfs(r, c, d)

print(cnt)