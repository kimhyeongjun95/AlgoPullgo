# 백준 4485 녹색 옷 입은 애가 젤다지?

# 화폐의 단위 : 루피
# 도둑루피 : 소지한 루피 감소

# N x N 동굴
# [0][0]번 칸
# [N-1][N-1]까지 이동
# 잃는 금액을 최소로 하여 이동
# 잃는 최소 금액 return

from collections import deque
tc = 1
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# dxy = [(0, 1), (1, 0)]
def bfs(queue, arr, visited):
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    queue.append((nx, ny))
    return visited[n-1][n-1]

while True:
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[float('inf')] * n for _ in range(n)]
    visited[0][0] = arr[0][0]
    answer = float('inf')
    queue = deque([(0, 0)])
    answer = bfs(queue, arr, visited)
    print(f'Problem {tc}: {answer}')

    tc += 1