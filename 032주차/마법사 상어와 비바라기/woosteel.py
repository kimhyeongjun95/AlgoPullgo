from collections import deque


N, M = map(int, input().split())
basket = []
order = deque()
for _ in range(N):
    basket.append(list(map(int, input().split())))
for _ in range(M):
    order.append(list(map(int, input().split())))

way = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1],
       [0, 1], [1, 1], [1, 0], [1, -1]]  # 이동 방향
cloud = deque([[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]])  # 초기 구름 상태

while order:
    visited = [[False for _ in range(N)] for _ in range(N)]
    d, s = order.popleft()

    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + way[d][0] * s) % N
        cloud[i][1] = (cloud[i][1] + way[d][1] * s) % N
        if cloud[i][0] < 0:
            cloud[i][0] += N
        if cloud[i][1] < 0:
            cloud[i][1] += N
        visited[cloud[i][0]][cloud[i][1]] = True
        basket[cloud[i][0]][cloud[i][1]] += 1

    while cloud:
        x, y = cloud.popleft()  # cloud 초기화
        cnt = 0
        for i in range(2, 9, 2):
            if 0 <= x + way[i][0] < N and 0 <= y + way[i][1] < N and basket[x + way[i][0]][y + way[i][1]]:
                basket[x][y] += 1

    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2 and not visited[i][j]:
                cloud.append([i, j])
                basket[i][j] -= 2

print(sum(map(sum, basket)))
